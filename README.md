# README Temperature and Humidity Monitor with Raspberry Pi

# Description:
This is a MicroPython script used to monitor temperature and humidity using a DHT11 sensor on a Raspberry Pi Pico W. 
It also displays the collected data on an SSD1306 OLED display. Additionally, it can serve a web page to view this data 
in real-time on any device connected to the same network.

# Dependencies:
To run this code, you will need the following libraries and modules:

usocket, 
network, 
machine, 
time, 
dht, 
ssd1306, 
framebuf

You will also need a DHT11 sensor and an SSD1306 display, both connected to your Raspberry Pi.

# Usage:
First, make sure your Raspberry Pi is connected to the same network as your viewing device. Modify the ssid and password 
variables in the script to match your network's.
