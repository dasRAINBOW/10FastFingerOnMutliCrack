import cv2
import mss
import numpy
import pytesseract
import pyautogui
from time import sleep

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
firstRun = True

def normMode():
    global firstRun
    sleep(3)
    left = pyautogui.locateOnScreen('urMum.png', confidence=0.8)[0]
    top = pyautogui.locateOnScreen('urMum.png', confidence=0.8)[1]
    left = left - 705
    top = top - 115
    mon = {'top': top, 'left': left, 'width': 930, 'height': 55}
    with mss.mss() as sct:
        while True:
            im = numpy.asarray(sct.grab(mon))

            text = pytesseract.image_to_string(im)
            if firstRun == True:
                textOld = text

            if text == textOld and firstRun == False:
                quit()

            pyautogui.typewrite(text + " ", 0.001)
            firstRun = False
            textOld = text

            cv2.imshow('Image', im)

input("Press Enter to start")

normMode()