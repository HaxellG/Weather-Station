try:
    import usocket as socket
except:
    import socket

import network

from machine import Pin, I2C
import time
from dht import DHT11
from ssd1306 import SSD1306_I2C
import framebuf

ssid = "MANDALOR"
password = "laperradaderocky2016"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("Conexión éxitosa")
print(station.ifconfig())

pin = Pin(20, Pin.IN, Pin.PULL_UP)
dht11 = DHT11(pin, None, dht11 = True)

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)

T, H = dht11.read()

def lectura_sensor():
    T, H = dht11.read()
    try:
        oled.text("Temperatura: "+ str(T)+"C", 0, 0)
        oled.text("Humedad: "+ str(H)+"%", 0, 30)
        oled.show()
        print(f"Temperatura: {T}°C")
        print(f"Humedad: {H}%")
    except:
        print("Error...")
    time.sleep(2)
    return()

def pagina_web():
  html = """<!DOCTYPE HTML><html>
<head>
  <meta http-equiv=\"refresh\" content=\"10\">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 2.0rem; }
    p { font-size: 2.0rem; }
    .units { font-size: 1.2rem; }
    .bme-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
  </style>
</head>
<body>
  <h2>DHT11 usando Raspberry</h2>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="bme-labels">Temperatura:</span> 
    <span>"""+str(T)+"""</span>
    <span class="bme-labels">°C</span>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="bme-labels">Humedad:</span>
    <span>"""+str(H)+"""</span>
    <span class="bme-labels">%</span>
  </p>
</body>
</html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conexion, direccion = s.accept()
  request = conexion.recv(1024)
  lectura_sensor()
  respuesta = pagina_web()
  conexion.send('HTTP/1.1 200 OK\n')
  conexion.send('Content-Type: text/html\n')
  conexion.send('Connection: close\n\n')
  conexion.sendall(respuesta)
  conexion.close()