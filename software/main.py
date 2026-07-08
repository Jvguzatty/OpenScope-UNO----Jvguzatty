print("Programa iniciado")

import sys

from PySide6.QtWidgets import QApplication

from serial_manager import SerialManager
from oscilloscope import Oscilloscope


app = QApplication(sys.argv)

scope = Oscilloscope()

scope.widget.setWindowTitle("OpenScope UNO -- Jvguzatty")

scope.widget.show()

serial = SerialManager("COM3", 115200)


while True:

    samples = serial.read_samples()

    scope.update(samples)

    app.processEvents()