#pragma once

#include <Arduino.h>

// ===============================
// Configurações gerais
// ===============================

// Comunicação Serial
constexpr uint32_t SERIAL_BAUD = 115200;

// Entrada analógica
constexpr uint8_t ADC_PIN = A0;

// Quantidade de amostras por captura
constexpr uint16_t SAMPLE_COUNT = 256;