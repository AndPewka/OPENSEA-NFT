import pyautogui
from time import sleep
from function import *
from random import choice
import os
from telegram import *
import time
import pyperclip

def load():
	##SETTINGS
	pyautogui.FAILSAFE = False
	delay = 0


	name_card = choice_card()

	count = int(input("write count cards -- >"))
	start_time = time.time()
	iters = 0

	while name_card:

		iters += 1
		description = get_description(name_card)
		
		count += 1
		click_button(pyautogui,"add_item.png")
		sleep(1 * delay)
		click_button(pyautogui,"drop_file.png")
		sleep(1 * delay)

			#pyautogui.write(name_card)
		pyperclip.copy(name_card)
		pyautogui.hotkey('ctrl', 'v')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(str(count))


		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('tab')
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('enter')
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Background")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Background"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Fur")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Fur"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Emotions")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Emotions"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Plasters")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Plasters"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Eyes wear")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Eyes wear"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Headress")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Headress"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Earrings")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Earrings"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Clothes")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Clothes"])
		sleep(1 * delay)

		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write("Muzzle")
		sleep(1 * delay)
		pyautogui.press('tab')
		sleep(1 * delay)
		pyautogui.write(description["Muzzle"])
		sleep(1 * delay)

		sleep(1 * delay)
		pyautogui.press('tab')

		sleep(1 * delay)
		pyautogui.press('tab')

		sleep(1 * delay)
		pyautogui.press('enter')

		for i in range(17):
			sleep(1 * delay)
			pyautogui.press('tab')

		sleep(1 * delay)
		pyautogui.press('enter')

		sleep(1 * delay)
		click_button(pyautogui,"close.png")

		sleep(1 * delay)
		click_button(pyautogui,"sell.png")

		sleep(1 * delay)
		click_button(pyautogui,"amount.png")


		sleep(1 + delay)
		pyautogui.write('0.01')
		sleep(1 * delay)
		click_button(pyautogui,"post.png")
		sleep(1 * delay)
		click_button(pyautogui,"sub.png")
		sleep(1 * delay)
		click_button(pyautogui,"view.png")
		sleep(1 * delay)
		click_button(pyautogui,"back.png")
		telegram_send_message("{} was loaded".format(count))
		
		name_card = choice_card()


	times = "--- %s seconds ---" % (time.time() - start_time)
	pyautogui.alert('Cards was loaded' + "\n{}".format(times) + "\n {} cards was loaded".format(iters))

	#sleep(100)
	#pyautogui.doubleClick()
	#pyautogui.write('Hello world!')