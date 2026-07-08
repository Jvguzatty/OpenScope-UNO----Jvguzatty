# ==========================================
# COMO EXECUTAR O OPENSCOPE
#
# Abra o terminal na pasta do projeto e execute:
#
# python -m software.main
#
# ==========================================

import sys
import time

from PySide6.QtWidgets import QApplication

from software.core.measurements import Measurements
from software.core.fps import FPS
from software.communication.serial_manager import SerialManager
from software.core.acquisition import Acquisition
from software.ui.main_window import MainWindow
from software.utils.config import SERIAL_PORT, SERIAL_BAUD


app = QApplication(sys.argv)

window = MainWindow()

fpsCounter = FPS()

window.show()

serial = SerialManager(
    SERIAL_PORT,
    SERIAL_BAUD
)

acquisition = Acquisition(serial)

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