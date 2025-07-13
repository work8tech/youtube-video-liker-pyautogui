import pyautogui
import time

number_of_likes = int(input("How many videos should we give likes on?: "))
print(f"Program begins in 3 seconds to give {number_of_likes} on your favorite channel's youtube shorts.")
channel_link = "https://www.youtube.com/@diplomaduck/shorts"

time.sleep(3)

pyautogui.press('win')
time.sleep(1)
pyautogui.write('edge',0.05)
pyautogui.press('enter')

pyautogui.moveTo(167,52,3)

pyautogui.click()

pyautogui.write(channel_link)
pyautogui.press('enter') 
pyautogui.moveTo(562,963,3)
pyautogui.click()
pyautogui.moveTo(1355,541,3)
for i in range(number_of_likes):
    time.sleep(4)
    pyautogui.click()
    pyautogui.press('down')