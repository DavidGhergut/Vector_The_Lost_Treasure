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

def storyline_level_2():
    field1 = [
        gold, gold, cyan, white, white, cyan, cyan, cyan,
        gold, cyan, cyan, cyan, cyan, cyan, white, white,
        cyan, white, white, cyan, cyan, cyan, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field2 = [
        gold, gold, cyan, cyan, white, white, cyan, cyan,
        gold, cyan, cyan, cyan, cyan, white, white, cyan,
        cyan, cyan, white, white, cyan, cyan, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field3 = [
        gold, gold, cyan, cyan, cyan, white, white, cyan,
        gold, cyan, cyan, cyan, white, white, cyan, cyan,
        cyan, cyan, cyan, white, white, cyan, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field4 = [
        gold, gold, cyan, cyan, cyan, cyan, white, white,
        gold, cyan, cyan, white, white, cyan, cyan, cyan,
        cyan, cyan, cyan, cyan, white, white, cyan, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    field5 = [
        gold, gold, cyan, cyan, cyan, cyan, cyan, white,
        gold, cyan, white, white, cyan, cyan, cyan, cyan,
        cyan, cyan, cyan, cyan, cyan, white, white, cyan,
        green, green, green, green, green, green, green, green,
        green, green, green, green, blue, green, green, green,
        green, red, green, green, darkgreen, green, purple, green,
        green, darkgreen, green, green, green, green, darkgreen, green,
        green, green, green, green, green, green, green, green,
    ]
    #AICI SCRIEM STORYLINE-UL PENTRU AL DOILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE SECOND LEVEL)
    print("Pe drum insa, acesta se pierde, numai ca se intalneste cu o randunica care are sa-l ghideze catre castel, cu conditia de a-i da bete pentru cuibul acesteia. Cu bratele stranse, Vector continua drumul.")
    print("\n")
    for i in range(5):
        sense.set_pixels(field1)
        sleep(0.5)
        sense.set_pixels(field2)
        sleep(0.5)
        sense.set_pixels(field3)
        sleep(0.5)
        sense.set_pixels(field4)
        sleep(0.5)
        sense.set_pixels(field5)
        sleep(0.5)
    sense.clear()