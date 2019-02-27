import win32api, win32con, win32gui, time, win32clipboard

def setClipBoard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()

def getClipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def moveClick(x, y, t=0):
    x, y = int(x), int(y)
    win32api.SetCursorPos((x, y))
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(t)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def hover(x, y, t=0):
    x, y = int(x), int(y)
    win32api.SetCursorPos((x, y))
    time.sleep(t)

def click(x, y, t=0):
    x, y = int(x), int(y)
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

def position():
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    return x, y

def screenSize():
    width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    return width, height

def yPercentToPosition(percent):
    return round(screenSize()[0]*percent, 0)

def xPercentToPosition(percent):
    return round(screenSize()[1]*percent, 0)

def positionPercent(x, y, accuracy=5):
    width, height = screenSize()
    relativeX = (x / width) * 100
    relativeY = (y / height) * 100
    relativeXrounded = int(round((x / width) * 100, accuracy))
    relativeYrounded = int(round((y / height) * 100, accuracy))
    return relativeXrounded, relativeYrounded

def currentPositionPercent(accuracy=5): # accuracy is decimal places in percentage
    width, height = screenSize()
    y, x = position()
    relativeX = (x / width) * 100
    relativeY = (y / height) * 100
    relativeXrounded = int(round((x / width) * 100, accuracy))
    relativeYrounded = int(round((y / height) * 100, accuracy))
    return relativeXrounded, relativeYrounded
