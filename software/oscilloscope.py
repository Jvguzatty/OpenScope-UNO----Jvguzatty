import pyqtgraph as pg


class Oscilloscope:

    def __init__(self):

        self.widget = pg.PlotWidget()

        self.widget.setYRange(0, 1023)

        self.curve = self.widget.plot()

    def update(self, samples):

        self.curve.setData(samples)