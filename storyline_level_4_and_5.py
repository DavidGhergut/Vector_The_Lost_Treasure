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

def storyline_level_4_and_5():
    boss1 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, toxicgreen, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, toxicgreen, red, red, red, toxicgreen, black, black,
    ]
    boss2 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, red, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, toxicgreen, red, red, red, red, black, black,
    ]
    boss3 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, red, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, black, red, red, red, red, black, black,
    ]
    boss4 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, toxicgreen, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, black, red, red, red, red, black, black,
    ]
    boss5 = [
        red, black, black, black, black, black, black, red,
        red, red, black, black, black, black, red, red,
        black, red, red, red, red, red, red, black,
        black, red, blue, black, black, blue, red, black,
        red, black, gold, blue, blue, gold, black, red,
        red, toxicgreen, black, black, black, black, toxicgreen, red,
        black, toxicgreen, toxicgreen, toxicgreen, toxicgreen, toxicgreen, red, black,
        black, black, red, red, red, toxicgreen, black, black,
    ]
    #AICI SCRIEM STORYLINE-UL PENTRU AL PATRULEA SI AL CINCILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE FOURTH AND THE FIFTH LEVEL)
    print("Aerul era rece si se simtea permanent urmarit inauntrul castelului. Cu fiecare camera strabatuta, inima-i batea din ce in ce mai tare.")
    print("Insa imensa usa statea la capatul unei podele de gheata. Acesta se uita aent la podea si la micile patratele care au fost dezghetate de urmele lui Medios.")
    print("Nu ii ia mult, pana cand Vector dezluseste drumul pe care trebuie sa-l urmeze pentru a deschide usa.")
    print("Odata cu usa deschisa, tavanul incepe sa se prabuseasca din spatele lui. Fuge turbat prin holul care pare sa nu se mai termine. Reuseste sa ajunga in ultima secunda la captul holului unde se intalneste cu Medios.")
    print("Acesta ii spune \"Ai ajuns pana aici, mi-ai distrus castelul, sper sa ai energia necesara ca sa vezi cum iti distrug poporul.\"")
    print("\"Tirania ta se opreste aici si acum\" urla Vector")
    print("Cu aerul din camera aproape fiert de respiratiile combatantilor, batalia incepe.")
    print("\n")
    print("Oare va reusi Vector sa-si salveze poporul sau il va baga intr-o era plina de tragedii si durere?")
    for i in range(5):
        sense.set_pixels(boss1)
        sleep(0.5)
        sense.set_pixels(boss2)
        sleep(0.5)
        sense.set_pixels(boss3)
        sleep(0.5)
        sense.set_pixels(boss4)
        sleep(0.5)
        sense.set_pixels(boss5)
        sleep(0.5)
    sense.clear()