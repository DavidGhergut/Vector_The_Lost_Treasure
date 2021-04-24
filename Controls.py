from ENTERING_MAIN_MENU import ENTERING_MAIN_MENU
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
#FUNCTIE DE AFISARE A CONTROALELOR (FUNCTION FOR CONTROLS)

def Controls():
    print("\n")
    print(color("CONTROLS MAIN MENU:", fore=green))
    print(color("Blue -> Vector (you)", fore=blue))
    print(color("Brown -> doors that lead to exit", fore=brown))
    print(color("Purple -> Storyline", fore=purple))
    print(color("Darkbrown & Orange -> Level 1", fore=orange, back=darkbrown))
    print(color("Cyan -> Level 2", fore=cyan))
    print(color("Grey -> Level 3", fore=dimgrey))
    print(color("Gold & orange -> Level 4", fore=orange, back=gold))
    print(color("Red -> Level 5 (Boss fight)", fore=red))
    print("\n")
    ENTERING_MAIN_MENU()
