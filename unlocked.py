#IMAGINE PENTRU NIVEL ACCESIBIL (IMAGE FOR AN ACCESSIBLE LEVEL)
from sense_hat import SenseHat
from ENTERING_MAIN_MENU import ENTERING_MAIN_MENU
from time import sleep

sense = SenseHat()
def unlocked():
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
    unlock_image = [
        black, black, black, black, black, black, black, black,
        black, black, green, green, green, green, black, black,
        black, green, green, green, green, green, green, black,
        black, green, green, green, green, green, green, black,
        black, green, green, green, green, green, green, black,
        black, green, green, green, green, green, green, black,
        black, black, green, green, green, green, black, black,
        black, black, black, black, black, black, black, black,
    ]
    sense.set_pixels(unlock_image)
    sleep(1)
    ENTERING_MAIN_MENU()
