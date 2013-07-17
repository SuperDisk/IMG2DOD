import ctypes
import os
import time

os.environ['SDL_VIDEODRIVER'] = "dummy"

import pygame
pygame.init()
pygame.display.set_mode((1, 1))

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

point = POINT()
ppoint = ctypes.pointer(point)

COLORTABLE = {
0: (0, 0, 0),
1: (109, 111, 113),
2: (7, 145, 205),
3: (105, 156, 65),
4: (244, 126, 32),
5: (214, 22, 59),
6: (110, 26, 17),
7: (248, 222, 215),
8: (255, 255, 255),
9: (209, 211, 212),
10: (115, 207, 242),
11: (155, 204, 102),
12: (255, 236, 0),
13: (214, 128, 170),
14: (129, 36, 104),
15: (142, 104, 76),
}

MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down 
MOUSEEVENTF_LEFTUP = 0x0004 # left button up 
MOUSEEVENTF_CLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP

COLORPOS = {
    0: (744, 222),
    
    1: (780, 220),

    2: (815, 222),

    3: (852, 220),

    4: (888, 220),

    5: (927, 220),

    6: (964, 220),

    7: (1000, 220),

    8: (744, 260),

    9: (780, 260),

    10: (815, 260),

    11: (852, 260),

    12: (888, 260),

    13: (927, 260),

    14: (964, 260),

    15: (1000, 260)
    }

def rgb2hex(rgb):
    return (rgb[0] << 16) + (rgb[1] << 8) + rgb[2];

def hex2rgb(hexcolor):
    r = ( hexcolor >> 16 ) & 0xFF;

    g = ( hexcolor >> 8 ) & 0xFF;

    b = hexcolor & 0xFF;

    return r, g, b

def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))

HEXATABLE = {}
for key, value in COLORTABLE.items():
    HEXATABLE[key] = rgb2hex(value)

revtable = {}
for key, value in COLORTABLE.items():
    revtable[value] = key

REVTABLE = revtable

#img = pygame.image.load(input("Give image: ")).convert()
img = pygame.image.load("C:\\evan.jpg").convert()

for i in range(6):
    print(i)
    time.sleep(1)

print("Starting.")

ctypes.windll.user32.GetCursorPos(ppoint)
offset = point.x, point.y

#img2 = img.copy()
for x in range(img.get_width()):
    for y in range(img.get_height()):

        color = rgb2hex(tuple(img.get_at((x, y))))
        newcolor = takeClosest(color, HEXATABLE.values())

        #Choose colorz
        if hex2rgb(newcolor) != (255, 255, 255):
            ctypes.windll.user32.SetCursorPos(*COLORPOS[REVTABLE[hex2rgb(newcolor)]])
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_CLICK, 0, 0, 0, 0)

            #Plot this color, or somethin
            ctypes.windll.user32.SetCursorPos(offset[0] + x, offset[1] + y)
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_CLICK, 0, 0, 0, 0)

        else: continue
        
        #Settery.
        #img2.set_at((x, y), hex2rgb(newcolor))

    time.sleep(7)

print("DONE")
#pygame.image.save(img2, "C:\\dur\\mario2.png")
