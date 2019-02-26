import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width, height = pyautogui.size()

mouseX, moouseY = pyautogui.position()

for i in range(3):
      pyautogui.moveTo(100, 100, duration=0.1)
      pyautogui.moveTo(200, 100, duration=0.1)
      pyautogui.moveTo(200, 200, duration=0.1)
      pyautogui.moveTo(100, 200, duration=0.1)
      pyautogui.moveRel(0, -100, duration=0.25)

pyautogui.click(200, 250, button='right')

pyautogui.mouseDown()
pyautogui.mouseup()

pyautogui.doubleClick()

pyautogui.scroll(200)

pyautogui.typewrite("Hello World",0.1)
