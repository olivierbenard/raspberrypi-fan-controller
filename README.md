# raspberrypi-fan-controller
Switch on or off the fan connected to the RaspberryPi depending of the temperature.

## Fan controller code

Move the script _fancontroller.py_ to **/usr/local/bin/**
```
sudo mv fancontroller.py /usr/local/bin/
```

Then, make the script executable
```
sudo chmod +x /usr/local/bin/fancontroller.py
```

## Execute the fan controller code on boot

Move the script _fancontroller.sh_ to **/etc/init.d**
```
sudo mv fancontroller.sh /etc/init.d/
```

Then, make the script executable
```
sudo chmod +x /etc/init.d/fancontroller.sh
```

Now, register the script to run on boot
```
sudo update-rc.d fancontroller.sh defaults
```

Finally, restart the machine or kick off manually:
```
sudo reboot
```
or
```
sudo /etc/init.d/fancontroller.sh start
```
