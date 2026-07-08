#include <Arduino.h>

void setup()
{
    Serial.begin(9600);

    // Espera um instante para a Serial estabilizar
    delay(1000);

    Serial.println("Arduino iniciado!");
}

void loop()
{
    Serial.println("Teste");
    delay(1000);
}