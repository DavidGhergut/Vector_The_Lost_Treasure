
from sense_hat import SenseHat
import time

s = SenseHat()

brown = (135, 80, 22)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def animation_win_Level5():
    def chest1():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        O, W, W, W, W, W, W, O,
        O, B, B, W, W, B, B, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        ]
        return logo
        
    def chest2():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        O, W, W, W, W, W, W, O,
        O, B, Y, W, W, Y, B, O,
        O, B, B, U, Y, B, B, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        ]
        return logo

    def chest3():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        O, W, W, W, W, W, W, O,
        O, O, Y, W, W, Y, O, O,
        O, B, Y, Y, Y, Y, B, O,
        O, B, B, U, Y, B, B, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        ]
        return logo
        
    def chest4():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, B, B, B, B, B, B, O,
        O, W, W, W, W, W, W, O,
        O, O, Y, W, W, Y, O, O,
        O, Y, G, Y, G, Y, Y, O,
        O, B, Y, Y, Y, Y, B, O,
        O, B, B, U, Y, B, B, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        ]
        return logo
        
    def chest5():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, O, O, O,
        O, O, Y, Y, Y, Y, O, O,
        U, Y, G, Y, G, Y, Y, Y,
        O, B, Y, Y, Y, Y, B, G,
        O, B, B, U, Y, B, B, O,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        ]
        return logo
        
    def chest6():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, O, Y, U, O, O, O,
        O, O, Y, Y, Y, Y, O, O,
        Y, Y, G, Y, G, Y, Y, Y,
        U, B, Y, Y, Y, Y, B, Y,
        O, B, B, U, Y, B, B, G,
        O, B, B, B, B, B, B, O,
        O, B, B, B, B, B, B, O,
        ]
        return logo
        
    def chest7():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, Y, U, O, O, O,
        O, O, Y, Y, Y, Y, O, O,
        Y, Y, G, Y, G, Y, Y, Y,
        Y, B, Y, Y, Y, Y, B, Y,
        U, B, B, U, Y, B, B, Y,
        O, B, B, B, B, B, B, G,
        O, B, B, B, B, B, B, O,
        ]
        return logo

    def chest8():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, Y, U, O, O, O,
        O, O, Y, Y, Y, Y, O, O,
        Y, Y, G, Y, G, Y, Y, Y,
        Y, B, Y, Y, Y, Y, B, Y,
        Y, B, B, U, Y, B, B, Y,
        U, B, B, B, B, B, B, Y,
        O, B, B, B, B, B, B, G,
        ]
        return logo
        
    def chest9():
        W = white
        Y = yellow
        B = brown
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, Y, U, O, O, O,
        O, O, Y, Y, Y, Y, O, O,
        Y, Y, G, Y, G, Y, Y, Y,
        Y, B, Y, Y, Y, Y, B, Y,
        Y, B, B, U, Y, B, B, Y,
        Y, B, B, B, B, B, B, Y,
        U, B, B, B, B, B, B, G,
        ]
        return logo

    images = [chest1, chest2, chest3, chest4, chest5, chest6, chest7, chest8, chest9]
    count = 0

    while count < len(images): 
        s.set_pixels(images[count % len(images)]())
        time.sleep(0.5)
        count += 1

