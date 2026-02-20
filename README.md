Weather API – Raspberry Pi / MicroPython
Popis projektu

Tento skript se připojí k Wi-Fi síti, odešle HTTP požadavek na API služby OpenWeatherMap a vypíše aktuální meteorologická data pro Prahu (GPS souřadnice 50.0755, 14.4378).

Program získává:

    aktuální teplotu

    minimální a maximální teplotu

    průměrnou teplotu

    vlhkost vzduchu

    atmosférický tlak

Použité technologie

    Python / MicroPython

    requests

    network

    API služba OpenWeatherMap

API klíč

Pro správné fungování je nutné mít vlastní API klíč ze služby:

    https://openweathermap.org/

Po registraci vlož svůj klíč do proměnné:

    token = "TVŮJ_API_KLÍČ"


!!!Nikdy nesdílej svůj API klíč veřejně!!!
Doporučuje se použít .gitignore, aby se klíč nenahrál do repozitáře.

URL požadavek

Program používá následující endpoint:

    https://api.openweathermap.org/data/2.5/weather


Parametry:

    lat – zeměpisná šířka

    lon – zeměpisná délka

    units=metric – teplota v °C

    appid – API klíč

Spuštění programu

Uprav Wi-Fi údaje:

    ssid = 'NAZEV_SITE'
    password = 'HESLO'


Vlož vlastní API klíč.

Spusť skript:

    python main.py

Výstup programu

Příklad výstupu:

    temperature: 21.5 C
    avreage:     20.8 C
    humidity:    63 RH%
    pressure:    1012 hPa

Struktura získaných dat (JSON)

Program čte hodnoty z odpovědi:

    raw["main"]["temp"]
    raw["main"]["temp_max"]
    raw["main"]["temp_min"]
    raw["main"]["pressure"]
    raw["main"]["humidity"]

!Možné chyby!

    invalid request – špatný API klíč

    request failed – problém s internetem nebo připojením Wi-Fi

    Status code ≠ 200 – server odmítl požadavek

Možná rozšíření

    Zobrazení dat na LCD

    Odesílání dat přes MQTT

    Logování do souboru

    Automatické aktualizace v intervalu

    Přidání předpovědi počasí (/forecast endpoint)

Autor

Projekt vytvořen pro výuku práce s API, Git a GitHub.