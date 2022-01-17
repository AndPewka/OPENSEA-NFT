from time import sleep



while __name__ == "__main__":
	sleep()
	exec(open("initial_settings.txt").read()) ##беру все переменные их текстовика
	print(count_collection)
