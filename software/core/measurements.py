"""
==========================================
OpenScope
Medições da forma de onda.
==========================================
"""
from frequency import Frequency

class Measurements:

    ADC_MAX = 1023
    VREF = 5.0

    @staticmethod
    def adc_to_voltage(value):

        return value * Measurements.VREF / Measurements.ADC_MAX

    @staticmethod
    def analyze(samples):

        if not samples:
            return None

        adc_max = max(samples)
        adc_min = min(samples)

        vmax = Measurements.adc_to_voltage(adc_max)
        vmin = Measurements.adc_to_voltage(adc_min)
        vpp = vmax - vmin

        period = Frequency.analyze(samples)

        return {
            "vmax": vmax,
            "vmin": vmin,
            "vpp": vpp,
            "period": period
        }