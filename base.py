import pyautogui
import cv2
import numpy as np
import time
import keyboard

base = cv2.imread('chat.PNG', cv2.IMREAD_GRAYSCALE)
if base is None:
    raise ValueError("Imagem não encontrada ou caminho inválido")

region = (245, 802, 79, 27)
base_int = base.astype(np.uint8)
base_bin = cv2.threshold(base_int, 30, 255, cv2.THRESH_BINARY)[1]

def tela_nova(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    screenshot = screenshot.astype(np.uint8)
    _, thresholded = cv2.threshold(screenshot, 30, 255, cv2.THRESH_BINARY)
    return thresholded

def diff(base_bin, tela_nova):
    numero = np.abs(base_bin - tela_nova)
    soma_dife = np.sum(numero)
    return soma_dife

threshold_limit = 100

ini = 'f1'

def inicio(key):
    print(f"pressione f1 para iniciar")
    keyboard.wait(key)
    print("iniciando")

inicio(ini)

while True:
    tela_atual = tela_nova(region)
    resultado = diff(base_bin, tela_atual)
    
    
    if resultado > threshold_limit:
        pyautogui.click(x = 287 ,y= 809 ,clicks=2)
        time.sleep(1)
        pyautogui.click(x = 293 ,y= 1058 )
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

