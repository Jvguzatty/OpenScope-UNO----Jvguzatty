#pragma once

#include <Arduino.h>

void adcInit();
uint16_t adcRead();
void adcCapture(uint16_t* buffer, uint16_t size);