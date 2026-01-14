
# Proyecto Pronósticos Celular

Este proyecto permite obtener el pronóstico del tiempo para una ciudad específica y enviar un mensaje diario a tu celular utilizando la API de WeatherAPI y Twilio.

## ¿Cómo funciona?
- El script principal (`main.py`) consulta el pronóstico del día para la ciudad configurada.
- Si hay probabilidad de lluvia, envía un mensaje SMS/WhatsApp a tu número usando Twilio.
- Todos los resultados de la ejecución se guardan en un archivo `log.txt` para su posterior revisión.

## Automatización con AWS EC2 y crontab
Este repositorio fue utilizado en una instancia EC2 de AWS para ejecutar el script automáticamente todos los días a una hora específica usando `crontab`.

### Ejemplo de configuración de crontab
1. Conéctate a tu instancia EC2.
2. Edita el crontab con:
	```sh
	crontab -e
	```
3. Agrega una línea como la siguiente para ejecutar el script todos los días a las 8:00 AM:
	```sh
	0 8 * * * cd /ruta/al/proyecto && /ruta/a/python3 main.py >> log.txt 2>&1
	```
	Cambia `/ruta/al/proyecto` y `/ruta/a/python3` según corresponda.

## Requisitos
- Python 3.x
- Las siguientes librerías (puedes instalar con `pip install -r requirements.txt`):
  - pandas
  - requests
  - beautifulsoup4
  - tqdm
  - python-dotenv
  - twilio

## Variables de entorno
Crea un archivo `.env` con las siguientes variables:
```
API_KEY_WAPI=tu_api_key_de_weatherapi
PHONE_NUMBER=numero_twilio
TWILIO_AUTH_TOKEN=tu_auth_token
TWILIO_SID=tu_sid
MY_PHONE_NUMBER=tu_numero_destino
```

## Archivo de log
El archivo `log.txt` almacena los resultados y posibles errores de cada ejecución del script para facilitar el monitoreo.

