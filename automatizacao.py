import pyautogui
import time
import pandas as pd

tabela= pd.read_csv('prof4.csv')

pyautogui.click(x=467, y=741)#chrome segundo icone
time.sleep(2)
for linha in tabela.index:
    time.sleep(1)
    pyautogui.click(x=416, y=224)#clicka no perfil
    time.sleep(3)
    pyautogui.click(x=406, y=59)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(x=509, y=749)#word terceiro icone
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=454, y=748)#chorme
    time.sleep(1)
    pyautogui.click(x=19, y=59)#voltar
    time.sleep(2)
    pyautogui.tripleClick(x=375, y=118)
    time.sleep(1)
    pyautogui.press('delete')
    nome = tabela.loc[linha, 'Nome']
    pyautogui.write(nome)
    pyautogui.press('enter')
    time.sleep(2)


