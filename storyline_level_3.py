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

def storyline_level_3():
    castle1 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        dimgrey, black, dimgrey, black, black, dimgrey, black, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, brown, brown, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, brown, brown, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, brown, brown, dimgrey, dimgrey, dimgrey,
    ]
    castle2 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        dimgrey, black, dimgrey, black, black, dimgrey, black, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, brown, brown, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, brown, brown, dimgrey, dimgrey, dimgrey,
    ]
    castle3 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        dimgrey, black, dimgrey, black, black, dimgrey, black, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, brown, brown, dimgrey, dimgrey, dimgrey,
    ]
    castle4 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        dimgrey, black, dimgrey, black, black, dimgrey, black, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
    ]
    castle5 = [
        black, red, black, black, black, black, red, black,
        red, red, red, black, black, red, red, red,
        dimgrey, black, dimgrey, black, black, dimgrey, black, dimgrey,
        dimgrey, red, dimgrey, dimgrey, dimgrey, dimgrey, red, dimgrey,
        red, red, red, dimgrey, dimgrey, red, red, red,
        dimgrey, red, dimgrey, black, black, dimgrey, red, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, dimgrey, dimgrey,
    ]
    #AICI SCRIEM STORYLINE-UL PENTRU AL TREILEA NIVEL (HERE WE WRITE THE STORYLINE FOR THE THIRD LEVEL)
    print("Odata ajuns la castel este intampinat de mecanisme bizare care tin usa inchisa. Fiind si seara, Vector isi pune popasul in niste tufisuri de langa usa si se culca cu speranta unor idei noi intr-o noua zi.")
    print("Dimineata este trezit de pasii apasatori ai lui Medios. Acesta se apropia d ecastel iesind mai devreme sa captureze tribute si sacrificii de la satele din apropiere. Vector isi scoate capul din tufis si se uita mai atent in speranta ca o sa afle codul usii.")
    print("Medios incepe sa paseasca pe cuburile antice aprinzandu-le intr-un verde deschis. Vector observa cum demonul se duce pe o anumita cale ca sa deschida usam, insa, inainte sa poata afla secretul, simte cum Medios isi intoarce capul spre el.")
    print("Vector se aseaza repede inapoi in tufis neapucand sa gaseasca tot codul. Zile trec poate chiar saptamani, dar cu fiecare traseu luat de Medios in afara castelului, Vector se apropia din ce in ce mai mult de cod, cand intr-o zi, cu toate cunostintele adunate de-a lungul saptamanilor, intra in castel.")
    print("\n")
    for i in range(5):
        sense.set_pixels(castle1)
        sleep(0.5)
        sense.set_pixels(castle2)
        sleep(0.5)
        sense.set_pixels(castle3)
        sleep(0.5)
        sense.set_pixels(castle4)
        sleep(0.5)
        sense.set_pixels(castle5)
        sleep(0.5)
    sense.clear()