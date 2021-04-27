from sense_hat import SenseHat
from datetime import datetime, timedelta
from colr import color
import random
from afisare_imagine_de_sfarsit_de_nivel_1 import afisare_imagine_de_sfarsit_de_nivel_1
from afisare_imagine_de_sfarsit_de_nivel_2 import afisare_imagine_de_sfarsit_de_nivel_2
from ENTERING_MAIN_MENU import ENTERING_MAIN_MENU
from Controls_Level_5 import Controls_Level_5
from vector_is_hit import vector_is_hit
from boss_gets_angry import boss_gets_angry
from animation_win_Level5 import animation_win_Level5
from pathlib import Path
from pygame import mixer, mixer_music
from animation_lose_level_1 import animation_lose_level_1
from animation_easter_egg import animation_easter_egg

sense = SenseHat()

#CULORI pentru SenseHat (COLOURS for the SenseHat):
black = [0, 0, 0]
cyan = [0, 255, 255]
blue = [0, 0, 255]
darker_blue = [0, 102, 204]
red = [248, 0, 0]
gold = [248, 212, 0]
green = [0, 255, 0]
white = [248, 252, 248]
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

def Level5():
    Controls_Level_5()
    intro_level5 = [
        red, red, red, red, red, red, red, red,
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, black, black, toxicgreen,
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, black, black, black,
        black, black, black, black, black, black, black, black,
        pink, black, black, black, black, black, black, black,
    ]
    sense.set_pixels(intro_level5)
    dir_path = Path(__file__).parent.resolve()
    boss_life_hearts = 0
    vector_life_hearts = 3
    boss_x, boss_y = 2, 7
    vector_x, vector_y = 7, 0
    nr_bullets = 0
    ok_left = False # Boss moves to the left 
    ok_right = True # Boss moves to the right
    ok_angry = False
    ok_music = False
    points = {}
    bullets_fired = {}
    boss_bullets_fired = {}
    #EASTER EGG :D
    easter_controls = []
    easter_solution = ["up", "up", "down", "left", "left", "right", "up", "down", "down", "right", "left", "up", "down"]
    initial_date, initial_date_boss_bullet = datetime.now(), datetime.now()
    print(color("You have " + str(vector_life_hearts) + " hearts. Pick up bullets and shoot Medios in order to win. Be careful and watch out for the fire balls! You got this!", fore=green))
    while (boss_life_hearts < 8):
        if ok_music == False:
            ok_music = True
            initial_music_date = datetime.now()
            final_music_date = initial_music_date + timedelta(seconds=293)
            path1 = dir_path/'melodie_boss.mp3'
            mixer.music.load(str(path1))
            mixer.music.set_volume(3)
            mixer.music.play()
        elif datetime.now() >= final_music_date:
            ok_music = False
        if (vector_life_hearts == 0):
            mixer.music.stop()
            path2 = dir_path/'d.mp3'
            mixer.music.load(str(path2))
            mixer.music.set_volume(1)
            mixer.music.play()
            animation_lose_level_1()
            break
        event = sense.stick.wait_for_event(emptybuffer = True)
        if event.action == "pressed":
            #IMPLEMENTING BOSS'S MOVEMENTS
            if len(easter_controls) == 13:
                ok_easter = True
                for poz in range(0, len(easter_controls)):
                    if easter_controls[poz] != easter_solution[poz]:
                        ok_easter = False
                        break
                if ok_easter == True:
                    print(color("Awesome! You have found the easter egg! You win automatically! Less goo!", fore=gold))
                    mixer.music.stop()
                    path2 = dir_path/'letsgoo.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    animation_easter_egg()
                    break
            elif len(easter_controls) < 13:
                easter_controls.append(event.direction)
            if not((event.direction == "left" and vector_y == 0) or (event.direction == "up" and vector_x == 5) or (event.direction == "right" and vector_y == 7) or (event.direction == "down" and vector_x == 7) or (event.direction == "middle" and nr_bullets == 0)):
                sense.set_pixel(boss_y, boss_x, black)
                if ok_right == True and ok_left == False:
                    if (boss_y + 1 > 7):
                        boss_y -= 1
                        ok_right = False
                        ok_left = True
                    else:
                        boss_y += 1
                elif ok_right == False and ok_left == True:
                    if (boss_y - 1 < 0):
                        boss_y += 1
                        ok_right = True
                        ok_left = False
                    else:
                        boss_y -= 1
                if boss_life_hearts < 4:
                    sense.set_pixel(boss_y, boss_x, toxicgreen)
                elif boss_life_hearts == 4 and ok_angry == False:
                    print(color("\nMEDIOS IS ANGRY!\n", fore=purple))
                    mixer.music.stop()
                    path2 = dir_path/'MONSTER_SCREAM.mp3'
                    mixer.music.load(str(path2))
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    sense.set_pixel(boss_y, boss_x, toxicgreen)
                    boss_gets_angry(boss_x, boss_y)
                    ok_angry = True
                    ok_music = False
                else:
                    sense.set_pixel(boss_y, boss_x, purple)
                #IMPLEMENTING BULLETS' MOVEMENTS
                for bullet in list(bullets_fired):
                    if bullets_fired[bullet][0] == 1:
                        sense.set_pixel(bullets_fired[bullet][1], 1, black)
                        bullets_fired.pop(bullet)
                    elif bullets_fired[bullet][0] - 1 == boss_x and bullets_fired[bullet][1] == boss_y:
                        sense.set_pixel(boss_life_hearts, 0, black)
                        boss_life_hearts += 1
                        sense.set_pixel(bullets_fired[bullet][1], bullets_fired[bullet][0], black)
                        bullets_fired.pop(bullet)
                    else:
                        bullets_fired[bullet][0] -= 1
                for bullet in bullets_fired.values():
                    sense.set_pixel(bullet[1], bullet[0] + 1, black)
                    sense.set_pixel(bullet[1], bullet[0], blue)
                if not((event.direction == "left" and vector_y == 0) or (event.direction == "up" and vector_x == 5) or (event.direction == "right" and vector_y == 7) or (event.direction == "down" and vector_x == 7) or (event.direction == "middle" and nr_bullets == 0)):
                    for fired_bullet in list(boss_bullets_fired):
                        if boss_bullets_fired[fired_bullet][0] == 7:
                            sense.set_pixel(boss_bullets_fired[fired_bullet][1], 7, black)
                            boss_bullets_fired.pop(fired_bullet)
                        elif (boss_bullets_fired[fired_bullet][0] == vector_x and boss_bullets_fired[fired_bullet][1] == vector_y) or (boss_bullets_fired[fired_bullet][0] + 1 == vector_x and boss_bullets_fired[fired_bullet][1] == vector_y):
                            sense.set_pixel(boss_bullets_fired[fired_bullet][1], boss_bullets_fired[fired_bullet][0], black)
                            boss_bullets_fired.pop(fired_bullet)
                            vector_is_hit(vector_x, vector_y)
                            vector_life_hearts -= 1
                            print(color("\n\nYOU HAVE " + str(vector_life_hearts) + " LIVES LEFT!\n", fore=green))
                        else:
                            boss_bullets_fired[fired_bullet][0] += 1
                    for fired_bullet in boss_bullets_fired.values():
                        sense.set_pixel(fired_bullet[1], fired_bullet[0] - 1, black)
                        sense.set_pixel(fired_bullet[1], fired_bullet[0], red)
            sense.set_pixel(vector_y, vector_x, black)
            #IF A BULLET IS IN THE WAY OF A NON-PICKED BULLET IT WILL HOP OVER IT
            for point in list(points):
                sense.set_pixel(points[point][1], points[point][0], white) 
            pixels = sense.get_pixels()
            if event.direction == "up" and vector_x > 5:
                up = 8 * (vector_x - 1) + vector_y
                if pixels[up] == white:
                    points.pop("point " + str(vector_x - 1) + " and " + str(vector_y))
                    nr_bullets += 1
                vector_x -= 1
            elif event.direction == "down" and vector_x < 7:
                down = 8 * (vector_x + 1) + vector_y
                if pixels[down] == white:
                    points.pop("point " + str(vector_x + 1) + " and " + str(vector_y))
                    nr_bullets += 1
                vector_x += 1
            elif event.direction == "left" and vector_y > 0:
                left = 8 * vector_x + vector_y - 1
                if pixels[left] == white:
                    points.pop("point " + str(vector_x) + " and " + str(vector_y - 1))
                    nr_bullets += 1
                vector_y -= 1
            elif event.direction == "right" and vector_y < 7:
                right = 8 * vector_x + vector_y + 1
                if pixels[right] == white:
                    points.pop("point " + str(vector_x) + " and " + str(vector_y + 1))
                    nr_bullets += 1
                vector_y += 1
            elif event.direction == "middle":
                if nr_bullets > 0:
                    nr_bullets -= 1
                    new_fired_bullet = [vector_x - 1, vector_y]
                    sense.set_pixel(new_fired_bullet[1], new_fired_bullet[0], blue)
                    bullets_fired["bullet " + str(vector_x - 1) + " and " + str(vector_y)] = new_fired_bullet
                    print(color("\nYou have " + str(nr_bullets) + " bullet left!\n", fore=green))
                else:
                    print(color("\nYOU DON'T HAVE ENOUGH BULLETS TO SHOOT!\n", fore=red))
            sense.set_pixel(vector_y, vector_x, pink)
            if not((event.direction == "left" and vector_y == 0) or (event.direction == "up" and vector_x == 5) or (event.direction == "right" and vector_y == 7) or (event.direction == "down" and vector_x == 7) or (event.direction == "middle" and nr_bullets == 0)):
                for fired_bullet in list(boss_bullets_fired):
                    if boss_bullets_fired[fired_bullet][0] == vector_x and boss_bullets_fired[fired_bullet][1] == vector_y:
                        sense.set_pixel(boss_bullets_fired[fired_bullet][1], boss_bullets_fired[fired_bullet][0], black)
                        boss_bullets_fired.pop(fired_bullet)
                        vector_is_hit(vector_x, vector_y)
                        vector_life_hearts -= 1
                        print(color("\n\nYOU HAVE " + str(vector_life_hearts) + " LIVES LEFT!\n", fore=green))
            final_date_new_bullet = initial_date + timedelta(seconds = 5)
            if datetime.now() >= final_date_new_bullet:
                point_x = random.randint(5, 7)
                point_y = random.randint(0, 7)
                sense.set_pixel(point_y, point_x, white)
                new_point = [point_x, point_y]
                points["point " + str(point_x) + " and " + str(point_y)] = new_point
                initial_date = datetime.now()
            if boss_life_hearts < 4:
                final_date_boss_bullet = initial_date_boss_bullet + timedelta(seconds = 10)
            else:
                final_date_boss_bullet = initial_date_boss_bullet + timedelta(seconds = 5)
            if datetime.now() >= final_date_boss_bullet:
                boss_bullet_x = 3
                boss_bullet_y = boss_y
                sense.set_pixel(boss_bullet_y, boss_bullet_x, red)
                new_boss_bullet = [boss_bullet_x, boss_bullet_y]
                boss_bullets_fired["fired " + str(boss_bullet_x) + " and " + str(boss_bullet_y)] = new_boss_bullet
                initial_date_boss_bullet = datetime.now()
    if vector_life_hearts != 0 and ok_easter == False:
        
        mixer.music.stop()
        path2 = dir_path/'victory_boss.mp3'
        mixer.music.load(str(path2))
        mixer.music.set_volume(1)
        mixer.music.play()
        animation_win_Level5()
    afisare_imagine_de_sfarsit_de_nivel_1()
    afisare_imagine_de_sfarsit_de_nivel_2()
    ENTERING_MAIN_MENU()

#Level5()