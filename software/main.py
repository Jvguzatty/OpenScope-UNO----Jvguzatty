# ==========================================
# COMO EXECUTAR O OPENSCOPE
#
# Abra o terminal na pasta do projeto e execute:
#
# python software/main.py
#
# ==========================================

import sys

from PySide6.QtWidgets import QApplication
from software.core.measurements import Measurements
from software.core.fps import FPS


from software.Communication.serial_manager import SerialManager
from software.core.acquisition import Acquisition
from ui import MainWindow


app = QApplication(sys.argv)

window = MainWindow()

fpsCounter = FPS()

window.show()

from utils.config import *

serial = SerialManager(
    SERIAL_PORT,
    SERIAL_BAUD
)

acquisition = Acquisition(serial)

import time

while True:
    
    start = time.perf_counter()

    samples = acquisition.capture()

    window.scope.update(samples)

    
    measurements = Measurements.analyze(samples)

    if measurements:
        window.bottomBar.updateMeasurements(measurements)
        fps = fpsCounter.update()
        window.bottomBar.updateFPS(fps)

    app.processEvents()

    elapsed = time.perf_counter() - start

    print(f"{elapsed*1000:.2f} ms")