"""
==========================================
OpenScope
Autor: Jvguzatty

Barra inferior.
==========================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout
)

from styles import *


class BottomBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(40)

        self.setStyleSheet(f"""
            background-color:{BACKGROUND};
            color:{TEXT};
        """)

        layout = QHBoxLayout()

        self.vmax = QLabel("Vmax: ---")
        self.vmin = QLabel("Vmin: ---")
        self.vpp = QLabel("Vpp: ---")

        self.samples = QLabel("Samples: 256")
        self.fps = QLabel("FPS: --")

        layout.addWidget(self.vmax)
        layout.addSpacing(25)

        layout.addWidget(self.vmin)
        layout.addSpacing(25)

        layout.addWidget(self.vpp)

        layout.addStretch()

        layout.addWidget(self.samples)

        layout.addSpacing(30)

        layout.addWidget(self.fps)

        self.setLayout(layout)

    def updateMeasurements(self, data):

        self.vmax.setText(f"Vmax: {data['vmax']:.2f} V")
        self.vmin.setText(f"Vmin: {data['vmin']:.2f} V")
        self.vpp.setText(f"Vpp: {data['vpp']:.2f} V")

    def updateFPS(self, fps):

        self.fps.setText(f"FPS: {fps:.1f}")