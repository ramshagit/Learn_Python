import requests
import json
#APIKEY="b6907d289e10d714a6e88b30761fae22"
print("Planning to do Weather related project")
#take input to enter the zip code
Zipcode = input("Enter Zipcode: ")
print("your zipcode is ",Zipcode)
Country = input("Country code: ")
print("your country is ",Country)
resp = requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+Zipcode+','+Country+'&appid=b64f437c3b7f1016e3df8a0f9df9f2df')
#resp = requests.get('https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22')
#resp = requests.get('api.openweathermap.org/data/2.5/weather?zip={'+Zipcode+'},{'+Country+'}')
print(resp.status_code)
#for todo_item in resp.json():
 #print('{} {}'.format(todo_item['id'], todo_item['summary']))
data = json.loads(resp.text)
print(data)
print("City is "+data['name'])
print("Current Condition is "+data['weather'][0]['description'])
print("sun rise "+ str(data['sys']['sunrise']))
#loaded_json = json.loads(json_data)
#for x in weather:
#	print("%s: %d" % (x, weather[x]))