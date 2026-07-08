#pragma once

#include <Arduino.h>

void serialInit();
void serialSendSamples(uint16_t* buffer, uint16_t size);
