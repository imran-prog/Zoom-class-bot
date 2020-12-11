import pyautogui
import keyboard
import time
import bot

# Declairing main variable

def time_set():
    global id_num, hour, minute

    hour = time.strftime("%H")
    minute = time.strftime("%M")


    # conditions according to the time of meetings

    if (hour == "08" and minute == "30"):
        id_num = teacher_ids[0]
    elif (hour == "09" and minute == "15"):
        id_num = teacher_ids[1]
    elif (hour == "10" and minute == "00"):
        id_num = teacher_ids[2]
    elif (hour == "11" and minute == "10"):
        id_num = teacher_ids[3]
    elif (hour == "11" and minute == "55"):
        id_num = teacher_ids[4]
    elif (hour == "12" and minute == "40"):
        id_num = teacher_ids[5]
    elif (hour == "03" and minute == "34"):
        id_num = teacher_ids[4]

    return id_num

teacher_ids = [
    '749-382-7688', 
    '894 652 6523', 
    '828 528 9414', 
    '471 966 4984', 
    '590 547 4397', 
    '252 445 6829'
    ]

password = ['1234']

while (True):
    id_num = ""
    time_set()
    if (id_num != ""):
        zoom_control = mouse_control(id_num, password)
        time.sleep(2)
        zoom_control.opening_zoom_window()
        zoom_control.joining_class()
        time.sleep(60)
    else:
        time.sleep(60)
        continue