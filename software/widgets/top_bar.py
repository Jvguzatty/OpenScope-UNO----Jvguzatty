"""
==========================================
OpenScope
Autor: Jvguzatty

Barra superior do software.
==========================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout
)

from PySide6.QtCore import Qt

from styles import *


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(45)

        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
            color: {TEXT};
        """)

        layout = QHBoxLayout()

        self.title = QLabel("📈 OpenScope")

        self.title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        self.com = QLabel("COM3")

        self.run = QLabel("🟢 RUN")

        layout.addWidget(self.title)

        layout.addStretch()

        layout.addWidget(self.com)

        layout.addSpacing(20)

        layout.addWidget(self.run)

        self.setLayout(layout)