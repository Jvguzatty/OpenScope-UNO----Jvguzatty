import struct
import unittest

from software.communication.serial_manager import SerialManager
from software.utils.config import SAMPLE_COUNT


class SerialManagerTests(unittest.TestCase):
    def test_parse_frame_with_valid_header_footer_and_payload(self):
        samples = [0, 1, 1023] * (SAMPLE_COUNT // 3 + 1)
        samples = samples[:SAMPLE_COUNT]
        payload = struct.pack(f"<{SAMPLE_COUNT}H", *samples)
        frame = SerialManager.HEADER + struct.pack("<H", SAMPLE_COUNT) + payload + SerialManager.FOOTER

        parsed = SerialManager.parse_frame(frame)

        self.assertEqual(parsed, samples)

    def test_parse_frame_rejects_invalid_footer(self):
        payload = struct.pack(f"<{SAMPLE_COUNT}H", *([0] * SAMPLE_COUNT))
        frame = SerialManager.HEADER + struct.pack("<H", SAMPLE_COUNT) + payload + b"\x00"

        with self.assertRaises(ValueError):
            SerialManager.parse_frame(frame)


if __name__ == "__main__":
    unittest.main()
