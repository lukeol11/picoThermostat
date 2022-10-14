# Smart Pico W Thermostat

## Description

Control you home heating using a Raspberry Pi W.

### Possible features

- [x] Toggle Relay
- [x] Control heating using http web server
  - [x] ON/OFF Functionality
  - [x] Toggle Thermostat functionality
  - [x] Temperature Display
  - [ ] Static IP Address
  - [ ] Change thermostat temperature
  - [ ] Time setting
  - [ ] Weather display
- [x] Control heating using onboard temperature sensor
  - [ ] Move from [web_server.py](web_server.py) to [thermostat.py](thermostat.py)
- [ ] Control heating using time
- [ ] Control heating using weather api
- [ ] Control heating using physical buttons
- [ ] Control heating using Google Assistant

## Setup

### Required files

- [main.py](main.py)
- [web_server.py](web_server.py)
- [index.html](index.html)
- [credentials.py](credentials.py)

## Hardware

- Raspberry Pi Pico W
- sb components Pico Single Channel Relay HAT

## Software

- Language: Micropython
