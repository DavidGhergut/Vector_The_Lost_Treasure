from colr import color

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

#FUNCTIE DE AFISARE A CONTROALELOR PENTRU NIVELUL 3 (FUNCTION FOR CONTROLS AT LEVEL 3)
#ENGLEZA (ENGLISH)
"""
def Controls_Level_3():
    print("\n")
    print(color("CONTROLS LEVEL 3:", fore=green))
    print(color("Pink -> Vector", fore=pink))
    print(color("Red -> Key to the hallway", fore=red))
    print(color("Cyan -> Ice", fore=cyan))
    print(color("Grey -> Floor", fore=dimgrey))
    print(color("Purple -> Lasers", fore=purple))
    print("\n")
"""
#ROMANA (ROMANIAN)
def Controls_Level_3():
    print("\n")
    print(color("CONTROALE NIVEL 3:", fore=green))
    print(color("Roz -> Vector", fore=pink))
    print(color("Rosu -> Cheie catre hol", fore=red))
    print(color("Cyan -> Gheata", fore=cyan))
    print(color("Gri -> Podea", fore=dimgrey))
    print(color("Mov -> Laser", fore=purple))
    print("\n")