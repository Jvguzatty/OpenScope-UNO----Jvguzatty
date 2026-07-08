#include "serial.h"
#include "config.h"

void serialInit()
{
    Serial.begin(SERIAL_BAUD);
    delay(1);
}

void serialSendSamples(const uint16_t* buffer, uint16_t size)
{
    constexpr uint8_t HEADER[] = {0xAA, 0x55};
    constexpr uint8_t FOOTER[] = {0x55, 0xAA};

    Serial.write(HEADER, sizeof(HEADER));

    Serial.write(
        reinterpret_cast<const uint8_t*>(buffer),
        size * sizeof(uint16_t)
    );

    Serial.write(FOOTER, sizeof(FOOTER));
}