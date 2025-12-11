# TCS34725_RGB-Color-Sensor__RaspberryPi

The [TCS34725 RGB sensor](https://learn.adafruit.com/adafruit-color-sensors/overview) provides a digital return of red, green, blue (RGB), and clear light sensing values. An RGB Color sensor helps you accurately detect an object’s colour in your interactive projects.

----
**TCS34725 on-board white LED**

Used to provide constant illumination. 

The LED pin can be pulled low to turn off the LED. This can be done by:

  1. Wiring directly to ground to turn it off completely.
     
  2. Wiring to a spare digital pin and control it with digitalWrite().

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
VIN | 3.3V
SDA | SDA / GPIO2 / Pin3
SCL| SCL / GPIO3 / Pin5

----
### Python
----

Our programming language for this tutorial will be *Python*, which is the standard programming language included with a Raspberry Pi.

Learn more about Python [here](https://www.python.org/)

----
### PROGRAMMING INSTRUCTIONS

- Make sure your RPi is connected to internet (WIFI or Ethernet)

- Plug your Raspberry Pi and wait until you see the main Desktop
  
- Open the Raspberry Pi's Terminal (black top left icon).

- The RPi terminal should pop-up, looking similar to [this](https://github.com/kingston-hackSpace/TCS34725_RGB-Color-Sensor__RaspberryPi/blob/main/Terminal-view_.jpg)

- From now on, we will be typing instructions on the terminal only.


# Using the terminal

- Updating device and installing all necessary protocols:

  ```
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y python3-pip i2c-tools
  ```

- Create a directory for your project (located at Desktop):

  ```
  cd Desktop
  mkdir RGB_project
  cd RGB_project
  ```

- Create a Virtual Environment (venv) located at your new RGB_project directory:

  ```
  python3 -m venv venv
  ```

- **Activate your *Virtual Environment***

  ```
  source venv/bin/activate
  ```

- Install the tcs34725 sensor library:

  ```
  pip3 install adafruit-circuitpython-tcs34725
  ```

- Download python script from github

  ```
  wget https://github.com/kingston-hackSpace/TCS34725_RGB-Color-Sensor__RaspberryPi/archive/refs/heads/main.zip
  ```
  
- You should have a "main.zip" file located in your project directory. To confirm that everything went well, type the following:

  ```
  ls
  ```

- You should now see the zip file displayed in your terminal as part of your project directory.

- Unzip and go to main folder:

  ```
  unzip main.zip
  cd TCS34725_RGB-Color-Sensor__RaspberryPi-main
  ls
  ```

- From the last step ("ls" command), you should now see a file called "RGB_project.py".

- Run the python file:

  ```
  python3 RGB_project.py
  ```

- You should now see the reading from your sensor being printing on the terminal.

- To exit the readings and go back to your terminal:

  ```
  CTRL + C
  ```

- To modify the script:

  ```
  nano RGB_project.py
  ```
  
- To save and exit the script:

  ```
  CTRL + O
  CTRL + X
  ```
  
- To run the script again:

  ```
  python3 RGB_project.py
  ```
  
 


----
### MORE TUTORIALS

- [Interfacing a TCS34725 RGB Color Sensor With Arduino – A Complete Guide](https://www.makerguides.com/tcs34725-rgb-color-sensor-with-arduino/)

- [LED lighting based on colour readings](https://learn.adafruit.com/adafruit-color-sensors/arduino-code)
