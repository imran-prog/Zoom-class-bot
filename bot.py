import pyautogui
import keyboard
import time


class mouse_control:

    def __init__(self, teach_id, password):
        self.teacher_id = teach_id
        self.password = password

    @staticmethod
    def resolution():
        return pyautogui.size()

    # Resolution 1280 x 1024

    @staticmethod
    def opening_zoom_window():
        '''
        This Function has the followings steps:
        1. Minimize all the windows which are opened
        2. Goto the search bar in bottom left side in windows 10.
        3. The cursor will click on saerch bar and then search for Zoom app
        4. And the last step is to open the app.
        '''
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
        '''
        This function will enter the ID of teacher and password,
        and then press enter to get into the class
        '''
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
        pyautogui.typewrite(f'{self.password}')
        time.sleep(1)
        pyautogui.moveTo(652, 647, duration=0.5)
        pyautogui.click(652, 647)

    @staticmethod
    def joining_audio():
        '''
        This function is made to join the audio, but this function,
        is not joining the audio...
        '''
        time.sleep(30)
        pyautogui.moveTo(617, 463, duration=0.5)
        pyautogui.click(617, 463)
        time.sleep(3)
        pyautogui.moveTo(879, 360, duration=0.5)
        pyautogui.click(879, 360)
        time.sleep(3)

