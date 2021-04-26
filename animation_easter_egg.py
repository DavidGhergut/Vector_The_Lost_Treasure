from sense_hat import SenseHat
import time

s = SenseHat()

brown = (136, 68, 16)
green = (97, 222, 42)
yellow = (255, 255, 0)
blue = (255, 255, 0)
red = (248, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (0, 0, 255)

def animation_easter_egg():
    def chest1():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        W, O, O, O, O, O, O, O,
        W, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo
        
    def chest2():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        W, O, O, O, O, O, O, O,
        W, O, O, O, O, O, O, O,
        W, W, O, O, O, O, O, O,
        W, W, O, O, O, O, O, O,
        W, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def chest3():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        W, O, O, O, O, O, O, O,
        W, W, O, O, O, O, O, O,
        W, W, O, O, O, O, O, O,
        W, W, W, O, O, O, O, O,
        W, W, W, O, O, O, O, O,
        W, W, O, O, O, O, O, O,
        W, O, O, O, O, O, O, O,
        ]
        return logo
        
    def chest4():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        W, O, O, O, O, O, O, O,
        W, W, O, O, O, O, O, O,
        W, W, W, O, O, O, O, O,
        W, W, W, O, O, O, O, O,
        W, W, W, W, O, O, O, O,
        W, W, W, W, O, O, O, O,
        W, W, W, O, O, O, O, O,
        W, W, O, O, O, O, O, O,
        ]
        return logo
        
    def chest5():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        W, W, O, O, O, O, O, O,
        W, W, W, O, O, O, O, O,
        W, W, W, W, O, O, O, O,
        W, W, W, W, O, O, O, O,
        W, W, W, W, W, O, O, O,
        W, W, W, W, W, O, O, O,
        W, W, W, W, O, O, O, O,
        W, W, W, O, O, O, O, O,
        ]
        return logo
        
    def chest6():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, W, W, O, O, O, O, O,
        W, W, W, W, O, O, O, O,
        W, W, W, W, W, O, O, O,
        W, W, W, W, W, O, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, O, O, O,
        W, W, W, W, O, O, O, O,
        ]
        return logo
        
    def chest7():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, W, W, O, O, O, O,
        O, W, W, W, W, O, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, O, O,
        O, W, W, W, W, O, O, O,
        ]
        return logo

    def chest8():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, W,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest9():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest10():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest11():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, O, W, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest12():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, O, O, W, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest13():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, W, W, O, W, W, W, O,
        O, W, W, W, O, O, W, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest14():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, W, O, O,
        O, W, W, O, W, W, W, O,
        O, W, W, W, O, O, W, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest15():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, W, W, O, O, O,
        O, O, O, O, W, W, W, O,
        O, W, W, O, O, W, W, W,
        O, W, W, W, O, O, W, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest16():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, W, W, W, O,
        O, O, O, O, O, W, W, O,
        O, W, W, O, O, W, W, W,
        O, W, W, W, O, O, W, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest17():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, W, W, W,
        O, O, O, O, O, W, W, W,
        O, W, W, O, O, O, W, W,
        O, W, W, W, O, O, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest18():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, W, W, W,
        O, O, O, O, O, O, W, W,
        O, W, W, O, O, O, O, W,
        O, W, W, W, O, O, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        

    def chest19():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, W, W,
        O, O, O, O, O, O, O, W,
        O, W, W, O, O, O, O, O,
        O, W, W, W, O, O, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest20():
        W = white
        Y = yellow
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, W,
        O, O, O, O, O, O, O, O,
        O, W, W, O, O, O, O, O,
        O, W, W, W, O, O, O, O,
        W, W, W, W, W, W, O, O,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest21():
        Y = red 
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, O, O, O, O, O,
        O, W, W, W, O, O, O, O,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest22():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, O, O, O, O, O,
        O, W, W, W, Y, Y, O, O,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest23():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, Y, O, O, O, O,
        O, W, W, W, Y, Y, O, O,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest24():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, Y, O, O, O, O,
        O, W, W, Y, O, Y, O, O,
        O, W, W, W, Y, Y, O, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest25():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, O, O, O,
        O, O, O, Y, O, Y, O, Y,
        O, W, W, Y, O, Y, O, Y,
        O, W, W, W, Y, Y, O, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest26():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, O, Y, O, Y,
        O, W, W, Y, O, Y, O, Y,
        O, W, W, W, Y, Y, Y, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest27():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, O, Y, U, Y,
        O, W, W, Y, Y, Y, Y, Y,
        O, W, W, W, Y, Y, Y, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
    
    def chest28():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, Y, Y, Y, Y, Y,
        O, W, W, W, Y, Y, Y, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest29():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, Y,
        O, W, W, W, Y, Y, Y, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest30():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, Y,
        O, W, W, G, Y, Y, Y, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest31():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, Y,
        O, W, W, G, G, Y, Y, Y,
        W, W, W, W, W, W, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest32():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, Y,
        O, W, W, G, G, Y, Y, Y,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest33():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, Y,
        O, W, W, G, G, Y, G, Y,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest34():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, Y,
        O, W, W, G, G, Y, G, G,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest35():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        logo = [
        O, O, O, O, Y, Y, Y, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, G,
        O, W, W, G, G, Y, G, G,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest36():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        P = pink
        logo = [
        O, O, O, O, Y, Y, P, O,
        O, O, O, Y, U, Y, U, Y,
        O, W, W, G, Y, Y, Y, G,
        O, W, W, G, G, Y, G, G,
        W, W, W, G, W, G, Y, G,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest37():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        P = pink
        logo = [
        O, O, O, O, Y, Y, P, O,
        O, O, O, Y, U, P, U, Y,
        O, W, W, G, Y, Y, Y, G,
        O, W, W, G, G, Y, G, G,
        W, W, W, W, W, G, Y, G,
        W, W, W, G, W, W, W, G,
        O, W, W, W, W, W, W, O,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest38():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        P = pink
        logo = [
        O, O, O, O, P, Y, P, O,
        O, O, O, Y, U, P, U, Y,
        O, W, W, G, Y, Y, Y, G,
        O, W, W, G, G, Y, G, G,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, G,
        O, W, W, G, W, W, W, G,
        O, O, W, W, W, W, O, O,
        ]
        return logo
        
    def chest39():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        P = pink
        logo = [
        O, O, O, O, P, Y, P, O,
        O, O, O, Y, U, P, U, Y,
        O, W, W, G, Y, Y, Y, G,
        O, W, W, G, G, Y, G, G,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, G,
        O, O, W, G, W, W, O, G,
        ]
        return logo
        
    def chest40():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        P = pink
        logo = [
        O, O, O, O, P, Y, P, O,
        O, O, O, Y, U, P, U, Y,
        O, W, W, G, Y, Y, Y, G,
        O, W, W, G, G, Y, G, G,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, G,
        O, O, W, G, G, W, G, G,
        ]
        return logo
        
    def chest41():
        Y = red
        W = white
        O = nothing
        U = blue
        G = green
        P = pink
        logo = [
        O, O, O, O, P, Y, P, O,
        O, O, O, Y, U, P, U, Y,
        O, W, W, G, Y, Y, Y, G,
        O, W, W, G, G, Y, G, G,
        W, W, W, W, W, G, Y, Y,
        W, W, W, W, W, W, W, W,
        O, W, W, W, W, W, W, O,
        O, O, W, G, G, G, G, G,
        ]
        return logo

    images = [chest1, chest2, chest3, chest4, chest5, chest6, chest7, chest8, chest9,
    chest10, chest11, chest12, chest13, chest14, chest15, chest16, chest17, chest18, chest19, chest20,
    chest21, chest22, chest23, chest24, chest25, chest26, chest27, chest28, chest29, chest30,
    chest31, chest32, chest33, chest34, chest35, chest36, chest37, chest38, chest39, chest40,
    chest41]
    count = 0

    while count < len(images): 
        s.set_pixels(images[count % len(images)]())
        time.sleep(0.3)
        count += 1