from sense_hat import sense_hat
from Controls_Level_3 import Controls_Level_3
from pathlib import Path
from datetime import datetime, timedelta
from pygame import mixer, mixer_music

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

#VARIABILE GLOBALE (GLOBAL VARIABLES)
sense = SenseHat()
dir_path = Path(__file__).parent.resolve()

def Level3():
    Controls_Level_3()
    image_level3 = [
        cyan, cyan, dimgrey, dimgrey, purple, red, purple, cyan,
        dimgrey, dimgrey, cyan, cyan, cyan, cyan, purple, dimgrey,
        dimgrey, cyan, cyan, cyan, cyan, cyan, cyan, dimgrey,
        purple, cyan, cyan, cyan, dimgrey, dimgrey, dimgrey, cyan,
        pink, cyan, dimgrey, cyan, purple, cyan, cyan, cyan,
        cyan, cyan, purple, dimgrey, cyan, cyan, cyan, dimgrey,
        dimgrey, cyan, dimgrey, cyan, dimgrey, purple, cyan, cyan,
        cyan, dimgrey, cyan, cyan, cyan, dimgrey, dimgrey, cyan
    ]
    sense.set_pixels(image_level3)
    vector_y = 0
    vector_x = 4
    has_flag = False
    ok_theme_song = False
    while has_flag == False:
        """
        if ok_theme_song == False:
            ok_theme_song = True
            initial_date_theme_song = datetime.now()
            #IMPORTANT DATA TO COMPLETE FOR RUNNING THE THEME SONG
            final_date_theme_song = initial_date_theme_song + timedelta(seconds = )
            path1 = dir_path/''
            mixer.music.load(str(path1))
            mixer.music.set_volume(1)
            mixer.music.play()
        elif datetime.now() >= final_date:
            ok_theme_song = False
        """


