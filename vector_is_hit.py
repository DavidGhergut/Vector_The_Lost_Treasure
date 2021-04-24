from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

black = [0, 0, 0]
white = [255, 255, 255]
pink = [255, 113, 181]

def vector_is_hit(x, y):
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
    sense.set_pixel(y, x, pink)

