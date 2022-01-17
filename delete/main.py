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
			card["url"] = card["url"].replace("assets","collection/cryptogangboys/asset")
			card["url"] = card["url"] + "/edit"
			print(card)

			sleep(delay)
			os.system("start {}".format(card["url"]))
			sleep(5)
			pyautogui.hotkey("pgdn")
			sleep(0.1)
			pyautogui.hotkey("pgdn")

			sleep(delay)
			click_button(pyautogui,"delete.png",password,count)
			sleep(delay)
			click_button(pyautogui,"delete_item.png",password,count)
			sleep(3)
			pyautogui.hotkey('ctrl', 'w')
			telegram_send_message("{} line was delete".format(count),token,persons)

			if count > 25000:
				count = 0

			change_count(count)
			count += 1
			


			line = file.readline()

	count = 0
	change_count(count)









