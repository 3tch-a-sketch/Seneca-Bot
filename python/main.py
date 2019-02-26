import time, keyboard, win32api, win32con, win32gui
import minilib as mouse

email = input('email:')
password = input("password:")
login = False

# DEBUG:
email = "15samuletchells@catmosecollege.com"
# DEBUG:

globaldelay = 0.2   #this should be higher on slower computers.

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

keyboard.press_and_release("win")
time.sleep(globaldelay)
keyboard.write("chrome https://app.senecalearning.com/login")
keyboard.press_and_release("enter")
time.sleep(globaldelay + 2)
keyboard.press("alt")
keyboard.press("space")
keyboard.release("alt")
keyboard.release("space")
time.sleep(globaldelay)
keyboard.press_and_release("down")
time.sleep(globaldelay)
keyboard.press_and_release("down")
time.sleep(globaldelay)
keyboard.press_and_release("down")
time.sleep(globaldelay)
keyboard.press_and_release("down")
time.sleep(globaldelay)

keyboard.press_and_release("enter")
if login != True:
    keyboard.write(email)
    del email
    time.sleep(globaldelay)
    keyboard.press_and_release("tab")
    time.sleep(globaldelay)
    keyboard.write(password)
    del password
    time.sleep(globaldelay)
    keyboard.press_and_release("enter")

mouse.hover(mouse.xPercentToPosition(40), mouse.yPercentToPosition(5), 0.5)
