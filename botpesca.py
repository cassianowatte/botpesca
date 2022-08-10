import pyautogui


a = pyautogui.locateOnScreen('vara.png')
b = pyautogui.locateOnScreen('alga.png')

for t in range(20):
    pyautogui.moveTo(a[0] + 10, a[1] + 10, duration=0.025)
    pyautogui.rightClick(a[0] + 10, a[1] + 10, duration=0.025)
    pyautogui.moveTo(358, 451, duration=0.025)
    pyautogui.click(x=358, y=451, duration=0.025)
