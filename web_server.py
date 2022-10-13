import network
import socket
from time import sleep
import machine
import credentials

pico_led = machine.Pin("LED", machine.Pin.OUT)
relay = machine.Pin(6, machine.Pin.OUT)


def findTemperature():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    return 27 - ((sensor_temp.read_u16() * conversion_factor) - 0.706)/0.001721


def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(credentials.ssid, credentials.password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip


def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def webpage(temperature, state):
    # Template HTML
    page = open("index.html", "r")
    html = page.read()
    page.close()
    html = str(html).replace("{temperature}", str(temperature))
    html = html.replace("{state}", str(state))
    return html


def serve(connection):
    # Start a web server
    state = 'OFF'
    pico_led.off()
    relay.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/heatingon?':
            pico_led.on()
            relay.on()
            state = 'ON'
        elif request == '/heatingoff?':
            pico_led.off()
            relay.off()
            state = 'OFF'
        temperature = findTemperature()
        html = webpage(temperature, state)
        client.send(html)
        client.close()
