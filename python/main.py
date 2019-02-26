import minilib, time, wx, keyboard


import win32api, win32con, time

def moveClick(x, y, t=0):
    win32api.SetCursorPos((x, y))
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def hover(x, y, t=0):
    win32api.SetCursorPos((x, y))
    time.sleep(t)

def click(x, y, t=0):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def drag(x1, y1, x2, y2, t=0):
    win32api.SetCursorPos((x1, y1))
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
    time.sleep(t)
    win32api.SetCursorPos((x2, y2))
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)



app = wx.App(False)
width, height = wx.GetDisplaySize()
print(width, height)

moveClick(0,1040,0.1)
time.sleep(0.5)
keyboard.write('Internet Explorer')
keyboard.press('enter')
hover
