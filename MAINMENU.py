"""
--> Spymania 2D SenseHat Game <--
Contribuitori:
David Ghergut
Mihai Pangratie
"""

#Aici importam toate modulele de python de care avem nevoie in tot programul (Here we import all the python modules that we need in the whole program)
from sense_hat import SenseHat
from time import sleep
import collections
from pygame import mixer, mixer_music
from colr import color
from animation_lose_level_1 import animation_lose_level_1
from animation_win_level_1 import animation_win_level_1
from locked import locked
from unlocked import unlocked
from ENTERING_MAIN_MENU import ENTERING_MAIN_MENU
from datetime import datetime, timedelta
from afisare_imagine_de_sfarsit_de_nivel_1 import afisare_imagine_de_sfarsit_de_nivel_1
from afisare_imagine_de_sfarsit_de_nivel_2 import afisare_imagine_de_sfarsit_de_nivel_2
from Controls import Controls
from Controls_Level_1 import Controls_Level_1
from Controls_Level_3 import Controls_Level_3
from Controls_Level_4 import Controls_Level_4
from storyline_level_1 import storyline_level_1
from storyline_level_2 import storyline_level_2
from storyline_level_3 import storyline_level_3
from storyline_level_4_and_5 import storyline_level_4_and_5
from pathlib import Path 
from Level5 import Level5

#VARIABILE GLOBALE (GLOBAL VARIABLES):
sense = SenseHat()
is_playable = [1, 0, 1, 1, 1]

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

#FUNCTIE DE MAIN MENU (MAIN MENU FUNCTION):

entering_image_1 = [
    black, black, black, brown, brown, black, black, black,
    black, black, black, black, black, black, black, black,
    dimgrey, dimgrey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

entering_image_2 = [
    black, black, black, brown, brown, black, black, black,
    black, black, brown, blue, blue, brown, black, black,
    dimgrey, dimgrey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

reset = [
    black, black, black, brown, brown, black, black, black,
    black, black, black, black, black, black, black, black,
    dimgrey, dimgrey, black, black, black, black, purple, purple,
    black, black, black, black, black, black, black, black,
    gold, orange, black, black, black, black, darkbrown, orange,
    black, black, black, black, black, black, black, black,
    red, red, black, black, black, black, cyan, cyan,
    black, black, black, coral, coral, black, black, black,
]

dir_path = Path(__file__).parent.resolve()
def MAIN_MENU():
    sense.show_message("Welcome", text_colour = blue, scroll_speed = 0.05)
    sense.show_message("to", text_colour = gold, scroll_speed = 0.05)
    sense.show_message("Vector.", text_colour = green, scroll_speed = 0.05)
    sense.show_message("The Lost Treasure!", text_colour = purple, scroll_speed = 0.05)
    sleep(0.5)
    sense.show_message("Press joystick to continue!", text_colour = darker_blue, scroll_speed = 0.05)
    event1 = sense.stick.wait_for_event(emptybuffer = True)
    #ZONA DE SELECTARE A NIVELULUI DE JOC (THE LEVEL SELECTION ZONE)
    if event1.action == "pressed":
        sense.show_message("Choose the level you want to play!", text_colour = coral, scroll_speed = 0.05)
        ok1 = False
        pixel1_x = 2
        pixel1_y = 3
        pixel2_x = 2
        pixel2_y = 4
        ENTERING_MAIN_MENU()
        print("\n\n")
        print(color("Go to the coral section for instructions!", fore=coral))
        print("\n\n")
        #INITIALIZAM FISIERUL MP3 PENTRU A FI RULAT
        mixer.init()
        ok3 = False
        while ok1 == False:
            if ok3 == False:
                ok3 = True
                initial_date = datetime.now()
                final_date = initial_date + timedelta(seconds=28)
                path = dir_path/'b.mp3'
                mixer.music.load(str(path))
                mixer.music.set_volume(1)
                mixer.music.play()
            elif datetime.now() >= final_date:
                ok3 = False
            event2 = sense.stick.wait_for_event(emptybuffer = True)
            if event2.action == "pressed" and event2.direction == "middle":
                if pixel1_y == 3 and pixel1_x == 0 and pixel2_y == 4 and pixel2_x == 0:
                    mixer.music.stop()
                    sense.show_message("exit? -> up!", text_colour = red, scroll_speed = 0.04)
                    sense.show_message("resume? -> down!", text_colour = green, scroll_speed = 0.04)
                    event3 = sense.stick.wait_for_event(emptybuffer = True)
                    if event3.action == "pressed" and event3.direction == "up":
                        ok1 = True
                        sense.show_message("Thank", text_colour = blue, scroll_speed = 0.05)
                        sense.show_message("you", text_colour = gold, scroll_speed = 0.05)
                        sense.show_message("for", text_colour = red, scroll_speed = 0.05)
                        sense.show_message("playing", text_colour = purple, scroll_speed = 0.05)
                        sense.show_message("Vector.", text_colour = green, scroll_speed = 0.05)
                        sense.show_message("The Lost Treasure!", text_colour = gold, scroll_speed = 0.05)
                        return
                    elif event3.action == "pressed" and event3.direction == "down":
                        sense.show_message("Choose the level you want to play!", text_colour = coral, scroll_speed = 0.05)
                        ENTERING_MAIN_MENU()
                        ok3 = False
                        pixel1_x = 2
                        pixel1_y = 3
                        pixel2_x = 2
                        pixel2_y = 4
                        event2 = sense.stick.wait_for_event(emptybuffer = True)
                elif pixel1_y == 6 and pixel1_x == 2 and pixel2_y == 7 and pixel2_x == 2:
                    mixer.music.stop()
                    Storyline()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                    ok3 = False
                elif pixel1_y == 6 and pixel1_x == 4 and pixel2_y == 7 and pixel2_x == 4:
                    mixer.music.stop()
                    if is_playable[0] == 1:
                        Level1()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                    ok3 = False
                elif pixel1_y == 6 and pixel1_x == 6 and pixel2_y == 7 and pixel2_x == 6:
                    mixer.music.stop()
                    if is_playable[1] == 1:
                        #Level2()
                        unlocked()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                    ok3 = False
                elif pixel1_y == 0 and pixel1_x == 2 and pixel2_y == 1 and pixel2_x == 2:
                    mixer.music.stop()
                    if is_playable[2] == 1:
                        Level3()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                    ok3 = False
                elif pixel1_y == 0 and pixel1_x == 4 and pixel2_y == 1 and pixel2_x == 4:
                    mixer.music.stop()
                    if is_playable[3] == 1:
                        Level4()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                    ok3 = False
                elif pixel1_y == 0 and pixel1_x == 6 and pixel2_y == 1 and pixel2_x == 6:
                    mixer.music.stop()
                    if is_playable[4] == 1:
                        Level5()
                    else:
                        locked()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
                    ok3 = False
                elif pixel1_y == 3 and pixel1_x == 7 and pixel2_y == 4 and pixel2_x == 7:
                    Controls()
                    pixel1_x = 2
                    pixel1_y = 3
                    pixel2_x = 2
                    pixel2_y = 4
            if event2.action == "pressed" and event2.direction != "middle":
                pixels = sense.get_pixels()
                if pixel1_y == 3 and pixel1_x == 1 and pixel2_y == 4 and pixel2_x == 1:
                    sense.set_pixels(entering_image_2)
                else:
                    sense.set_pixels(reset)
                sense.set_pixel(pixel1_y, pixel1_x, black)
                sense.set_pixel(pixel2_y, pixel2_x, black)
                if pixels[3] == black:
                    sense.set_pixel(3, 0, brown)
                if pixels[4] == black:
                    sense.set_pixel(4, 0, brown)
                if pixels[16] == black:
                    sense.set_pixel(0, 2, dimgrey)
                if pixels[17] == black:
                    sense.set_pixel(1, 2, dimgrey)
                if pixels[22] == black:
                    sense.set_pixel(6, 2, purple)
                if pixels[23] == black:
                    sense.set_pixel(7, 2, purple)
                if pixels[32] == black:
                    sense.set_pixel(0, 4, gold)
                if pixels[33] == black:
                    sense.set_pixel(1, 4, orange)
                if pixels[38] == black:
                    sense.set_pixel(6, 4, darkbrown)
                if pixels[39] == black:
                    sense.set_pixel(7, 4, orange)
                if pixels[48] == black:
                    sense.set_pixel(0, 6, red)
                if pixels[49] == black:
                    sense.set_pixel(1, 6, red)
                if pixels[54] == black:
                    sense.set_pixel(6, 6, cyan)
                if pixels[55] == black:
                    sense.set_pixel(7, 6, cyan)
                if pixels[59] == black:
                    sense.set_pixel(3, 7, coral)
                if pixels[60] == black:
                    sense.set_pixel(4, 7, coral)
                if event2.direction == "up" and pixel1_x > 0 and pixel2_x > 0:
                    pixel1_x = pixel1_x - 1
                    pixel2_x = pixel2_x - 1
                elif event2.direction == "down" and pixel1_x < 7 and pixel2_x < 7:
                    pixel1_x = pixel1_x + 1
                    pixel2_x = pixel2_x + 1
                elif event2.direction == "left" and pixel1_y > 0 and pixel2_y > 0:
                    pixel1_y = pixel1_y - 1
                    pixel2_y = pixel2_y - 1
                elif event2.direction == "right" and pixel1_y < 7 and pixel2_y < 7:
                    pixel1_y = pixel1_y + 1
                    pixel2_y = pixel2_y + 1
                sense.set_pixel(pixel1_y, pixel1_x, blue)
                sense.set_pixel(pixel2_y, pixel2_x, blue)

    #La finalul programului, dezactivam toate led-urile aprinse de pe SenseHat (At the end of the program, we clear the SenseHat)
    sense.clear()


def Storyline():
    path1 = dir_path/'Povesti_Din_Folclorul_Maghiar.mp3'
    mixer.music.load(str(path1))
    mixer.music.set_volume(1)
    mixer.music.play() 
    storyline_level_1()
    storyline_level_2()
    storyline_level_3()
    storyline_level_4_and_5()
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    is_playable[0] = 1
    ENTERING_MAIN_MENU()


#FUNCTIE PENTRU NIVELUL 1 (LEVEL 1 FUNCTION)
def Level1():
    Controls_Level_1()
    image_level1 = [
        black, black, black, black, dimgrey, black, red, purple,
        black, pink, gold, black, dimgrey, black, red, red,
        black, black, black, black, dimgrey, black, black, black,
        dimgrey, dimgrey, dimgrey, black, black, dimgrey, water, water,
        black, gold, water, black, black, black, black, black,
        black, black, water, black, black, water, water, water,
        black, gold, water, black, black, water, brown, black,
        dimgrey, black, water, black, black, water, black, black,
    ]
    sense.set_pixels(image_level1)
    vector_y = 1
    vector_x = 1
    has_wooden_bucket_fire = False
    has_wooden_bucket_water = 0
    has_wooden_bucket = False
    has_flag = False
    ok4 = False
    while has_flag == False:
        if ok4 == False:
            ok4 = True
            initial_date = datetime.now()
            final_date = initial_date + timedelta(seconds=51)
            path1 = dir_path/'a.mp3'
            mixer.music.load(str(path1))
            mixer.music.set_volume(1)
            mixer.music.play()
        elif datetime.now() >= final_date:
            ok4 = False
        pixels1 = sense.get_pixels()
        event4 = sense.stick.wait_for_event(emptybuffer = True)
        if event4.action == "pressed" and event4.direction == "up" and vector_x > 0 and pixels1[8 * (vector_x - 1) + vector_y] != dimgrey:
            if pixels1[8 * (vector_x - 1) + vector_y] == gold and vector_x - 2 >= 0 and pixels1[8 * (vector_x - 2) + vector_y] != dimgrey:
                if pixels1[8 * (vector_x - 2) + vector_y] == water:
                    sense.set_pixel(vector_y, vector_x - 2, black)
                    sense.set_pixel(vector_y, vector_x - 1, black)
                elif pixels1[8 * (vector_x - 2) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x - 1, black)
                elif pixels1[8 * (vector_x - 2) + vector_y] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y, vector_x - 1, black)
                    sense.set_pixel(vector_y, vector_x - 2, gold)
            elif pixels1[8 * (vector_x - 1) + vector_y] == gold and (vector_x - 2 < 0 or pixels1[8 * (vector_x - 2) + vector_y] == dimgrey):
                continue
            elif pixels1[8 * (vector_x - 1) + vector_y] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y, vector_x - 1, black)
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x - 1) + vector_y] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x - 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * (vector_x - 1) + vector_y] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True:
                    sense.set_pixel(vector_y, vector_x - 1, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x - 1) + vector_y] == purple:
                mixer.music.stop()
                path2 = dir_path/'c.mp3'
                mixer.music.load(str(path2))
                mixer.music.set_volume(1)
                mixer.music.play()
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x - 1
                sense.set_pixel(vector_y, vector_x, pink)
        elif event4.action == "pressed" and event4.direction == "down" and vector_x < 7 and pixels1[8 * (vector_x + 1) + vector_y] != dimgrey:
            if pixels1[8 * (vector_x + 1) + vector_y] == gold and vector_x + 2 <= 7 and pixels1[8 * (vector_x + 2) + vector_y] != dimgrey:
                if pixels1[8 * (vector_x + 2) + vector_y] == water:
                    sense.set_pixel(vector_y, vector_x + 2, black)
                    sense.set_pixel(vector_y, vector_x + 1, black)
                elif pixels1[8 * (vector_x + 2) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x + 1, black)
                elif pixels1[8 * (vector_x + 2) + vector_y] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y, vector_x + 1, black)
                    sense.set_pixel(vector_y, vector_x + 2, gold)
            elif pixels1[8 * (vector_x + 1) + vector_y] == gold and (vector_x + 2 > 7 or pixels1[8 * (vector_x + 2) + vector_y] == dimgrey):
                continue
            elif pixels1[8 * (vector_x + 1) + vector_y] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y, vector_x + 1, black)
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x + 1) + vector_y] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x + 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * (vector_x + 1) + vector_y] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True:
                    sense.set_pixel(vector_y, vector_x + 1, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * (vector_x + 1) + vector_y] == purple:
                mixer.music.stop()
                path2 = dir_path/'c.mp3'
                mixer.music.load(str(path2))
                mixer.music.set_volume(1)
                mixer.music.play()
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_x = vector_x + 1
                sense.set_pixel(vector_y, vector_x, pink)
        elif event4.action == "pressed" and event4.direction == "left" and vector_y > 0 and pixels1[8 * vector_x + vector_y - 1] != dimgrey:
            if pixels1[8 * vector_x + vector_y - 1] == gold and vector_y - 2 >= 0 and pixels1[8 * vector_x + vector_y - 2] != dimgrey:
                if pixels1[8 * vector_x + vector_y - 2] == water:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                    sense.set_pixel(vector_y - 2, vector_x, black)
                elif pixels1[8 * vector_x + vector_y - 2] == red:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                elif pixels1[8 * vector_x + vector_y - 2] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                    sense.set_pixel(vector_y - 2, vector_x, gold)
            elif pixels1[8 * vector_x + vector_y - 1] == gold and (vector_y - 2 < 0 or pixels1[8 * vector_x + vector_y - 2] == dimgrey):
                continue
            elif pixels1[8 * vector_x + vector_y - 1] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y - 1, vector_x, black)
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y - 1] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y - 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * vector_x + vector_y - 1] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True:
                    sense.set_pixel(vector_y - 1, vector_x, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y - 1] == purple:
                mixer.music.stop()
                path2 = dir_path/'c.mp3'
                mixer.music.load(str(path2))
                mixer.music.set_volume(1)
                mixer.music.play()
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y - 1
                sense.set_pixel(vector_y, vector_x, pink)
        elif event4.action == "pressed" and event4.direction == "right" and vector_y + 1 < 7 and pixels1[8 * vector_x + vector_y + 1] != dimgrey:
            if pixels1[8 * vector_x + vector_y + 1] == gold and vector_y + 2 <= 7 and pixels1[8 * vector_x + vector_y + 2] != dimgrey:
                if pixels1[8 * vector_x + vector_y + 2] == water:
                    sense.set_pixel(vector_y + 1, vector_x, black)
                    sense.set_pixel(vector_y + 2, vector_x, black)
                elif pixels1[8 * vector_x + vector_y + 2] == red: 
                    sense.set_pixel(vector_y + 1, vector_x, black)
                elif pixels1[8 * vector_x + vector_y + 2] == gold:
                    continue
                else:
                    sense.set_pixel(vector_y + 1, vector_x, black)
                    sense.set_pixel(vector_y + 2, vector_x, gold)
            elif pixels1[8 * vector_x + vector_y + 1] == gold and (vector_x + 2 > 7 or pixels1[8 * vector_x + vector_y + 2] == dimgrey):
                continue
            elif pixels1[8 * vector_x + vector_y + 1] == water:
                if has_wooden_bucket_water == 0 and has_wooden_bucket == True:
                    has_wooden_bucket_water = 1
                    sense.set_pixel(vector_y + 1, vector_x, black)
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y + 1] == brown:
                has_wooden_bucket = True
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y + 1
                sense.set_pixel(vector_y, vector_x, pink)
            elif pixels1[8 * vector_x + vector_y + 1] == red:
                if has_wooden_bucket_water == 1 and has_wooden_bucket == True:
                    sense.set_pixel(vector_y + 1, vector_x, black)
                    has_wooden_bucket_fire = True
                    has_wooden_bucket_water = 0
                else:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif pixels1[8 * vector_x + vector_y + 1] == purple:
                mixer.music.stop()
                path2 = dir_path/'c.mp3'
                mixer.music.load(str(path2))
                mixer.music.set_volume(1)
                mixer.music.play()
                animation_win_level_1()
                sleep(2)
                has_flag = True
            else:
                sense.set_pixel(vector_y, vector_x, black)
                vector_y = vector_y + 1
                sense.set_pixel(vector_y, vector_x, pink)
    if has_wooden_bucket_fire == True:
        is_playable[1] = 1
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    ENTERING_MAIN_MENU()
#Aici apelam toate functiile pe care le-am creat astfel incat jocul sa poata rula (Here we call all the functions we need in order for the game to load)

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
    original_pixels = sense.get_pixels()
    vector_y = 0
    vector_x = 4
    has_flag = False
    out_of_board = False
    ok_theme_song = False
    moves_made = 0
    print(color("\nWow! You made it to the castle! Well, you have a maximum of 15 movements and you need to take the red key to Medios's hallway. Make careful steps if you want to stay alive. Don't fall off the map and don't touch the lasers! Good luck!\n", fore=green))
    while has_flag == False and moves_made <= 15:
        if ok_theme_song == False:
            ok_theme_song = True
            initial_date_theme_song = datetime.now()
            final_date_theme_song = initial_date_theme_song + timedelta(seconds = 32)
            path1 = dir_path/'melodie_level3.mp3'
            mixer.music.load(str(path1))
            mixer.music.set_volume(1)
            mixer.music.play()
        elif datetime.now() >= final_date_theme_song:
            ok_theme_song = False
        pixels = sense.get_pixels()
        event = sense.stick.wait_for_event(emptybuffer=True)
        if event.action == "pressed" and event.direction != "middle":
            moves_made += 1
            if event.direction == "up":
                if vector_x == 0:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    out_of_board = True
                elif pixels[8 * (vector_x - 1) + vector_y] == cyan:
                    while pixels[8 * (vector_x - 1) + vector_y] == cyan:
                        if original_pixels[8 * vector_x + vector_y] == dimgrey or (vector_y == 0 and vector_x == 4):
                            sense.set_pixel(vector_y, vector_x, dimgrey)
                        else:
                            sense.set_pixel(vector_y, vector_x, cyan)
                        vector_x -= 1
                        sense.set_pixel(vector_y, vector_x, pink)
                        sleep(0.5)
                        if vector_x - 1 < 0:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            out_of_board = True
                            break
                    if out_of_board == False:
                        if pixels[8 * (vector_x - 1) + vector_y] == purple:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_x -= 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            out_of_board = True
                        elif pixels[8 * (vector_x - 1) + vector_y] == dimgrey:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_x -= 1
                            sense.set_pixel(vector_y, vector_x, pink)
                        elif pixels[8 * (vector_x - 1) + vector_y] == red:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_x -= 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            mixer.music.stop()
                            path2 = dir_path/'c.mp3'
                            mixer.music.load(str(path2))
                            mixer.music.set_volume(1)
                            mixer.music.play()
                            animation_win_level_1()
                            has_flag = True
                elif pixels[8 * (vector_x - 1) + vector_y] == purple:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    out_of_board = True
                elif pixels[8 * (vector_x - 1) + vector_y] == dimgrey:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                elif pixels[8 * (vector_x - 1) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_win_level_1()
                    has_flag = True
                if out_of_board == True:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif event.direction == "right":
                if vector_y == 7:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    out_of_board = True
                elif pixels[8 * vector_x + vector_y + 1] == cyan:
                    while pixels[8 * vector_x + vector_y + 1] == cyan:
                        if original_pixels[8 * vector_x + vector_y] == dimgrey or (vector_y == 0 and vector_x == 4):
                            sense.set_pixel(vector_y, vector_x, dimgrey)
                        else:
                            sense.set_pixel(vector_y, vector_x, cyan)
                        vector_y += 1
                        sense.set_pixel(vector_y, vector_x, pink)
                        sleep(0.5)
                        if vector_y + 1 > 7:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            out_of_board = True
                            break
                    if out_of_board == False:
                        if pixels[8 * vector_x + vector_y + 1] == purple:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_y += 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            out_of_board = True
                        elif pixels[8 * vector_x + vector_y + 1] == dimgrey:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_y += 1
                            sense.set_pixel(vector_y, vector_x, pink)
                        elif pixels[8 * vector_x + vector_y + 1] == red:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_y += 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            mixer.music.stop()
                            path2 = dir_path/'c.mp3'
                            mixer.music.load(str(path2))
                            mixer.music.set_volume(1)
                            mixer.music.play()
                            animation_win_level_1()
                            has_flag = True
                elif pixels[8 * vector_x + vector_y + 1] == purple:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    out_of_board = True
                elif pixels[8 * vector_x + vector_y + 1] == dimgrey:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                elif pixels[8 * vector_x + vector_y + 1] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_win_level_1()
                    has_flag = True
                if out_of_board == True:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif event.direction == "left":
                if vector_y == 0:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    out_of_board = True
                elif pixels[8 * vector_x + vector_y - 1] == cyan:
                    while pixels[8 * vector_x + vector_y - 1] == cyan:
                        if original_pixels[8 * vector_x + vector_y] == dimgrey or (vector_y == 0 and vector_x == 4):
                            sense.set_pixel(vector_y, vector_x, dimgrey)
                        else:
                            sense.set_pixel(vector_y, vector_x, cyan)
                        vector_y -= 1
                        sense.set_pixel(vector_y, vector_x, pink)
                        sleep(0.5)
                        if vector_y - 1 < 0:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            out_of_board = True
                            break
                    if out_of_board == False:
                        if pixels[8 * vector_x + vector_y - 1] == purple:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_y -= 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            out_of_board = True
                        elif pixels[8 * vector_x + vector_y - 1] == dimgrey:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_y -= 1
                            sense.set_pixel(vector_y, vector_x, pink)
                        elif pixels[8 * vector_x + vector_y - 1] == red:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_y -= 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            mixer.music.stop()
                            path2 = dir_path/'c.mp3'
                            mixer.music.load(str(path2))
                            mixer.music.set_volume(1)
                            mixer.music.play()
                            animation_win_level_1()
                            has_flag = True
                elif pixels[8 * vector_x + vector_y - 1] == purple:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    out_of_board = True
                elif pixels[8 * vector_x + vector_y - 1] == dimgrey:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                elif pixels[8 * vector_x + vector_y - 1] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_win_level_1()
                    has_flag = True
                if out_of_board == True:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
            elif event.direction == "down":
                if vector_x == 7:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    out_of_board = True
                elif pixels[8 * (vector_x + 1) + vector_y] == cyan:
                    while pixels[8 * (vector_x + 1) + vector_y] == cyan:
                        if original_pixels[8 * vector_x + vector_y] == dimgrey or (vector_y == 0 and vector_x == 4):
                            sense.set_pixel(vector_y, vector_x, dimgrey)
                        else:
                            sense.set_pixel(vector_y, vector_x, cyan)
                        vector_x += 1
                        sense.set_pixel(vector_y, vector_x, pink)
                        sleep(0.5)
                        if vector_x + 1 > 7:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            out_of_board = True
                            break
                    if out_of_board == False:
                        if pixels[8 * (vector_x + 1) + vector_y] == purple:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_x += 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            out_of_board = True
                        elif pixels[8 * (vector_x + 1) + vector_y] == dimgrey:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_x += 1
                            sense.set_pixel(vector_y, vector_x, pink)
                        elif pixels[8 * (vector_x + 1) + vector_y] == red:
                            sense.set_pixel(vector_y, vector_x, cyan)
                            vector_x += 1
                            sense.set_pixel(vector_y, vector_x, pink)
                            mixer.music.stop()
                            path2 = dir_path/'c.mp3'
                            mixer.music.load(str(path2))
                            mixer.music.set_volume(1)
                            mixer.music.play()
                            animation_win_level_1()
                            has_flag = True
                elif pixels[8 * (vector_x + 1) + vector_y] == purple:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    out_of_board = True
                elif pixels[8 * (vector_x + 1) + vector_y] == dimgrey:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                elif pixels[8 * (vector_x + 1) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_win_level_1()
                    has_flag = True
                if out_of_board == True:
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
    if moves_made > 15:
        mixer.music.stop()
        path2 = dir_path/'d.mp3'
        mixer.music.load(str(path2))
        mixer.music.set_volume(1)
        mixer.music.play()
        animation_lose_level_1()
    if has_flag == True:
        is_playable[2] = 1
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    ENTERING_MAIN_MENU()

def Level4():
    Controls_Level_4()
    intro_level4 = [
        dimgrey, dimgrey, dimgrey, red, dimgrey, dimgrey, dimgrey, red,
        dimgrey, red, dimgrey, dimgrey, red, dimgrey, red, dimgrey,
        dimgrey, dimgrey, dimgrey, red, dimgrey, red, dimgrey, gold,
        dimgrey, red, dimgrey, dimgrey, dimgrey, red, dimgrey, red,
        pink, dimgrey, dimgrey, red, dimgrey, dimgrey, dimgrey, red,
        red, dimgrey, dimgrey, red, dimgrey, red, dimgrey, red,
        dimgrey, dimgrey, red, dimgrey, dimgrey, dimgrey, dimgrey, red,
        dimgrey, red, dimgrey, dimgrey, red, dimgrey, red, dimgrey
    ]
    sense.set_pixels(intro_level4)
    print(color("\nImpressive! You made it to Medios's hallway! It looks like Medios is quite a smart villain and in every room that we need to go through to get to his room he has put several landmines. Watch out for them and try to find a safe way to the doors and get the golden key, in order to fight all mighty Medios.\n", fore=green))
    pixels = sense.get_pixels()
    ok_music = False
    vector_x = 4
    vector_y= 0
    has_golden_key = False
    while has_golden_key == False:
        if ok_music == False:
            ok_music = True
            initial_music_date = datetime.now()
            final_music_date = initial_music_date + timedelta(seconds=21)
            path1 = dir_path/'melodie_level4.mp3'
            mixer.music.load(str(path1))
            mixer.music.set_volume(1)
            mixer.music.play()
        elif datetime.now() >= final_music_date:
            ok_music = False
        event = sense.stick.wait_for_event(emptybuffer=True)
        if event.action == "pressed":
            if event.direction == "up" and vector_x > 0:
                if pixels[8 * (vector_x - 1) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
                elif pixels[8 * (vector_x - 1) + vector_y] == gold:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    has_golden_key = True
                    animation_win_level_1()
                else:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
            elif event.direction == "right" and vector_y < 7:
                if pixels[8 * vector_x + vector_y + 1] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
                elif pixels[8 * vector_x + vector_y + 1] == gold:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    has_golden_key = True
                    animation_win_level_1()
                else:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y += 1
                    sense.set_pixel(vector_y, vector_x, pink)
            elif event.direction == "down" and vector_x < 7:
                if pixels[8 * (vector_x + 1) + vector_y] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
                elif pixels[8 * (vector_x + 1) + vector_y] == gold:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x += 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    has_golden_key = True
                    animation_win_level_1()
                else:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_x += 1
                    sense.set_pixel(vector_y, vector_x, pink)
            elif event.direction == "left" and vector_y > 0:
                if pixels[8 * vector_x + vector_y - 1] == red:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'d.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_lose_level_1()
                    break
                elif pixels[8 * vector_x + vector_y - 1] == gold:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
                    mixer.music.stop()
                    path2 = dir_path/'c.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    has_golden_key = True
                    animation_win_level_1()
                else:
                    sense.set_pixel(vector_y, vector_x, dimgrey)
                    vector_y -= 1
                    sense.set_pixel(vector_y, vector_x, pink)
    if has_golden_key == True:
        is_playable[3] = 1
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    ENTERING_MAIN_MENU()

#Pentru a te putea folosi de SenseHat-ul fizic, comenteaza toate liniile de mai jos (If you want to use the physical SenseHat, comment all the lines below)
import threading

#th = threading.Thread(target=MAIN_MENU)
th = threading.Thread(target=MAIN_MENU)
th.start()
sense.loop()
th.join()