# TCS34725_RGB-Color-Sensor__RaspberryPi

The [TCS34725 RGB sensor](https://learn.adafruit.com/adafruit-color-sensors/overview) provides a digital return of red, green, blue (RGB), and clear light (C) sensing values. An RGB Color sensor helps you accurately detect an object’s colour in your interactive projects.

----
**TCS34725 on-board white LED**

Used to provide constant illumination. 

On the Raspberry Pi, the LED pin can be wired to a GPIO pin and controlled manually. If left unconnected, the LED remains on by default due to internal pull-up.

----
# TUTORIAL SET-UP for Raspberry Pi
----
### HARDWARE

- Raspberry Pi
- TCS34725 sensor
----
### WIRING
Raspberry Pi GPIO [diagram here](https://github.com/kingston-hackSpace/RaspberryPi/blob/main/GPIO-diagram.png)

RGB Sensor | RPi GPIO
-|-
GND | GND
VIN | 3.3V or 5V
SDA | SDA / GPIO2 / Pin3
SCL| SCL / GPIO3 / Pin5

----
### Python
----

This tutorial uses *Python*, which is the standard programming language included with a Raspberry Pi.

Learn more about Python [here](https://www.python.org/).

----
### PROGRAMMING INSTRUCTIONS

- Ensure the RPi is connected to the internet (via WIFI or Ethernet).

- Power on the Raspberry Pi and wait until you see the main Desktop.
  
- Open the Raspberry Pi's Terminal (black icon at the top-left in your Desktop).

- The RPi Terminal should pop-up, looking similar to [this](https://github.com/kingston-hackSpace/TCS34725_RGB-Color-Sensor__RaspberryPi/blob/main/Terminal-view_.jpg)

- From now on, we will be typing instructions using the Terminal.


# Configure Dependancies

- Enable i2C:

      sudo raspi-config

- Navigate to *Interface Options* > *Enable I2C*

- Reboot the RPi
  
      sudo reboot

- Update and install all necessary protocols:

      sudo apt update && sudo apt upgrade -y
      sudo apt install -y python3-pip i2c-tools

----
# Virtual Environments

- Create a Virtual Environment (venv) located at your Desktop:

      cd Desktop
      python3 -m venv venv

- **Activate your *Virtual Environment***

      source venv/bin/activate

- More about Virtual Environments [here](https://github.com/kingston-hackSpace/Virtual-Environments__RaspberryPi/blob/main/README.md)
  
----
# Installting the TCS34725 library

- Create a directory for your project (located at Desktop):

      mkdir RGB_project
      cd RGB_project

- Install the tcs34725 sensor library:

      pip install adafruit-circuitpython-tcs34725

- Download the following python script:

      wget https://github.com/kingston-hackSpace/TCS34725_RGB-Color-Sensor__RaspberryPi/archive/refs/heads/main.zip
  
- You should have a "main.zip" file located in your project directory. To confirm that everything went well, type the following:
  
      ls
  
- You should now see the zip file displayed in your terminal as part of your project directory.

- Unzip and go to main folder:

      unzip main.zip
      cd TCS34725_RGB-Color-Sensor__RaspberryPi-main
      ls

- From the last step ("ls" command), you should now see a file called "RGB_project.py".

- Run the python file:

      python3 RGB_project.py

- You should now see the reading from your sensor being printed on the terminal.

- To exit the readings and go back to the terminal:

      CTRL + C
  
- To modify the script:

      nano RGB_project.py

- To save and exit the script:

      Save : CTRL + O -> Enter
      Exit : CTRL + X

- To run the script again, type:

      python3 RGB_project.py

**IMPORTANT NOTE: **

The dependencies for this script were installed in the virtual environment that you previously created. You will always need to be inside the virtual environment to successfully run this script. 

----
### MORE TUTORIALS

- [Interfacing a TCS34725 RGB Color Sensor With Arduino – A Complete Guide](https://www.makerguides.com/tcs34725-rgb-color-sensor-with-arduino/)

- [LED lighting based on colour readings](https://learn.adafruit.com/adafruit-color-sensors/arduino-code)
