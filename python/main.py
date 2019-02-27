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

# non user configurable vars

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
jsPath = "..\\javascript\\answer.js"
js = ""
with open(jsPath, "r") as f:
    js = f.read()

print("JS: "+js)

keyboard.press_and_release("win+r")
time.sleep(globaldelay)

if loggedin != True:
    keyboard.write("chrome https://app.senecalearning.com/login")
else:
    keyboard.write("https://app.senecalearning.com/classroom/course/"+classurl)

keyboard.press_and_release("enter")
time.sleep(globaldelay + 5)
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

mouse.moveClick(y, x, 0.5)

time.sleep(globaldelay)
keyboard.press_and_release("f12")
x = mouse.xPercentToPosition(0.63)
y = mouse.yPercentToPosition(0.98)
print(str(x)+" "+str(y))

time.sleep(globaldelay+2)
mouse.moveClick(y, x, 0.5)

mouse.setClipBoard(js)
time.sleep(globaldelay)

keyboard.press_and_release("ctrl+v")
time.sleep(globaldelay)
keyboard.press_and_release("enter")
