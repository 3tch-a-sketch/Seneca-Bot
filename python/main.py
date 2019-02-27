import time, keyboard, win32api, win32con, win32gui
import minilib as mouse


loggedin = True

if loggedin =! True:
    email = input('email:')
    password = input("password:")

# DEBUG:
email = "15samuletchells@catmosecollege.com"
# DEBUG:

globaldelay = 0.2   #this should be higher on slower computers.

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

keyboard.press_and_release("win+r")
time.sleep(globaldelay)
keyboard.write("chrome https://app.senecalearning.com/login")
keyboard.press_and_release("enter")
time.sleep(globaldelay + 2)
keyboard.press_and_release("f11")

keyboard.press_and_release("enter")
if loggedin == False:
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
