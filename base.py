import pyautogui
from PIL import Image
import cv2
import numpy as np
import time
import keyboard
import pytesseract
from pushbullet import Pushbullet


base = cv2.imread('chat.PNG', cv2.IMREAD_GRAYSCALE)
diff_limit = 5000
region = (224, 792, 98, 35)
base_bin = cv2.threshold(base, 30, 255, cv2.THRESH_BINARY)[1]
ini = 'f1'
chat_txt= (5,833,451,222)
pb = Pushbullet(api_key="api key")


def textin(chat_txt):
    screenshot = pyautogui.screenshot(region = chat_txt)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    texto = str(pytesseract.image_to_string(screenshot)) 
    return texto
   
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

def enviar(title, body):
    pb.push_note(title,body)


def inicio(key):
    print(f"pressione f1 para iniciar")
    keyboard.wait(key)
    print("iniciando")

   


inicio(ini)

while True:
    tela_atual = tela_nova(region)
    resultado = diff(base_bin, tela_atual)
    
   
    if resultado > diff_limit:
        pyautogui.moveTo(x = 242 ,y= 810)
        pyautogui.click()
        pyautogui.mouseDown(); pyautogui.mouseUp()
        time.sleep(1)
         
        texto_capturado = textin(chat_txt)

        enviar("olha as platininha", texto_capturado)
        
       
        time.sleep(5)
        pyautogui.moveTo(x = 169 ,y= 1065 )
        pyautogui.mouseDown(); pyautogui.mouseUp()
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


