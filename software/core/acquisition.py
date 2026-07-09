"""
==========================================
OpenScope
Autor: Jvguzatty

Aquisição de dados.
==========================================
"""

import serial


class Acquisition:

    def __init__(self, serial_port):
        self.serial = serial_port

    def capture(self):
        try:
            return self.serial.read_samples()
        except (serial.SerialException, TimeoutError, ValueError):
            return []