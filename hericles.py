import os
import site
from importlib import reload

print('Instalando dependencias....')

os.system('python.exe -m pip install --upgrade pip')
os.system('pip install pyautogui')
reload(site)

import pyautogui, time, webbrowser

link = input('cole o link: ')
maximo = int(input('Quantas reaçoes quer enviar? '))
print('Caso queira parar antes de acabar aperte "Ctrl+C"')
print('Iniciando em...')
for i in range(0,5):
    print(f'{5-i}...')
    time.sleep(1)

webbrowser.open(f'{link}')
time.sleep(10)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

loop = 0

while loop <= maximo:
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'tab', 'enter')
    time.sleep(0.5)
    loop += 1
