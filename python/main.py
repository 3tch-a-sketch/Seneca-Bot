import time, wx, keyboard, win32api, win32con, time
import minilib as mouse

app = wx.App(False)
width, height = wx.GetDisplaySize()
print(width, height)

mouse.moveClick(0, width -10, 0.1)
time.sleep(0.5)
keyboard.write('Internet Explorer')
keyboard.press('enter')
