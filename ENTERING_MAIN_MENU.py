from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
#CULORI pentru SenseHat (COLOURS for the SenseHat):
black = [0, 0, 0]
cyan = [0, 255, 255]
blue = [0, 0, 255]
darker_blue = [0, 102, 204]
red = [248, 0, 0]
gold = [248, 212, 0]
green = [0, 255, 0]
white = [255, 255, 255]
purple = [128, 0, 128]
orange = [255, 140, 0]
brown = [136, 68, 16]
coral = [255, 160, 122]
toxicgreen = [97, 222, 42]
darkgreen = [0, 100, 0]
pink = [255, 113, 181]
yellow = [255, 255, 0]
darkbrown = [101, 67, 33]
magenta = [255, 0, 255]
brown2 = [210, 105, 30]
water = [24, 160, 232]
dimgrey = [104, 104, 104]
#FUNCTIE DE INTRARE IN MAIN MENU (ENTERING MAIN MENU FUNCTION)

entering_image_1 = [
    black, black, black, brown, brown, black, black, black,
    black, black, black, black, black, black, black, black,
    dimgrey, dimgrey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

entering_image_2 = [
    black, black, black, brown, brown, black, black, black,
    black, black, brown, blue, blue, brown, black, black,
    dimgrey, dimgrey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

entering_image_3 = [
    black, black, black, brown, brown, black, black, black,
    black, black, black, black, black, black, black, black,
    dimgrey, dimgrey, black, blue, blue, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

reset = [
    black, black, black, brown, brown, black, black, black,
    black, black, black, black, black, black, black, black,
    dimgrey, dimgrey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

def ENTERING_MAIN_MENU():
    sense.set_pixels(entering_image_1)
    sleep(0.65)
    sense.set_pixels(entering_image_2)
    sleep(0.65)
    sense.set_pixels(entering_image_3)
