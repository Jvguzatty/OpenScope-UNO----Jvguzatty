#include "serial.h"
#include "config.h"

void serialInit()
{
    Serial.begin(SERIAL_BAUD);
    delay(1);
}

void serialSendSamples(const uint16_t* buffer, uint16_t size)
{
    Serial.println("BEGIN");

    for (uint16_t i = 0; i < size; i++)
    {
        Serial.println(buffer[i]);
    }

    Serial.println("END");
}