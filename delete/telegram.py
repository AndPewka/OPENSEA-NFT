import requests
#def telegram_send_message(text,chat_id=["421697595","708173040"]):
def telegram_send_message(text,token,chat_id):
	for name_id in chat_id:
		method = "sendMessage"
		#token = "1944982692:AAEI8LTcmW5nAhH4obEkgWSiYdk3y1U24JM"   #Ваня
		#token = "1928890454:AAH2qGxtWbaqtmFhw1-QSwfgjVG3zgKi3vc"   #Стефан
		url = f"https://api.telegram.org/bot{token}/{method}"
		data = {"chat_id": name_id, "text": text}
		x = requests.post(url, data=data)



def telegram_get_message(token):
	url = f"https://api.telegram.org/bot{token}/getupdates?offset=-1"
	request = requests.get(url).json()
	#print(request)

	if request["result"]!=[]:
		ids = str(request["result"][-1]["message"]["from"]["id"])
		number = str(request["result"][-1]["update_id"])
		text = request["result"][-1]["message"]["text"]
		data = {
		"ids" : ids,
		"number" : number,
		"text" : text.lower()
		}
		return data["text"]
	else:
		return "start"





