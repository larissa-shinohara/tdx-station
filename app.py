from flask import Flask, render_template
from datetime import datetime
import requests
import pytemperature

app = Flask(__name__)

API_KEY = "dbd7380d7d53474016c2b3e08d7c4e24"
cidade = "campinas"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']

@app.route("/")
def hello():
    date = datetime.now().strftime(format="%d/%m/%y")
    date1 = datetime.now().strftime(format="%H:%M:%S")
    date2 = datetime.now().strftime(format="%m/%d/%y")
    date3 = datetime.now().strftime(format="%I:%M:%S%p")
    temperature = (requisicao_dic['main']['temp'] - 273.15)
    temperaturec1 = round(temperature,1)
    temperaturec2 = str(temperaturec1)
    temperaturec3 = temperaturec2 + '°C'

    temperaturef1 = pytemperature.c2f(temperaturec1)
    temperaturef2 = round(temperaturef1,1)
    temperaturef3 = str(temperaturef2)
    temperaturef4 = temperaturef3 + '°F'

    return render_template('home.html', date=date, date1=date1, date2=date2, date3=date3, temperaturec3=temperaturec3, temperaturef4=temperaturef4)
