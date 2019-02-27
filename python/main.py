import time, keyboard, win32api, win32con, win32gui
import minilib as mouse

loggedin = True
classurl = "fe56ca00-05aa-11e8-9a61-01927559cfd5" # the url looks like this https://app.senecalearning.com/classroom/course/fe56ca00-05aa-11e8-9a61-01927559cfd5 we want this part of it

if loggedin != True:
    email = input('email:')
    password = input("password:")

# DEBUG:
email = "15samuletchells@catmosecollege.com"
# DEBUG:

globaldelay = 0.2   #this should be higher on slower computers.

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

keyboard.press_and_release("win+r")
time.sleep(globaldelay)

if loggedin != True:
    keyboard.write("chrome https://app.senecalearning.com/login")
else:
    keyboard.write("https://app.senecalearning.com/classroom/course/"+classurl)

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

print(mouse.screenSize())
x = mouse.xPercentToPosition(0.05)
y = mouse.yPercentToPosition(0.74)
print(str(x)+" "+str(y))

mouse.hover(y, x, 0.5)
