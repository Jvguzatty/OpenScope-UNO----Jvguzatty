"""
==========================================
OpenScope
Autor: Jvguzatty

Cálculo de FPS.
==========================================
"""

import time


class FPS:

    def __init__(self):

        self.last_time = time.time()

        self.fps = 0

    def update(self):

        current_time = time.time()

        delta = current_time - self.last_time

        self.last_time = current_time

        if delta > 0:

            self.fps = 1 / delta

        return self.fps