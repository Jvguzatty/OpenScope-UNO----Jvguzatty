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

        layout.addWidget(self.vmax)

        layout.addSpacing(25)

        layout.addWidget(self.vmin)

        layout.addSpacing(25)

        layout.addWidget(self.vpp)

        layout.addStretch()

        layout.addWidget(self.samples)

        self.setLayout(layout)