from operator import truediv
from turtle import width
import pandas as pd 
import pyautogui as pg
import time 
import webbrowser as web

data = pd.read_csv("Lista_numeros_pesquisa.csv", sep=";")
data

#fazendo o envio
data_dict = data.to_dict('list')

leads = data_dict['WhatsApp']
messages = data_dict['msg']
combo = zip(leads,messages)
first = True
for lead, message in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('esc')
    time.sleep(5)
    pg.press('enter')
    time.sleep(10)
    pg.hotkey('ctrl', 'w')
