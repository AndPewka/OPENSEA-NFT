from tkinter import *
from tkinter.ttk import Checkbutton
from main import *




def start():
	description = {}
	output["text"] = "Генерация началась"
	
	description["count"] = int(check_count_state.get())

	description["last_count"] = int(check_last_count_state.get())
	description["count_collection"] = int(check_count_collection_state.get())
	description["rare_point"] = int(check_rare_point_state.get())
	description["default_price"] = check_default_price_state.get()

	description["k"] = int(check_k_state.get())
	bool_load = check_test_load_state.get()
	
	main(bool_load,description)
	#тут функцию main пихать	





window = Tk()
window.title("Gen v1.0")
#window.geometry('500x300') 
header_label = Label(window, text="Генератор nft")

check_count_label=Label(window, text='Введите колличество nft для создания')
check_test_load_label=Label(window, text='Выгружать nft на сайт')
last_count_label = Label(window,text="Введите последнюю загруженную nft")
count_collection_label = Label(window,text="Введите колличество ваших коллекций")
rare_point_label = Label(window,text="Введите нижний порог редкости карт")
last_count_label = Label(window,text="Введите последнюю загруженную nft")
k_label = Label(window,text="Введите коэффиецент редкости(0.8 обычный)")
default_price_label = Label(window,text="Введите цену 1 nft")

button = Button(window, text="Start", command=start,width=50)
output = Label(window,text="123154")

output_state = StringVar()
check_count_state = StringVar()
check_test_load_state = BooleanVar()
check_last_count_state = StringVar()
check_count_collection_state = StringVar()
check_rare_point_state = StringVar()
check_default_price_state = StringVar()
check_k_state = StringVar()


count = Entry(window,textvariable = check_count_state)
check_test_load = Checkbutton(window, var=check_test_load_state)
last_count = Entry(window,textvariable = check_last_count_state)
count_collection = Entry(window,textvariable = check_count_collection_state)
rare_point = Entry(window,textvariable = check_rare_point_state)
default_price = Entry(window,textvariable = check_default_price_state)
k = Entry(window,textvariable = check_k_state)

check_test_load_state.set(True)







chk_state = BooleanVar()  

header_label.grid(column=0,row=0)
count.grid(column=0,row=1)
check_test_load.grid(column=0,row=2)
last_count.grid(column=0,row=3)
count_collection.grid(column=0, row=4)
rare_point.grid(column=0, row=5)
default_price.grid(column=0,row=6)
k.grid(column=0,row=7)
button.grid(column=0,row=8,columnspan=2)
output.grid(column=0,row=9,columnspan=2)


check_count_label.grid(column=1,row=1)
check_test_load_label.grid(column=1,row=2)
last_count_label.grid(column=1,row=3)
count_collection_label.grid(column=1,row=4)
rare_point_label.grid(column=1,row=5)
default_price_label.grid(column=1,row=6)
k_label.grid(column=1,row=7)

window.mainloop()



