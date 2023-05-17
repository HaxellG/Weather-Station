# Temperature and Humidity Monitor with Raspberry Pi

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

Then, you can run the script. The Raspberry Pi will start measuring temperature and humidity and display the data on the 
OLED display. It will also serve a web page that will display this data. To access the web page, open a browser on any 
device connected to the same network and navigate to the Raspberry Pi's IP address on port 80.

For example, if the Raspberry Pi's IP address is 192.168.1.100, navigate to http://192.168.1.100.

The web page will automatically refresh every 10 seconds with the latest data.

Please note that the script is configured to use pins 0 and 1 for the I2C connection to the OLED display, and pin 20 for the DHT11 sensor. If your devices are connected to different pins, you will need to modify these values in the script.
