from function import *
import pyautogui
from time import sleep
import os
import pyperclip
from telegram import *
exec(open("settings.txt").read()) ##беру все переменные их текстовика

sleep(3)
while __name__ == "__main__":

	with open("list cards.txt", "r") as file:
		for i in range(count):
			line = file.readline()


		line = file.readline()
		card = {}

		while line:
			print(count)
			
			exec(line)
			card["url"] = card["url"] + "/sell"
			print(card)

			sleep(delay)
			os.system("start {}".format(card["url"]))
			sleep(delay)
			click_button(pyautogui,"amount.png",password,count)
			sleep(delay)
			pyperclip.copy(card["price"])
			pyautogui.hotkey('ctrl', 'v')
			sleep(delay)


			click_button(pyautogui,"post.png",password,count)
			sleep(delay)
			click_button(pyautogui,"sub.png",password,count)
			sleep(delay)
			click_button(pyautogui,"view.png",password,count)
			sleep(delay)
			pyautogui.hotkey('ctrl', 'w')
			telegram_send_message("{} line was resell".format(count),token,persons)

			if count > 25000:
				count = 0

			change_count(count)
			count += 1
			


			line = file.readline()

	count = 0
	change_count(count)









