from sense_hat import SenseHat
from time import sleep

def animation_lose_level_1():
    sense = SenseHat()
    white = [255, 255, 255]
    pink1 = [255, 230, 242]
    pink2 = [255, 214, 235]
    pink3 = [255, 199, 227]
    pink4 = [255, 179, 217]
    pink5 = [255, 163, 209]
    pink6 = [255, 148, 201]
    pink7 = [255, 128, 191]
    pink8 = [255, 112, 184]
    pink9 = [255, 105, 180]
    pink = [255, 20, 147]
    for i in range(8):
        sense.set_pixel(0, i, white)
        sense.set_pixel(1, i, white)
        sense.set_pixel(2, i, white)
        sense.set_pixel(3, i, white)
        sense.set_pixel(4, i, white)
        sense.set_pixel(5, i, white)
        sense.set_pixel(6, i, white)
        sense.set_pixel(7, i, white)
        sleep(0.4)

    image1 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink1, pink1, pink1, pink1, white, white,
        white, white, pink1, pink1, pink1, pink1, white, white,
        white, white, pink1, pink1, pink1, pink1, white, white,
        white, white, pink1, pink1, pink1, pink1, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image2 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink2, pink2, pink2, pink2, white, white,
        white, white, pink2, pink2, pink2, pink2, white, white,
        white, white, pink2, pink2, pink2, pink2, white, white,
        white, white, pink2, pink2, pink2, pink2, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image3 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink3, pink3, pink3, pink3, white, white,
        white, white, pink3, pink3, pink3, pink3, white, white,
        white, white, pink3, pink3, pink3, pink3, white, white,
        white, white, pink3, pink3, pink3, pink3, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image4 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink4, pink4, pink4, pink4, white, white,
        white, white, pink4, pink4, pink4, pink4, white, white,
        white, white, pink4, pink4, pink4, pink4, white, white,
        white, white, pink4, pink4, pink4, pink4, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image5 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink5, pink5, pink5, pink5, white, white,
        white, white, pink5, pink5, pink5, pink5, white, white,
        white, white, pink5, pink5, pink5, pink5, white, white,
        white, white, pink5, pink5, pink5, pink5, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image6 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink6, pink6, pink6, pink6, white, white,
        white, white, pink6, pink6, pink6, pink6, white, white,
        white, white, pink6, pink6, pink6, pink6, white, white,
        white, white, pink6, pink6, pink6, pink6, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image7 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink7, pink7, pink7, pink7, white, white,
        white, white, pink7, pink7, pink7, pink7, white, white,
        white, white, pink7, pink7, pink7, pink7, white, white,
        white, white, pink7, pink7, pink7, pink7, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image8 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink8, pink8, pink8, pink8, white, white,
        white, white, pink8, pink8, pink8, pink8, white, white,
        white, white, pink8, pink8, pink8, pink8, white, white,
        white, white, pink8, pink8, pink8, pink8, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image9 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink9, pink9, pink9, pink9, white, white,
        white, white, pink9, pink9, pink9, pink9, white, white,
        white, white, pink9, pink9, pink9, pink9, white, white,
        white, white, pink9, pink9, pink9, pink9, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image10 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image11 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, pink, pink, white,
        white, white, pink, pink, white, white, pink, white,
        white, white, pink, pink, pink, white, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image12 = [
        white, white, white, white, white, white, pink, pink,
        white, pink, pink, white, white, white, white, pink,
        white, pink, pink, white, white, white, white, white,
        white, pink, white, white, pink, white, white, white,
        white, white, white, pink, pink, pink, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image13 = [
        pink, pink, white, white, white, white, white, white,
        pink, pink, white, white, white, white, white, white,
        pink, white, white, white, white, white, white, white,
        white, white, white, white, pink, white, white, white,
        white, white, white, pink, pink, pink, white, white,
        white, white, pink, pink, pink, pink, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image14 = [
        pink, pink, white, white, white, white, white, white,
        pink, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, pink, white, white, white,
        white, white, white, white, pink, pink, white, white,
        white, white, pink, white, white, pink, white, white,
        white, pink, pink, pink, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]
    
    image15 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, pink, white, white,
        white, white, white, white, white, pink, pink, white,
        white, pink, white, white, white, white, pink, white,
        pink, pink, pink, white, white, white, white, white,
    ]
    
    image16 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, pink, white,
        white, white, white, white, white, white, pink, pink,
        pink, white, white, white, white, white, white, pink,
    ]
    
    image17 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, pink,
        white, white, white, white, white, white, white, pink,
    ]
    
    image18 = [
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
        white, white, white, white, white, white, white, white,
    ]

    images_for_printing = [image1, image2, image3, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13, image14, image15, image16, image17, image18]
    for i in images_for_printing:
        sense.set_pixels(i)
        sleep(0.3)
    sense.clear()
