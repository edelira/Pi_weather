import time
from xml.dom import minidom
import urllib
from neopixel import *
from random import *

# LED strip configuration:
LED_COUNT      = 13      # Number of LED pixels.
LED_PIN        = 18       # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
def twinkle (strip,color,count,speed):
    repeat = 0
    while repeat != 10:
        repeat += 1
        for i in range(count):
            strip.setPixelColor(randrange(LED_COUNT), color)
            strip.show()
            time.sleep(speed)
        ColorWipe(strip, Color(0,0,0))

def snowspark(strip,color,sparklenght,speed):
    repeat = 0
    while repeat != 10:
        repeat += 1
        colorWipe(strip, Color(55, 55, 55))

        light = randrange(LED_COUNT)
        strip.setPixelColor(light,color)
        strip.show()
        time.sleep(sparklenght)
        strip.setPixelColor(light,Color(55,55,55))
        strip.show()
        time.sleep(speed)
                
def thunder(strip, frequency):
    repeat = 0
    while repeat != 10:
        repeat += 1
        light = 255
        colorWipe(strip, Color(255, 255, 255))
        
        while light != 0 :
            light -=15
            colorWipe(strip, Color(light, light, light))
            time.sleep(.02)
        time.sleep(randrange(frequency))
def moonlight(strip,intensity):
    for i in range(intensity):
        strip.setPixelColor(i,Color(255, 248, 100))
        strip.show()
        time.sleep(5)
def sunlight(strip, intensity):
    for i in range(intensity):
        strip.setPixelColor(i,Color(200, 135, 17))
        strip.show()
        time.sleep(5)
        
API_key = "Place API key here"

while True:
	time.sleep(5)
	url_str = 'http://api.openweathermap.org/data/2.5/weather?id=4887398&units=imperial&mode=xml&APPID=%s' %API_key
	xml_str = urllib.urlopen(url_str).read()
	xmldoc = minidom.parseString(xml_str)

	weather = xmldoc.getElementsByTagName('weather')
	icon = weather[0].attributes['icon'].value
	print icon
	
	if icon == '01d':
		print "clear sky"
		sunlight(strip,13)
	elif icon == '01n':
		print "clear sky night"	
		moonlight(strip,13)
	elif icon == '02d':
		print "few clouds"
		sunlight(strip,9)
	elif icon == '02n':
		print "few clouds night"
		moonlight(strip,9)
	elif icon == '03d':
		print "scattered clouds"
		sunlight(strip,6)
	elif icon == '03n':
		print "scattered clouds night"
		moonlight(strip,6)
	elif icon == '04d':
		print "broken clouds"
		sunlight(strip,3)
	elif icon == '04n':
		print "broken clouds night"
		moonlight(strip,3)
	elif icon == '09d':
		print "shower rain"	
		twinkle(strip,Color(0,17,255),4,1)
	elif icon == '09n':
		print "shower rain night"
		twinkle(strip,Color(0,17,255),4,1)
	elif icon == '10d':
		print "rain"
		twinkle(strip,Color(0,17,255),9,.5)
	elif icon == '10n':
		print "rain night"
		twinkle(strip,Color(0,17,255),9,.5)
	elif icon == '11d':
		print "thunderstorm"
		thunder(strip,10)
	elif icon == '11n':
		print "thunderstorm night"	
		thunder(strip,10)
	elif icon == '13d':
		print "snow"
		snowspark(strip,Color(255,255,255),.2,2)
	elif icon == '13n':
		print "snow night"
		snowspark(strip,Color(255,255,255),.2,2)
	elif icon == '50d':
		print "mist"	
	elif icon == '50n':
		print "mist night"