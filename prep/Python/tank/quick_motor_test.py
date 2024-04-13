Motor_A_EN = 4
Motor_B_EN = 17

Motor_A_Pin1 = 14
Motor_A_Pin2 = 15
Motor_B_Pin1 = 27
Motor_B_Pin2 = 18
# left_motor = Motor(Motor_B_EN, Motor_B_Pin1, Motor_B_Pin2)
# right_motor = Motor(Motor_A_EN, Motor_A_Pin2, Motor_A_Pin1)

import gpiozero as gz
import time 

pin1a = gz.DigitalOutputDevice(14)
pin2a = gz.DigitalOutputDevice(15)
ena = gz.PWMOutputDevice(4)

pin1b = gz.DigitalOutputDevice(18)
pin2b = gz.DigitalOutputDevice(27)
enb = gz.PWMOutputDevice(17)

print("Ready")
time.sleep(1)
pin1a.on()
pin2a.off()
ena.value = 1.0
print("Go")
time.sleep(2)
ena.value = 0
pin1a.off()

print("Ready")
time.sleep(1)
pin1b.on()
pin2b.off()
enb.value = 1.0
print("Go")
time.sleep(2)
enb.value = 0
pin1b.off()



print("Ready")
time.sleep(1)
pin1a.on()
pin2a.off()
pin1b.on()
pin2b.off()
ena.value = 1.0
enb.value = 1.0
print("Go")
time.sleep(2)
ena.value = 0
pin1a.off()
enb.value = 0
pin1b.off()

print("Goodbye")

