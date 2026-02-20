import requests
import network
import time


ssid = 'MQTT3IT'
password = 'vyuka3ITmqtt'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)


token = "28df0c7072d5262a17a2c651ed2e4cb6" # Vyzaduje vlastni API klic

# URL adresa s parametry
url = f"https://api.openweathermap.org/data/2.5/weather?lat={50.0755}&lon={14.4378}&units=metric&appid={token}"


try:
    #print("Leoš Bezkočka")
    data = requests.get(url)
    if(data.status_code == 200):
        raw=data.json()
        print("raw data:\n",raw)
        print("======= Parsed data =======")
        temp = raw["main"]["temp"]
        temp_max = raw["main"]["temp_max"]
        temp_min = raw["main"]["temp_min"]
        pressure = raw["main"]["pressure"]
        humidity = raw["main"]["humidity"]
        
        
        print(f"temperature: {temp} C")
        print(f"avreage:     {(temp_max+temp_min)/2} C")
        print(f"humidity:    {humidity} RH%")
        print(f"pressure:    {pressure} hPa")
        
        
    else:
        print("invalid request")
except Exception as err:
    print("request failed: " + str(err))

time.sleep(5)
