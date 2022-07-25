from pyautogui import screenshot as SS
from pyclick import HumanClicker as HC

while True:
    if SS(region=(100,200, 1, 1)).getcolors() == [(1, (67, 198, 96))]:
        HC().click()
        break