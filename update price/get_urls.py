import requests
import json


count = 50
url = "https://api.opensea.io/api/v1/assets"
querystring = {"order_direction":"desc","offset":"50","limit":"50","owner" : "0x93443125bf1c25d7d89a5a9aa8990133956da131"}

response = requests.request("GET", url, params=querystring)

while str(response) != "<Response [400]>":
  url = "https://api.opensea.io/api/v1/assets"
  querystring = {"order_direction":"desc", "offset":"{}".format(count),"limit":"50","owner" : "0x93443125bf1c25d7d89a5a9aa8990133956da131"}

  response = requests.request("GET", url, params=querystring)

  request = json.loads(response.text)

  exec(open("urls.txt").read()) ##беру все переменные их текстовика

  for i in range(50):
    try:
      url = request["assets"][i]["permalink"]
      price = str(float(request["assets"][i]["sell_orders"][-1]["current_bounty"]) / pow(10,16))
      nft_name = request["assets"][i]["name"]
      name = int(nft_name[1:])
      print(nft_name)
      # if name <= 10000:
      #   continue
    except:
      continue


    if url not in a:
      with open("list cards.txt","a") as file:
        word = r"card = {'url' : '{url}', 'price' : '{price}', 'name' : '{name}'}"
        word = word.replace(r"{url}",url)
        word = word.replace(r"{price}",price)
        word = word.replace(r"{name}",nft_name)
        file.write(word + "\n")

      a.append(url)

  print("{} / {}".format(len(a),count + 50))
  with open("urls.txt","w") as file:
    file.write("a = " + str(a))

  count += 50


