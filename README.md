# Welcome to my Pi Weather Cloud
This project is to create a LED cloud that changes colors based on current weather in my city (Chicago).


## Getting Started

These instructions will get you a copy of the project up and running on your Raspberry Pi and give you an idea of different patterns you can create using addressable LED strips.

### Prerequisites

Before getting this program running on your raspberry pi you would need to learn how to wire your LED strip to the Pi and have an OpenWeatherMap API
1. Adafruit has a great tutorial to follow to get wired up. [Wiring up your Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)
2. You need to request an API Key from the OpenWeatherMap website [Requesting API Key](https://openweathermap.org/appid)
### Installing
1. Move working directory to where you would like the program installed.

        $ cd ~/
        $ git clone https://github.com/edelira/Pi_weather.git

2. Navigate to the directory created

        $ cd Pi_weather

3.  Open Pi_led.py and add your API Key on line 63 "Place your API key here"

        $ sudo nano led_weather.py
    Save program and exit.
4.  Run program

        $ sudo python led_weather.py
5. Enjoy!