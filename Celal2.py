import tkinter as tk
import time
import pynput
import threading
from PIL import ImageGrab
import cv2
import numpy as np

keyboard = pynput.keyboard.Controller()
#func of Xp bot
def hold_space():
    while True:
        with keyboard.pressed(pynput.keyboard.Key.space):
            time.sleep(0.1)        
        if not running:
            break

def press_f4():
    while True:
        keyboard.press(pynput.keyboard.Key.f4)
        time.sleep(0.1)                                                 
        keyboard.release(pynput.keyboard.Key.f4)
        time.sleep(4)
      
        if running==False:
            break


#func of fishbot
def fast_fish_bot():
    keyboard.press(pynput.keyboard.Key.f4)
    time.sleep(0.1)                                                 
    keyboard.release(pynput.keyboard.Key.f4)
    time.sleep(0.1)
    keyboard.press(pynput.keyboard.Key.f3)
    time.sleep(0.1)                                                 
    keyboard.release(pynput.keyboard.Key.f3)
    while running:
        if check_for_screenshot():
            break
    time.sleep(0.5)
    while running:
        if not check_for_screenshot():
            time.sleep(3)
            keyboard.press(pynput.keyboard.Key.f3)
            time.sleep(0.1)
            keyboard.release(pynput.keyboard.Key.delete)
            time.sleep(0.5)
            while running:
                if check_for_screenshot():
                    break
            time.sleep(0.5)
        time.sleep(0.1)

template = cv2.imread('template_image.png')
x1,x2 =454,551
y1,y2 =243,332

def check_for_screenshot():
    img = ImageGrab.grab(bbox=(x1, y1, x2 , y2))
    result = cv2.matchTemplate(np.array(img), template, cv2.TM_CCOEFF_NORMED)
    if result.any:
        time.sleep(0.1)
        return True
    else:        
        time.sleep(0.1)
        return False


#GUI
def menu_button_click():
    fishing_button.pack_forget()
    A_button.pack_forget()
    B_button.pack_forget()
    basla_button.pack(pady=50, side="top", expand=False)
    start_button.pack_forget()
    finish_button.pack_forget()
    xp_bot_button.pack_forget()
    start_button_f.pack_forget()
    finish_button_f.pack_forget()
#First GUI screen
def basla_buttons():
    basla_button.pack_forget()
    xp_bot_button.pack()
    fishing_button.pack()
    A_button.pack()
    B_button.pack()
    menu_button.pack()

def xp_bot_buttons():
    start_button.pack()
    finish_button.pack()
    xp_bot_button.pack_forget()
    fishing_button.pack_forget()
    A_button.pack_forget()
    B_button.pack_forget()

def start_button_click():
    global running
    running = True
    start_button.config(background='blue')
    print("XP Botu Çalışmaya başladı!")
    space_thread = threading.Thread(target=hold_space)
    space_thread.start()
    four_thread = threading.Thread(target=press_f4)
    four_thread.start()

def stop_button_click():
    global running
    running = False
    finish_button.config(background='red')
    finish_button.update()
    time.sleep(0.5)
    finish_button.config(background=root.cget('bg'))
    finish_button.update()
    time.sleep(0.5)
    start_button.config(background=root.cget('bg'))
    start_button.update()
    print("XP Botu Durdu")

def fishing_buttons():
    xp_bot_button.pack_forget()
    fishing_button.pack_forget()
    A_button.pack_forget()
    B_button.pack_forget()
    start_button_f.pack()
    finish_button_f.pack()

def start_button_f_click():
    global running
    running= True
    start_button_f.config(background='blue')
    fish_thread = threading.Thread(target=fast_fish_bot)
    fish_thread.start
    print("Balıkçılık Botu Çalışmaya Başladı!")

def stop_button_f_click():
    global running
    running= False
    finish_button_f.config(background='red')
    finish_button_f.update()
    time.sleep(0.5)
    finish_button_f.config(background=root.cget('bg'))
    finish_button_f.update()
    time.sleep(0.5)
    start_button_f.config(background=root.cget('bg'))
    start_button_f.update()
    print("Balıkçılık Botu Durdu")

def a_button_click():
    print("A Butonuna Tıklandı")

def b_button_click():
    print("B Butonuna Tıklandı")

root = tk.Tk()
root.title("Celal2")
root.geometry("250x350")
#Exp botu çağırma
xp_bot_button= tk.Button(root,text="Örümcek Zindanı",height=4, width=30, command=xp_bot_buttons)
start_button = tk.Button(root, text="Çalıştır",height=4, width=30,  command=start_button_click)
finish_button = tk.Button(root, text="Durdur", height=4, width=30, command=stop_button_click)
#Balıkçılık botu çağırma
fishing_button = tk.Button(root,height=4, width=30,  text="Balıkçılık botu", command=fishing_buttons)
start_button_f=tk.Button(root, text="Çalıştır",height=4, width=30,  command=start_button_f_click)
finish_button_f =  tk.Button(root, text="Durdur", height=4, width=30, command=stop_button_f_click)
A_button = tk.Button(root, text="A",height=4, width=30, command=a_button_click)
B_button = tk.Button(root, text="B",height=4, width=30, command=b_button_click)
menu_button = tk.Button(root, text="Menü", command=menu_button_click)
menu_button.pack(side="bottom")
basla_button = tk.Button(root, text="Başla", height=4, width=30, command=basla_buttons)
basla_button.pack(pady=50, side="top", expand=True)
root.mainloop()