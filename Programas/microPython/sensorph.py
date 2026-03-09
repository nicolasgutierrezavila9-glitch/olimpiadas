"""Preparación dos sensores e actuadores para o proxecto.
Matheus Omena Ribeiro. 25/02/2026"""

import time
from machine import (
    ADC,
    Pin,
)  # Importamos as liberias que axudarán na práctica

pinph = 12
# Sensor
ph = ADC(Pin(pinph))
ph.atten(ADC.ATTN_11DB)  # Hasta 3.3V
ph.width(ADC.WIDTH_12BIT)  # 12 bits (0–4095)

# Bucle principal
while True:
    valorph = ph.read()
    print("ph:", valorph)
    time.sleep_ms(1000)
