# ==========================================
# COMO EXECUTAR O OPENSCOPE
#
# python -m software.main
#
# ==========================================

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from software.communication.serial_manager import SerialManager
from software.core.acquisition import Acquisition
from software.core.fps import FPS
from software.core.measurements import Measurements
from software.ui.main_window import MainWindow
from software.utils.config import SERIAL_BAUD, SERIAL_PORT


app = QApplication(sys.argv)

window = MainWindow()
window.show()

serial = SerialManager(
    SERIAL_PORT,
    SERIAL_BAUD
)

acquisition = Acquisition(serial)
fpsCounter = FPS()


def update():

    samples = acquisition.capture()

    print("Samples:", len(samples))

    if not samples:
        return

    window.scope.update(samples)

    measurements = Measurements.analyze(samples)

    if measurements:
        window.bottomBar.updateMeasurements(measurements)

    fps = fpsCounter.update()
    window.bottomBar.updateFPS(fps)


timer = QTimer()
timer.timeout.connect(update)

# 0 = executa o mais rápido possível sem travar a interface
timer.start(0)

sys.exit(app.exec())