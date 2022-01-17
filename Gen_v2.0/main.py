import random
import re
from function import *
from PIL import Image
from load import *
from datetime import datetime
import os
import sys

diff_properties = [] # здесь лежат все properties
#eval("list_{}['{}'] = {}".format(propertyies,name,chance)) здесь лежат все свойства картинки

sleep(3)

exec(open("initial_settings.txt").read()) ##беру все переменные их текстовика





telegram_send_message("Генерация началась...",token,persons)


print(" Загрузка nft на сайт - ({})\n".format(bool_load),
"Колличество nft для создания - ({})\n".format(count),
"Задержка для кликера на сайте - ({})\n".format(delay),
"Последняя загруженная nft на сайте - ({})\n".format(last_count),
"Колличество коллекций на сайте({})\n".format(count_collection),
"Порог редкости - ({})\n".format(rare_point),
"Цена 1 nft({})\n".format(default_price),
"Коэффиецент редкости - ({})\n".format(k))
#print("5 sec...")
print("Программа запущена...")


with open("prop_settings.txt","r") as file:
	line = file.readline()

	while line:
		if len(line) == 1:
			line = file.readline()
			continue

		if "Delete" in line or "#" in line:
			line = file.readline()
			continue

		propertyies = get_properties(line)

		if propertyies not in diff_properties:
			diff_properties.append(propertyies)
		#print("{} - {} - {} - {}".format(number,propertyies,name,chance))
		line = file.readline()



##сохраняем словари со всеми названиями png и их весами
for i in diff_properties:
	exec('list_{} = {}'.format(i,"{}"))
with open("prop_settings.txt","r") as file:
	line = file.readline()
	while line:
		if len(line) == 1:
			line = file.readline()
			continue

		if "Delete" in line or "#" in line:
			line = file.readline()
			#print(line)
			continue
		
		number = get_number(line)
		propertyies = get_properties(line)
		name = get_name(line)
		chance = get_chance(line)

		exec("list_{}['{}'] = {}".format(propertyies,name,chance))

		if propertyies not in diff_properties:
			diff_properties.append(propertyies)

		line = file.readline()


for prop_name in diff_properties:
	chance_rate = 0.0
	for i in eval("list_{}".format(prop_name)):
		chance_rate = chance_rate + eval("list_{}['{}']".format(prop_name,i))

	##обработка ошибки, если шанс одной проперти не равен 100
	if chance_rate != 100.0:
		print("В пропертис [{}] шанс выпадания не равен 100, шанс равен - {}/{}".format(prop_name,chance_rate,abs(100-chance_rate)))
		#input("Нажмите enter")
		#exit()

sleep(3)


it = 0
count_percent = 0

with open("card_rates.txt","a") as file:
	times = datetime.today()
	file.write(str(times) + "\n")


while it < count:
	start_time = time.time()
	req = telegram_get_message(token)
	print("telegramm message --> {}".format(req))
	if req == "start":
		load_properties = {}
		dir_card_name = ""

		for prop_name in diff_properties:# создаем словарь свойств для картинки
			

			selected = random.choices(list(eval("list_{}".format(prop_name)).keys()), weights=list(eval("list_{}".format(prop_name)).values()), k=1)[0]
			
			load_properties[prop_name] = selected
			dir_card_name = dir_card_name + selected + "$"


		dir_card_name = dir_card_name.replace(".png","") + ".png"
		locate_card = os.listdir(os.path.join("new_cards"))

		check_dir_prop(load_properties) # проверка на то что все свойства есть в виде png

		if dir_card_name not in locate_card:

			folder = "layers"
			main = Image.open("{}/empty.png".format(folder), 'r')

			try:
				for prop_name in load_properties:
					card = Image.open("{}/{}/{}".format(folder,prop_name,load_properties[prop_name]), 'r')
					main.paste(card,(0,0),card)
			except:
				print("error in {} / {}".format(prop_name,load_properties[prop_name]))
				sys.exit()

			main.save("new_cards/" + dir_card_name, format="png") 
			
			list_rate = []
			list_rate = diff_properties.copy()

			#удаляю название property, которые не должны быть 
			with open("prop_settings.txt","r") as file:
				line = file.readline();line = file.readline()

				while line:
					if "Delete" in line:
						list_rate.remove(get_name(line)) # из списка рейтинга
						del load_properties[get_name(line)] # из словари разгрузки на сайт

					line = file.readline()

			it += 1 # колличество выгруженных картинок
			last_count += 1 # название картинки
			card_rate = 0  #общий рейтинг картинки на основе properties
			#print(diff_properties)
			for prop_name in list_rate:
				card_rate = card_rate + eval("list_{}['{}']".format(prop_name,load_properties[prop_name]))
			card_rate = card_rate / len(list_rate)
			price = default_price
			count_percent += card_rate

			with open("card_rates.txt","a") as file:
				word = "   ------   "
				if card_rate <= rare_point:
					word = "   -RARE-   "
					price = str(float(default_price) * k * (1 + (rare_point-card_rate)/100) * (1 + 10/rare_point))
					price = price[0:5]

				if k == 0.9:
					price = default_price

				file.write("{}    -    {}    -    {}    -    {}%   -    {}\n".format(last_count,price,word,card_rate,dir_card_name))

			if bool_load == "yes":
				try:
					load(delay,dir_card_name,load_properties,last_count,count,count_collection,price,persons,token,password,give_price,script,start_word) ### загрузка cards
				except:
					e = sys.exc_info()[1]
					telegram_send_message("ERROR - {}".format(str(e)),token,persons)
					fun_break(pyautogui,password)
			print("{}/{}".format(it,count))

pyautogui.alert('Cards was loaded')