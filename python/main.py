import time, keyboard, win32api, win32con, win32gui
import minilib as mouse

email = input('email:')
password = input("password:")
globaldelay = 0.2   #this should be higher on slower computers.

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
#print(width, height)

keyboard.press_and_release("left windows+r")
time.sleep(globaldelay)
keyboard.write("iexplore -k https://app.senecalearning.com/login")
keyboard.press_and_release("enter")
time.sleep(globaldelay)
keyboard.write(email)
del email
time.sleep(globaldelay)
keyboard.press_and_release("tab")
time.sleep(globaldelay)
keyboard.write(password)
del password
