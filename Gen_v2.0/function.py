from random import choice
import os
import re
import time
import sys
import pyperclip
from time import sleep


def change_last_count(last_count):
	with open("initial_settings.txt","r") as file:
		text = file.read()
		text = text.replace("last_count={}".format(last_count-1),"last_count={}".format(last_count))

	with open("initial_settings.txt","w") as file:
		file.write(text)

def fun_break(pyautogui,password):
	script = os.getcwd() + "\\main.exe"
	pyautogui.hotkey('alt', 'f4')
	pyautogui.hotkey('alt', 'f4')
	os.system(f"start https://opensea.io/collections")
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
	click_button(pyautogui,"banner.png",password)
	os.system(script)
	sys.exit()

def click_button(pyautogui,file,password=None,script=None):
	file = "buttons\\" + file
	start_time = time.time()
	while pyautogui.locateOnScreen(file) == None:
		end_time=time.time()
		diff=int(end_time-start_time)
		print("click {} | {}".format(file,diff))
		if diff>=60:
			fun_break(pyautogui,password)
	pyautogui.click(file)

def check_area(pyautogui,file,password,script,last_count=0):
	file = "buttons\\" + file
	start_time = time.time()
	while pyautogui.locateOnScreen(file) == None:
		end_time=time.time()
		diff=int(end_time-start_time)
		print("check area {} | {}".format(file,diff))
		if diff>=150:
			if file == "add_item.png":
				change_last_count(int(last_count))
			elif file == "view.png":
				change_last_count(int(last_count))
			fun_break(pyautogui,"initial_settings.txt",password,script)
	return True

def check_chance(chance_list):
	count = 0
	for i in chance_list:
		count += i

	if count == 100:
		return True
	else:
		return False

def create_name_card(count,it):
	count = str(count)
	for i in range(len(str(it))-len(count)):
		count = "0" + count
	count = "#" + count
	return count



def check_dir_prop(description):
	for prop_name in description:

		if not os.path.isdir("layers/" + prop_name):
			print("-{}- property does not have folder".format(prop_name))
			input()
			exit()

		
		locate_card = os.listdir(os.path.join("layers/" + prop_name))

		if description[prop_name] not in locate_card:
			print("-{}- property does not have layer -{}-".format(prop_name,description[prop_name]))
			input()
			exit()

	return True


def get_chance(word):
	result = str(re.findall(r"\$.*\$", word))
	result = result.replace(r"['$","")
	result = result.replace(r"$']","")
	return result

def get_name(word):
	result = str(re.findall(r"{.*}", word))
	result = result.replace(r"['{","")
	result = result.replace(r"}']","")
	return result

def get_properties(word):
	result = str(re.findall(r"\[.*\]", word))
	result = result.replace(r"['[","")
	result = result.replace(r"]']","")
	return result

def get_number(word):
	result = str(re.findall(r"\|.*\|", word))
	result = result.replace(r"['|","")
	result = result.replace(r"|']","")
	return result



