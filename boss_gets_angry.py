from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

black = [0, 0, 0]
white = [255, 255, 255]
purple = [128, 0, 128]

def boss_gets_angry(x, y):
    sense.set_pixel(y, x, black)
    sleep(0.3)
    sense.set_pixel(y, x, white)
    sleep(0.3)
    sense.set_pixel(y, x, black)
    sleep(0.3)
    sense.set_pixel(y, x, white)
    sleep(0.3)
    sense.set_pixel(y, x, black)
    sleep(0.3)
    sense.set_pixel(y, x, purple)