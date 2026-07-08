#pragma once

#include <Arduino.h>

void serialInit();
void serialSendSamples(const uint16_t* buffer, uint16_t size);