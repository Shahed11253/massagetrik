import pyautogui
import time

massage = 10
while massage > 0:
    time.sleep(3)
    pyautogui.typewrite("How are you voro vai")
    pyautogui.press('enter')

    massage = massage - 1