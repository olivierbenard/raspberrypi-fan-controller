# -*- coding: utf-8 -*-
# to be moved to /usr/local/bin
# sudo chmod +x /usr/local/bin/fancontroller.py

import vcgencmd
from gpiozero import OutpuDevice


# IMPORTANT: maximum temperature is 85°C and cpu throttled at 80°C

ON_THRESHOLD = 70 # (degrees Celsius) fan starts at this temperature
OFF_THRESHOLD = 60 # (degrees Celsius) fan shuts down at this temperature
SLEEP_INTERVAL = 5 # (seconds) how often the core temperature is checked
GPIO_PIN = 18 # (number) which GPIO pin is used to control the fan

def main():

    vc = vcgencmd.Vcgencmd()
    fan = OutpuDevice(GPIO_PIN)

    while True:
        temperature = int(vc.measure_temp())
        # NOTE: fan.value = 1 if "on" else 0
        if temperature > ON_THRESHOLD and not fan.value:
            fan.on()
        elif fan.value and temperature < OFF_THRESHOLD:
            fan.off()
        time.sleep(SLEEP_INTERVAL)


if __name__ == '__main__':
    main()
