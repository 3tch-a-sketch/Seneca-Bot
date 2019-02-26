import time, keyboard, win32api, win32con, time
import minilib as mouse

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
print(width, height)

while True:
    Xpos, Ypos = mouse.pos()
    Xrel = width / Xpos
    Yrel = height / Ypos
    print(Xrel + ' ' + Yrel)
