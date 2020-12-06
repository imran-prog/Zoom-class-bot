import pyautogui
import keyboard
import time


class mouse_control:

    def __init__(self, teach_id):
        self.teacher_id = teach_id

    @staticmethod
    def resolution():
        return pyautogui.size()

    # Resolution 1280 x 1024

    @staticmethod
    def opening_zoom_window():
        keyboard.press_and_release('win + m')
        pyautogui.moveTo(181, 1023, duration=1)
        time.sleep(2)
        pyautogui.moveTo(162, 1005, duration=0.2)
        time.sleep(2)
        pyautogui.click(162, 1005)
        time.sleep(2)
        pyautogui.typewrite("zoom")
        time.sleep(2)
        pyautogui.moveTo(144, 504, duration=1)
        pyautogui.click(144, 504)
        time.sleep(8)

    def joining_class(self):
        time.sleep(2)
        pyautogui.moveTo(417, 444, duration=1)
        pyautogui.click(417, 444)
        time.sleep(2)
        pyautogui.moveTo(541, 471, duration=0.5)
        pyautogui.click(541, 471)
        pyautogui.typewrite(f'{self.teacher_id}')
        time.sleep(1)
        pyautogui.moveTo(667, 642, duration=0.5)
        pyautogui.click(667, 642)
        time.sleep(1)
        pyautogui.moveTo(535, 470, duration=0.5)
        pyautogui.click(535, 470)
        pyautogui.typewrite("1234")
        time.sleep(1)
        pyautogui.moveTo(652, 647, duration=0.5)
        pyautogui.click(652, 647)

teacher_ids = [
	'749-382-7688', 
	'894 652 6523', 
	'828 528 9414', 
	'471 966 4984', 
	'590 547 4397', 
	'252 445 6829'
	]

# Defininf time function



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

# Declairing main variable

while (True):
	id_num = ""
	time_set()
	if (id_num != ""):
		zoom_control = mouse_control(id_num)
		time.sleep(2)
		zoom_control.opening_zoom_window()
		zoom_control.joining_class()
		#time.sleep(60)
	else:
		#time.sleep(60)
		continue