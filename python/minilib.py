import win32api, win32con, time

def click(x,y,t):
    win32api.SetCursorPos((x,y))
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def move(x,y,t):
    win32api.SetCursorPos((x,y))
    time.sleep(t)
