#include "adc.h"

void adcInit()
{
    // Referência AVcc e canal ADC0 (A0)
    ADMUX = (1 << REFS0);

    // Liga o ADC
    // Prescaler = 128
    ADCSRA =
        (1 << ADEN) |
        (1 << ADPS2) |
        (1 << ADPS1) |
        (1 << ADPS0);
}

uint16_t adcRead()
{
    // Inicia conversão
    ADCSRA |= (1 << ADSC);

    // Espera terminar
    while (ADCSRA & (1 << ADSC));

    return ADC;
}

void adcCapture(uint16_t* buffer, uint16_t size)
{
    for (uint16_t i = 0; i < size; i++)
    {
        buffer[i] = adcRead();
    }
}