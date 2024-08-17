import pyautogui
import cv2
import numpy as np
import time
import keyboard

base = cv2.imread('chat.PNG', cv2.IMREAD_GRAYSCALE)
diff_limit = 100
region = (248, 788, 80, 23)
base_bin = cv2.threshold(base, 30, 255, cv2.THRESH_BINARY)[1]
ini = 'f1'

def tela_nova(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    screenshot = screenshot.astype(np.uint8)
    _, new_screenshot = cv2.threshold(screenshot, 30, 255, cv2.THRESH_BINARY)
    return new_screenshot

def diff(base_bin, tela_nova):
    numero = np.abs(base_bin - tela_nova)
    soma_dife = np.sum(numero)
    return soma_dife

def inicio(key):
    print(f"pressione f1 para iniciar")
    keyboard.wait(key)
    print("iniciando")


inicio(ini)

while True:
    tela_atual = tela_nova(region)
    resultado = diff(base_bin, tela_atual)
    
    
    if resultado > diff_limit:
        pyautogui.click(x = 292 ,y= 800 ,clicks=2)
        time.sleep(1)
        pyautogui.click(x = 160 ,y= 1064 )
        time.sleep(1)
        pyautogui.typewrite("sure, 1 sec")
        time.sleep(1)
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.press_and_release('t')
       
        print("pressione f1 para reiniciar")
        keyboard.wait(ini)
        print("reiniciando")
        
    
    time.sleep(3)
    print(resultado)

