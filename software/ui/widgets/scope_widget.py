"""Widget do oscilloscope."""

import pyqtgraph as pg
from software.styles import BACKGROUND, WAVE


class Oscilloscope:

    def __init__(self):
        self.widget = pg.PlotWidget()
        self.widget.setBackground(BACKGROUND)
        self.widget.showGrid(x=True, y=True, alpha=0.25)
        self.widget.setMouseEnabled(False, False)
        self.widget.hideButtons()
        self.widget.setMenuEnabled(False)
        self.widget.setLimits(xMin=0, xMax=255)

        pen = pg.mkPen(color=WAVE, width=2)
        self.curve = self.widget.plot(pen=pen)

    def update(self, samples):
        if not samples:
            return

        ymin = min(samples)
        ymax = max(samples)
        margem = max((ymax - ymin) * 0.30, 100)

        self.widget.setYRange(ymin - margem, ymax + margem)
        self.curve.setData(samples)
