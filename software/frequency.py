"""
==========================================
OpenScope
Autor: Jvguzatty

Medição de frequência.
==========================================
"""

from utils.config import SAMPLE_COUNT


class Frequency:

    @staticmethod
    def analyze(samples):

        if len(samples) < 2:
            return 0

        level = (max(samples) + min(samples)) / 2

        edges = []

        for i in range(1, len(samples)):

            if samples[i - 1] < level and samples[i] >= level:

                edges.append(i)

        if len(edges) < 2:
            return 0

        period = edges[1] - edges[0]

        return period