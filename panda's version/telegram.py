import requests
def telegram_send_message(text,chat_id=["708173040","378238003","512954483"]):
	for name_id in chat_id:
		method = "sendMessage"
		token = "1823379225:AAHrX2a1F9fl4JzvH8zT8cwXMSZ_uDEREMk"
		url = f"https://api.telegram.org/bot{token}/{method}"
		data = {"chat_id": name_id, "text": text}
		req = requests.post(url, data=data)

