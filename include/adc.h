#pragma once

#include <Arduino.h>

void adcInit();
void adcCapture(uint16_t* buffer, uint16_t size);