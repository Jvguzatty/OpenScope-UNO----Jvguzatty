"""
==========================================
OpenScope
Autor: Jvguzatty

Processamento de Trigger.
==========================================
"""


class Trigger:

    @staticmethod
    def process(samples):

        if len(samples) < 2:
            return samples

        level = 512

        trigger_index = 0

        for i in range(1, len(samples)):

            if samples[i - 1] < level and samples[i] >= level:

                trigger_index = i
                break

        return samples[trigger_index:] + samples[:trigger_index]