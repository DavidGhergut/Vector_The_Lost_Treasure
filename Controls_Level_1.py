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
#FUNCTIE DE AFISARE A CONTROALELOR PENTRU NIVELUL 1 (FUNCTION FOR CONTROLS AT LEVEL 1)
def Controls_Level_1():
    print("\n")
    print(color("CONTROLS LEVEL 1:", fore=green))
    print(color("Pink -> Vector", fore=pink))
    print(color("Grey -> Wall", fore=dimgrey))
    print(color("Brown -> Wood bucket", fore=brown))
    print(color("Gold -> Sand", fore=gold))
    print(color("Blue -> Water", fore=water))
    print(color("Red -> Fire", fore=red))
    print(color("Purple -> Flag", fore=purple))
    print("\n")
