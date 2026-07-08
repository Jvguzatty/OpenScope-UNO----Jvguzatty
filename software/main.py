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
from measurements import Measurements

from serial_manager import SerialManager
from ui import MainWindow


app = QApplication(sys.argv)

window = MainWindow()

window.show()

serial = SerialManager("COM3", 115200)

while True:

    samples = serial.read_samples()

    window.scope.update(samples)
    
    measurements = Measurements.analyze(samples)

    if measurements:
        window.bottomBar.updateMeasurements(measurements)

    app.processEvents()