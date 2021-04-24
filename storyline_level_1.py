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

def storyline_level_1():
    fire1 = [
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, black, black, black,
        black, black, black, red, red, black, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire2 = [
        black, black, black, black, black, black, black, black,
        black, black, black, black, red, black, black, black,
        black, black, black, red, red, red, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire3 = [
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, red, black, black,
        black, black, black, black, red, red, red, black,
        black, black, black, red, orange, orange, red, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire4 = [
        black, black, black, black, black, black, red, black,
        black, black, black, black, black, red, red, black,
        black, black, black, black, red, black, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    fire5 = [
        black, black, black, black, black, black, red, black,
        black, black, black, black, black, black, black, black,
        black, black, black, red, red, black, black, black,
        black, black, black, red, orange, red, black, black,
        black, black, red, orange, yellow, orange, red, black,
        black, red, orange, yellow, yellow, orange, red, black,
        black, darkbrown, darkbrown, yellow, yellow, darkbrown, darkbrown, black,
        black, black, darkbrown, darkbrown, darkbrown, darkbrown, black, black,
    ]
    #AICI SCRIEM STORYLINE-UL PENTRU PRIMUL NIVEL (HERE WE WRITE THE STORYLINE FOR THE FIRST LEVEL)
    print("\n")
    print("A fost odata ca niciodata un luptator curajos numit Vector. Acesta a crescut cu frica lordului malefic Medios in satul cel mai apropiat de castelul acestuia fiind martor la sacrificii si tribute date Lordului. \"Totul va avea sa se schimbe\" spune tare eroul confratilor lui. \"Voi infrange acest demon si voi readuce pacea pe aceste meleaguri\". Cu flama ultimului foc de tabara stinsa, eroul nostru porneste pe drumul catre Medios.")
    print("\n")
    for i in range(5):
        sense.set_pixels(fire1)
        sleep(0.5)
        sense.set_pixels(fire2)
        sleep(0.5)
        sense.set_pixels(fire3)
        sleep(0.5)
        sense.set_pixels(fire4)
        sleep(0.5)
        sense.set_pixels(fire5)
        sleep(0.5)
    sense.clear()