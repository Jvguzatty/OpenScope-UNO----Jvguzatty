"""
==========================================
OpenScope
Autor: Jvguzatty

Aquisição de dados.
==========================================
"""

from trigger import Trigger

class Acquisition:

    def __init__(self, serial):

        self.serial = serial

    def capture(self):

        samples = self.serial.read_samples()

        samples = Trigger.process(samples)

        return samples