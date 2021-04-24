from sense_hat import SenseHat
from colr import color
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
#Aceasta functie va afisa a doua imagine de sfarsit a tuturor nivelelor (This function will print the second ending image for all the levels)

imagine_de_sfarsit_bucata_2_etapa_1 = [
    black, black, black, black, black, black, black, black,
    black, blue, blue, black, black, green, green, black,
    black, black, blue, blue, green, green, black, black,
    black, black, black, blue, green, black, black, black,
    black, black, black, red, gold, black, black, black,
    black, black, red, red, gold, gold, black, black,
    black, red, red, black, black, gold, gold, black,
    black, black, black, black, black, black, black, black,
]
imagine_de_sfarsit_bucata_2_etapa_2 = [
    black, black, black, black, black, black, black, black,
    black, blue, blue, black, black, green, green, black,
    black, black, blue, blue, green, green, black, black,
    black, black, black, white, white, black, black, black,
    black, black, black, white, white, black, black, black,
    black, black, red, red, gold, gold, black, black,
    black, red, red, black, black, gold, gold, black,
    black, black, black, black, black, black, black, black,
]
imagine_de_sfarsit_bucata_2_etapa_3 = [
    black, black, black, black, black, black, black, black,
    black, blue, blue, black, black, green, green, black,
    black, black, blue, white, white, green, black, black,
    black, black, white, white, white, white, black, black,
    black, black, white, white, white, white, black, black,
    black, black, red, white, white, gold, black, black,
    black, red, red, black, black, gold, gold, black,
    black, black, black, black, black, black, black, black,
]
imagine_de_sfarsit_bucata_2_etapa_4 = [
    blue, blue, black, black, black, black, green, green,
    black, blue, blue, white, white, green, green, black,
    black, white, white, white, white, white, white, black,
    black, white, white, white, white, white, white, black,
    black, white, white, white, white, white, white, black,
    black, white, white, white, white, white, white, black,
    black, red, red, white, white, gold, gold, black,
    red, red, black, black, black, black, gold, gold,
]
imagine_de_sfarsit_bucata_2_etapa_5 = [
    blue, blue, white, white, white, white, green, green,
    blue, white, white, white, white, white, white, green,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    red, white, white, white, white, white, white, gold,
    red, red, white, white, white, white, gold, gold,
]
imagine_de_sfarsit_bucata_2_etapa_6 = [
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
    white, white, white, white, white, white, white, white,
]
def afisare_imagine_de_sfarsit_de_nivel_2():
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_1)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_2)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_3)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_4)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_5)
    sleep(0.5)
    sense.set_pixels(imagine_de_sfarsit_bucata_2_etapa_6)
    sleep(0.5)
    sense.clear()
