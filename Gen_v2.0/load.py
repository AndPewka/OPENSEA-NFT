import pyautogui
from time import sleep
from function import *
from random import choice
import os
import time
from telegram import *
import pyperclip



def load(delay,dir_card_name,description,last_count,count,count_collection,price,persons,token,password,give_price,script,start_word=""):
	
	card_name = create_name_card(last_count,count)
	##SETTINGS

	pyautogui.FAILSAFE = False
	iters = 0

	iters += 1
		
	click_button(pyautogui,"add_item.png",password,script)
	click_button(pyautogui,"drop_file.png",password,script)
	sleep(0.5)
	pyperclip.copy(dir_card_name)
	pyautogui.hotkey('ctrl', 'v')
	#pyautogui.write(dir_card_name,interval=0.05)
	sleep(0.5)

	pyautogui.press('enter')
	sleep(delay)

	pyautogui.press('tab')
	sleep(delay)

	pyautogui.press('tab')
	sleep(delay)


	pyperclip.copy(start_word + card_name)
	pyautogui.hotkey('ctrl', 'v')
	#pyautogui.write(card_name,interval=0.05)
	sleep(delay)



	for i in range(count_collection+5):
		pyautogui.press('tab')
		sleep(delay)


	pyautogui.press('enter')
	sleep(delay)



	pyautogui.press('tab')
	sleep(delay)


	pyautogui.press('tab')
	sleep(delay)


	for i in range(len(description)-1):
		pyautogui.press('enter')
		sleep(delay)



	pyautogui.press('tab')
	sleep(delay)

	pyautogui.press('tab')
	sleep(delay)

	pyautogui.press('tab')
	sleep(delay)


	for prop_name in description:
		pyperclip.copy(prop_name)
		pyautogui.hotkey('ctrl', 'v')
		#pyautogui.write(prop_name,interval=0.05)
		sleep(delay)




		pyautogui.press('tab')
		sleep(delay)


		pyperclip.copy(description[prop_name].replace(".png",""))
		pyautogui.hotkey('ctrl', 'v')
		#pyautogui.write(description[prop_name].replace(".png",""),interval=0.05)
		sleep(delay)



		pyautogui.press('tab')
		sleep(delay)


	pyautogui.press('tab')
	sleep(delay)
	

	pyautogui.press('enter')
	sleep(delay)


	for i in range(len(description) + 8):
		pyautogui.press('tab')
		sleep(delay)

	pyautogui.press('enter')  # CREATE
	sleep(delay)


	click_button(pyautogui,"close.png",password,script)

	if give_price == "no":
		click_button(pyautogui,"back.png",password,script)
		if check_area(pyautogui,"add_item.png",password,script,last_count):
			change_last_count(int(last_count))
			telegram_send_message("{} was loaded".format(card_name),token,persons)
		return True

	click_button(pyautogui,"sell.png",password,script)
	sleep(delay)
	click_button(pyautogui,"amount.png",password,script)
	sleep(delay)
	pyperclip.copy(price)
	pyautogui.hotkey('ctrl', 'v')
	sleep(delay)



	click_button(pyautogui,"post.png",password,script)
	click_button(pyautogui,"sub.png",password,script)
	
	if check_area(pyautogui,"view.png",password,script,last_count):
		change_last_count(int(last_count))
		telegram_send_message("{} was loaded".format(card_name),token,persons)

	click_button(pyautogui,"view.png",password,script)
	click_button(pyautogui,"back.png",password,script)
	

	
