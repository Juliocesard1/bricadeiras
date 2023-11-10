import webbrowser
import pyautogui
from time import sleep
import pyperclip

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')



while True:
    webbrowser.open_new_tab('https://www.instagram.com/')
    sleep(2)
    pyautogui.click(1071,1037,duration=1)
    sleep(2)
    pyautogui.click(1216,1033,duration=1)
    sleep(3)
    pyautogui.click(1447,367, duration= 1 )
    sleep(10)
    pyautogui.typewrite('lopz1570@gmail.com')
    sleep(2)
    pyautogui.click(50,0,duration=0.1)
    sleep(2)
    pyautogui.click(1358,416,duration=2)
    sleep(2)
    escrever('python é legal')
    sleep(2)
    pyautogui.click(1511,461,duration=2)
    sleep(2)
    pyautogui.click(1445,615,duration=2)
    sleep(2)
    pyautogui.click(1068,262,duration=1)
    sleep(2)
    pyautogui.click(1232,185,duration=1)
    sleep(2)
    pyautogui.typewrite('nike')
    sleep(2)
    pyautogui.click(1215,237,duration=1)
    sleep(2)
    pyautogui.click(1201,683,duration=1)
    sleep(2)
    coracao = pyautogui.locateCenterOnScreen('coracao.png')  
    sleep(1)
    if coracao is not None:
       sleep(86400)
    elif coracao == None:  
        pyautogui.click(1362,686,duration=1)
    sleep(2)
    pyautogui.click(1438,779,duration=1)
    sleep(2)
    pyautogui.typewrite('top dems')
    sleep(2)
    pyautogui.click(1727,777,duration=1)
    sleep(86400)