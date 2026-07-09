"""Janela principal do aplicativo."""

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from software.ui.widgets.top_bar import TopBar
from software.ui.widgets.bottom_bar import BottomBar
from software.ui.widgets.scope_widget import Oscilloscope


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QMainWindow{
            background:#111111;
        }

        QWidget{
            background:#111111;
            color:white;
        }
        """)

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
