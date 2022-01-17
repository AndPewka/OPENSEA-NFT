from random import choice
import os
def body_with_eye(body,eye):
	if eye[2:] == body:
		return 1
	else:
		return 0

def click_button(pyautogui,file):
	file = "buttons\\" + file
	while pyautogui.locateOnScreen(file) == None:
		pass
	pyautogui.click(file)

def check_area(pyautogui,file):
	file = "buttons\\" + file
	while pyautogui.locateOnScreen(file) == None:
		pass
	return True



def choice_card():
	locate_card = os.listdir(os.path.join("new_card"))
	i = 0
	massive = []
	while i < len(locate_card):
		if locate_card[i][0] == "+":
			massive.append(locate_card[i])
		i += 1
	if len(massive) != 0:
		target_card = choice(massive)
		os.rename("new_card\\" + target_card,"new_card\\" + target_card[1:])
		return target_card[1:]
	else:
		return False

	
	

def get_description(name):
	description = {}
	name = name.replace(".png", "")
	
	
	#ФОНЫ КАТАЛОГ -- 0
	word_1 = name[:name.find("$")]
	name = name[name.find("$")+1:]
	
	if word_1=="1":
		description["Background"] = "Sea foam"

	if word_1=="2":
		description["Background"] = "Violet"

	if word_1=="3":
		description["Background"] = "Calery"

	if word_1=="4":
		description["Background"] = "Peach"

	if word_1=="5":
		description["Background"] = "Coral"

	if word_1=="6":
		description["Background"] = "Banana"

	#ШЕРСТЬ КАТАЛОГ -- 1
	word_2 = name[:name.find("$")]
	name = name[name.find("$")+1:]
	
	if word_2=="1":
		description["Fur"] = "Purple" 

	if word_2=="2":
		description["Fur"] = "Blue"

	if word_2=="3":
		description["Fur"] = "Red "

	if word_2=="4":
		description["Fur"] = "Black"

	if word_2=="5":
		description["Fur"] = "Gray"

	if word_2=="6":
		description["Fur"] = "Brown"

	#ТЕЛО КАТАЛОГ -- 2
	word_3 = name[:name.find("$")]
	name = name[name.find("$")+1:]
		
	#ЭМОЦИЯ НА ГЛАЗАХ КАТАЛОГ -- 3
	word_4 = name[:name.find("$")][0]
	name = name[name.find("$")+1:]
	
	if word_4 == "1":
		description["Emotions"] = "Usual"

	if word_4 == "2":
		description["Emotions"] = "Stoned"

	if word_4 == "3":
		description["Emotions"] = "Angry"

	if word_4 == "4":
		description["Emotions"] = "Sad"

	#ПЛАСТЫРИ КАТАЛОГ -- 4
	word_5 = name[:name.find("$")][2:]
	name = name[name.find("$")+1:]
	
	if word_5 == "0":
		description["Plasters"] = "Without patches"

	if word_5 == "1" or word_5 == "2" or word_5 == "3" or word_5 == "4":
		description["Plasters"] = "One patch"

	if word_5 == "5" or word_5 == "9" or word_5 == "11" or word_5 == "12" or word_5 == "13" or word_5 == "14":
		description["Plasters"] = "Two patches"

	if word_5 == "6" or word_5 == "8":
		description["Plasters"] = "Three patches"

	if word_5 == "7":
		description["Plasters"] = "Four patches"

	#ОЧКИ КАТАЛОГ -- 5
	word_6 = name[:name.find("$")][2:]
	name = name[name.find("$")+1:]
	
	if word_6 == "0":
		description["Eyes wear"] = "Without eye wear"

	if word_6 == "1":
		description["Eyes wear"] = "Orange sport glasses"

	if word_6 == "2":
		description["Eyes wear"] = "Blue oval glasses"

	if word_6 == "3":
		description["Eyes wear"] = "Orange round glasses"

	if word_6 == "4":
		description["Eyes wear"] = "Yellow oval glasses"

	if word_6 == "5":
		description["Eyes wear"] = "Red wayfarer glasses"

	if word_6 == "6":
		description["Eyes wear"] = "Black polarized glasses"

	if word_6 == "7":
		description["Eyes wear"] = "Left eye band"

	if word_6 == "8":
		description["Eyes wear"] = "Right eye band"

	if word_6 == "9":
		description["Eyes wear"] = "Medical band"

	if word_6 == "11":
		description["Eyes wear"] = "Right eye pirate band"

	if word_6 == "13":
		description["Eyes wear"] = "Left eye pirate band"

	if word_6 == "14":
		description["Eyes wear"] = "Cyborg eye"

	#ШАПКИ КАТАЛОГ -- 6
	word_7 = name[:name.find("$")]
	name = name[name.find("$")+1:]
	
	if word_7 == "0_0":
		description["Headress"] = "Without headress"

	if word_7 == "1":
		description["Headress"] = "Pink happy octupus"

	if word_7 == "2":
		description["Headress"] = "Yellow happy octupus"

	if word_7 == "3":
		description["Headress"] = "Blue angry octupus"

	if word_7 == "4":
		description["Headress"] = "Red angry octupus"

	if word_7 == "5":
		description["Headress"] = "Devil horns"

	if word_7 == "6":
		description["Headress"] = "Nimbus"

	if word_7 == "7":
		description["Headress"] = "Panama hat"

	if word_7 == "8":
		description["Headress"] = "Top hat"

	if word_7 == "9":
		description["Headress"] = "Chef hat"

	#CЕРЬГИ КАТАЛОГ -- 7
	word_8 = name[:name.find("$")]
	name = name[name.find("$")+1:]
	
	if word_8 == "0_0":
		description["Earrings"] = "Without earrings"

	if word_8 == "1" or word_8 == "2":
		description["Earrings"] = "Golden single loop earring"

	if word_8 == "3":
		description["Earrings"] = "Golden double loop earrings"

	if word_8 == "4":
		description["Earrings"] = "Diamond stud earring"

	if word_8 == "5":
		description["Earrings"] = "Golden double loop & Diamond stud earring"

	#ОДЕЖДА КАТАЛОГ -- 8
	word_9 = name[:name.find("$")]
	name = name[name.find("$")+1:]
	
	if word_9 == "0_0":
		description["Clothes"] = "Naked"

	if word_9 == "1":
		description["Clothes"] = "Pandadas black training suit"

	if word_9 == "2":
		description["Clothes"] = "Pandadas red training suit"

	if word_9 == "3":
		description["Clothes"] = "White shirt"

	if word_9 == "4":
		description["Clothes"] = "Black shirt"

	if word_9 == "5":
		description["Clothes"] = "Black and White shirt"

	if word_9 == "6":
		description["Clothes"] = "Cream-Brown t-shirt"

	if word_9 == "7":
		description["Clothes"] = "Gray-Red t-shirt"

	if word_9 == "8":
		description["Clothes"] = "Mustand-Banana t-shirt"

	if word_9 == "9":
		description["Clothes"] = "Metallic texture shirt"

	if word_9 == "10":
		description["Clothes"] = "Blue texture shirt"

	if word_9 == "11":
		description["Clothes"] = "Brown texture shirt"

	if word_9 == "12":
		description["Clothes"] = "Venetian style shirt"

	if word_9 == "13":
		description["Clothes"] = "Yellow striped shirt"

	if word_9 == "14":
		description["Clothes"] = "Dark blue striped shirt"

	if word_9 == "15":
		description["Clothes"] = "Dark blue dotted shirt"

	if word_9 == "16":
		description["Clothes"] = "Banana-Blue dotted shirt"

	if word_9 == "17":
		description["Clothes"] = "Peach-Blue dotted shirt"

	if word_9 == "18":
		description["Clothes"] = "Coral-Blue dotted shirt"

	if word_9 == "19":
		description["Clothes"] = "Blue big-plaid shirt"

	if word_9 == "20":
		description["Clothes"] = "Yellow big-plaid shirt"

	if word_9 == "21":
		description["Clothes"] = "Yellow small-plaid shirt"

	if word_9 == "22":
		description["Clothes"] = "Red smoky shirt"

	if word_9 == "23":
		description["Clothes"] = "Blue smoky shirt"

	if word_9 == "24":
		description["Clothes"] = "Yellow smoky shirt"

	if word_9 == "25":
		description["Clothes"] = "Orange smoky shirt"

	if word_9 == "26":
		description["Clothes"] = "Gray-yellow smoky shirt"

	if word_9 == "27":
		description["Clothes"] = "Banana texture shirt"

	if word_9 == "28":
		description["Clothes"] = "Green woody shirt "

	if word_9 == "29":
		description["Clothes"] = "Toxic texture t-shirt"

	if word_9 == "30":
		description["Clothes"] = "Black smoky t-shirt"

	if word_9 == "31":
		description["Clothes"] = "Punk smoky t-shirt"

	if word_9 == "32":
		description["Clothes"] = "Camo t-shirt"

	if word_9 == "33":
		description["Clothes"] = "Light emerald t-shirt"

	if word_9 == "34":
		description["Clothes"] = "Green-blue smoky t-shirt"

	if word_9 == "35":
		description["Clothes"] = "Tiger t-shirt"

	if word_9 == "36":
		description["Clothes"] = "Yellow banana t-shirt"

	if word_9 == "37":
		description["Clothes"] = "Pink banana t-shirt"

	if word_9 == "38":
		description["Clothes"] = "Bloody t-shirt"

	if word_9 == "39":
		description["Clothes"] = "Hawaii t-shirt"



	#РОТ КАТАЛОГ -- 9
	word_10 = name 
	
	if word_10 == "1":
		description["Muzzle"] = "Usual"

	if word_10 == "2":
		description["Muzzle"] = "Opened"

	if word_10 == "3":
		description["Muzzle"] = "Tusks"

	if word_10 == "4":
		description["Muzzle"] = "Tongue"

	return description

