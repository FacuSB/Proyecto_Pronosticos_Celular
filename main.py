import pandas as pd
import requests
from tqdm import tqdm
from dotenv import load_dotenv
import os
import time
from twilio.rest import Client

def main():
	load_dotenv()
	API_KEY_WAPI = os.getenv("API_KEY_WAPI")
	PHONE_NUMBER = os.getenv("PHONE_NUMBER")
	TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
	TWILIO_SID = os.getenv("TWILIO_SID")
	MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

	place = "Corrientes, Corrientes"
	api_key = API_KEY_WAPI
	url_base = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={place}&days=1&aqi=no&alerts=no"
	response = requests.get(url_base).json()

	def getforecast(response, i):
		fecha = response["forecast"]["forecastday"][0]["hour"][i]["time"].split()[0]
		hora = int(response["forecast"]["forecastday"][0]["hour"][i]["time"].split()[1].split(":")[0])
		condicion = response["forecast"]["forecastday"][0]["hour"][i]["condition"]["text"]
		temp_c = response["forecast"]["forecastday"][0]["hour"][i]["temp_c"]
		rain = response["forecast"]["forecastday"][0]["hour"][i]["will_it_rain"]
		chance_rain = response["forecast"]["forecastday"][0]["hour"][i]["chance_of_rain"]
		return [fecha, hora, condicion, temp_c, rain, chance_rain]

	datos = []
	for i in tqdm(range(len(response["forecast"]["forecastday"][0]["hour"])), colour="red"):
		datos.append(getforecast(response, i))

	col = ["fecha", "hora", "condicion", "temp_c", "rain", "chance_rain"]
	Df = pd.DataFrame(datos, columns=col)

	df_rain = Df[(Df["rain"] == 1) | (Df["chance_rain"] > 50)]
	df_rain = df_rain[["hora", "condicion"]]
	df_rain.set_index("hora", inplace=True)

	if df_rain.empty:
		mensaje = (
			f"\nHola! \n\n\n El pronóstico de hoy {Df['fecha'][0]} en {place} indica que no hay horas con probabilidad de lluvia.\n\n\n Que tengas un buen día! :)"
		)
	else:
		mensaje = (
			f"\nHola! \n\n\n El pronóstico de hoy {Df['fecha'][0]} en {place} indica que hay:\n\n"
			f"{len(df_rain)} horas con probabilidad de lluvia:\n\n{df_rain.to_string()}\n\n\n Que tengas un buen día! :)"
		)

	time.sleep(2)
	client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
	log_lines = []
	log_lines.append(f"Enviando desde: {PHONE_NUMBER} a: {MY_PHONE_NUMBER}")
	log_lines.append(f"Mensaje: {mensaje}")
	print(log_lines[0])
	print(log_lines[1])
	try:
		message = client.messages.create(
			body=mensaje,
			from_=PHONE_NUMBER,
			to=MY_PHONE_NUMBER
		)
		log_lines.append("mensaje enviado " + message.sid)
		print(log_lines[-1])
	except Exception as e:
		log_lines.append(f"Error al enviar el mensaje: {e}")
		print(log_lines[-1])
	# Guardar todo en log.txt con timestamp
	with open("log.txt", "a", encoding="utf-8") as f:
		f.write("\n--- Ejecución: " + time.strftime("%Y-%m-%d %H:%M:%S") + " ---\n")
		for line in log_lines:
			f.write(line + "\n")

if __name__ == "__main__":
	main()