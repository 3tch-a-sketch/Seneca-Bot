import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width, height = pyautogui.size()

for i in range(3):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.moveTo(100, 200, duration=0.25)
