import pyqtgraph as pg

from styles import *


class Oscilloscope:

    def __init__(self):

        self.widget = pg.PlotWidget()

        self.widget.setBackground(BACKGROUND)

        self.widget.showGrid(
            x=True,
            y=True,
            alpha=0.25
        )

        self.widget.setYRange(0, 1023)

        self.widget.setMouseEnabled(False, False)

        self.widget.hideButtons()

        self.widget.setMenuEnabled(False)

        pen = pg.mkPen(
            color=WAVE,
            width=2
        )

        self.curve = self.widget.plot(pen=pen)

    def update(self, samples):

        if not samples:
            return

        ymin = min(samples)
        ymax = max(samples)

        margem = (ymax - ymin) * 0.10

        if margem < 5:
            margem = 5

        self.widget.setYRange(
            ymin - margem,
            ymax + margem
        )

        self.curve.setData(samples)