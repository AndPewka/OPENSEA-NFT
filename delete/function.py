from random import choice
import os
import re
import time
import sys
import pyperclip
from time import sleep

def change_count(count):
	with open("settings.txt", "r") as file:
		text = file.read()

	text = text.replace("count={}".format(str(count)),"count={}".format(str(count+1)))

	with open("settings.txt", "w") as file:
		file.write(text)
	print("count поменял")

def fun_break(pyautogui,password=None,count = 0):
	text = ""

########### Удаляем проблемную строку
	with open("list cards.txt","r") as file:
		line = file.readline()
		it = 0
		while len(line) != 0:
			line = file.readline()
			it += 1
			if count == it:
				continue
			text = text + line
	
	with open("list cards.txt","w") as file:
		file.write(text)
########
	script = os.getcwd() + "\\main.exe"

	pyautogui.hotkey('alt', 'f4')
	pyautogui.hotkey('alt', 'f4')
	os.system(f"start https://opensea.io/login?referrer=%2Faccount")
	sleep(3)
	pyautogui.hotkey('ctrl', 'r')
	sleep(3)
	click_button(pyautogui,"metamask.png",password)
	sleep(5)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.press("backspace")
	pyperclip.copy(password)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')
	os.system(script)
	sys.exit()

def click_button(pyautogui,file,password,last_count=0):
	file = "buttons\\" + file
	start_time = time.time()
	while pyautogui.locateOnScreen(file) == None:
		end_time=time.time()
		diff=int(end_time-start_time)
		print("click {} | {}".format(file,diff))
		if diff>=45:
			print("Программа сломалась на {}".format(last_count))
			change_count(int(last_count))
			fun_break(pyautogui,password,last_count)

	pyautogui.click(file)

def check_area(pyautogui,file,password,last_count=0):
	file = "buttons\\" + file
	start_time = time.time()
	while pyautogui.locateOnScreen(file) == None:
		end_time=time.time()
		diff=int(end_time-start_time)
		print("check area {} | {}".format(file,diff))
		if diff>=45:
			print("Программа сломалась на {}".format(last_count))
			change_count(int(last_count))
			fun_break(pyautogui,password,last_count)
	return True