#include <Arduino.h>

#include "config.h"
#include "serial.h"
#include "adc.h"

uint16_t samples[SAMPLE_COUNT];

void setup()
{
    serialInit();

    pinMode(9, OUTPUT);
    analogWrite(9, 128);

    adcInit();
}

void loop()
{
    adcCapture(samples, SAMPLE_COUNT);

    serialSendSamples(samples, SAMPLE_COUNT);
}