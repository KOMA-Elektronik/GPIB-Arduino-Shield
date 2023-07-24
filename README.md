# **GPIB ARDUINO SHIELD**

This repo contains a little set of tools to talk to old digital multimeters (DMM) via GPIB.

### You'll need:
* Arduino Uno R3
* GPIB Shield from this repo (production files available)
* GPIB capable DMM
* GPIB cable
* PC with Python 3 installed and USB cable
* `serial` library for Python

### How to set it up:

* connect an Arduino Uno R3 over USB to the computer
* attach the GPIB Shield with a GPIB cable connected to the DMM
* run the Python script

# GPIB Connection
The very old (and very bad) standard [IEEE-488](https://en.wikipedia.org/wiki/IEEE-488) is available on the back of a lot of older DMMs. With the help of an Arduino Uno R3 board, the 8-bit parallel bus can be converted to a serial connection and send over to the host PC via USB. 

# Contribution
If you find this repository useful and implemented a connection to a DMM that has not yet been added to the `Devices` folder - we would love to add it!