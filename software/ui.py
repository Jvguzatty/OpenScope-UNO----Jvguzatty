"""
==========================================
OpenScope
Autor: Jvguzatty

Janela principal.
==========================================
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout
)

from widgets.top_bar import TopBar
from widgets.bottom_bar import BottomBar
from widgets.scope_widget import Oscilloscope


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenScope -- Jvguzatty")

        self.resize(1200, 700)

        central = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.topBar = TopBar()
        self.scope = Oscilloscope()
        self.bottomBar = BottomBar()

        layout.addWidget(self.topBar)
        layout.addWidget(self.scope.widget)
        layout.addWidget(self.bottomBar)

        central.setLayout(layout)

        self.setCentralWidget(central)