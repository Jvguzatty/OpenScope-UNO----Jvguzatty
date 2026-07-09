"""
==========================================
OpenScope
Autor: Jvguzatty

Comunicação Serial
==========================================
"""

import struct
import time

import serial

from software.utils.config import SAMPLE_COUNT


class SerialManager:

    HEADER = b"\xAA\x55"
    FOOTER = b"\x55\xAA"
    COUNT_SIZE = 2

    def __init__(self, port="COM3", baudrate=115200):
        self.serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=0.1,
        )
        time.sleep(2)
        self.serial.reset_input_buffer()
        self._buffer = bytearray()

    @classmethod
    def parse_frame(cls, frame):
        if len(frame) < len(cls.HEADER) + cls.COUNT_SIZE + len(cls.FOOTER):
            raise ValueError("Frame too short")

        if frame[:2] != cls.HEADER:
            raise ValueError("Invalid header")

        if frame[-2:] != cls.FOOTER:
            raise ValueError("Invalid footer")

        sample_count = struct.unpack_from("<H", frame, 2)[0]
        if sample_count != SAMPLE_COUNT:
            raise ValueError(f"Unexpected sample count: {sample_count}")

        payload_start = len(cls.HEADER) + cls.COUNT_SIZE
        payload_end = payload_start + sample_count * 2
        expected_length = payload_end + len(cls.FOOTER)

        if len(frame) != expected_length:
            raise ValueError(f"Unexpected frame length: {len(frame)}")

        return list(struct.unpack(f"<{sample_count}H", frame[payload_start:payload_end]))

    def read_samples(self):
        while True:
            while len(self._buffer) < 4:
                chunk = self.serial.read(1)
                if not chunk:
                    raise TimeoutError("Timed out waiting for serial frame")
                self._buffer.extend(chunk)

            if self._buffer[:2] != self.HEADER:
                self._buffer.pop(0)
                continue

            sample_count = struct.unpack_from("<H", self._buffer, 2)[0]
            if sample_count != SAMPLE_COUNT:
                self._buffer.pop(0)
                continue

            expected_length = len(self.HEADER) + self.COUNT_SIZE + sample_count * 2 + len(self.FOOTER)

            while len(self._buffer) < expected_length:
                chunk = self.serial.read(1)
                if not chunk:
                    raise TimeoutError("Timed out waiting for serial frame")
                self._buffer.extend(chunk)

            frame = bytes(self._buffer[:expected_length])

            if frame[-2:] != self.FOOTER:
                self._buffer.pop(0)
                continue

            self._buffer = self._buffer[expected_length:]
            return self.parse_frame(frame)