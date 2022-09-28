import time

import pyautogui

pyautogui.moveTo(pyautogui.size().width / 2, pyautogui.size().height / 2)


def drag_quare():
    pyautogui.moveRel(300, 0, duration=1)
    pyautogui.moveRel(0, 300, duration=1)
    pyautogui.moveRel(-300, 0, duration=1)
    pyautogui.moveRel(0, -300, duration=1)


def move_up(units, seconds):
    pyautogui.moveRel(units, 0, duration=seconds)


def move_down(units, seconds):
    pyautogui.moveRel(units, 0, duration=seconds)


def move_left(units, seconds):
    pyautogui.moveRel(units, 0, duration=seconds)


def move_right(units, seconds):
    pyautogui.moveRel(units, 0, duration=seconds)


while True:
    drag_quare()
    time.sleep(5)
