"""Preparación dos sensores e actuadores para o proxecto.
Matheus Omena Ribeiro. 25/02/2026"""

import time
from machine import (
    ADC,
    Pin,
)  # Importamos as liberias que axudarán na práctica

pinturbidez = 14
# Sensor
turbidez = ADC(Pin(pinturbidez))
turbidez.atten(ADC.ATTN_11DB)  # Hasta 3.3V
turbidez.width(ADC.WIDTH_12BIT)  # 12 bits (0–4095)

# Bucle principal
while True:
    valorturbidez = turbidez.read()
    print("turbidez:", valorturbidez)
    time.sleep_ms(1000)
