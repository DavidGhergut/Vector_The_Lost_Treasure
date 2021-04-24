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
#Aceasta functie va afisa imaginea de sfarsit a tuturor nivelelor (This function will print the ending image for all the levels)

def afisare_imagine_de_sfarsit_de_nivel_1():
    imagine_de_sfarsit_bucata_1 = [
        black, black, black, black, black, black, black, black,
	black, black, black, black, black, black, black, black,
        black, black, blue, cyan, blue, cyan, black, black,
	black, black, cyan, red, gold, blue, black, black,
        black, black, blue, gold, red, cyan, black, black,
	black, black, cyan, blue, cyan, blue, black, black,
	black, black, black, black, black, black, black, black,
	black, black, black, black, black, black, black, black,
    ]
    angles = [0, 90, 180, 270, 0, 90, 180, 270, 0]
    sense.set_pixels(imagine_de_sfarsit_bucata_1)
    for rotation in angles:
        sense.set_rotation(rotation)
        sleep(0.5)
    sense.clear()
