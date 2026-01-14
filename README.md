# Proyecto Pronósticos Celular

> Automatiza el pronóstico del tiempo y el envío de alertas diarias a tu celular usando WeatherAPI y Twilio.

---

## Cómo funciona

- El script principal (`main.py`) consulta el pronóstico diario para la ciudad configurada.
- Si hay probabilidad de lluvia, envía un mensaje SMS/WhatsApp a tu número usando Twilio.
- Todos los resultados de la ejecución se guardan en el archivo `log.txt` para su posterior revisión.

---

## Configuración Inicial en AWS EC2

Sigue estos pasos para preparar tu instancia de AWS EC2 (Ubuntu/Debian) y ejecutar el proyecto:

1. **Actualizar el sistema:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Instalar pip (gestor de paquetes de Python):**
   ```bash
   sudo apt install -y python3-pip
   ```
3. **Clonar y preparar archivos:**
   - Clona el repositorio donde guardaste los scripts necesarios:
     - `requirements.txt`
     - `main.py`
     - (y otros scripts auxiliares si los tienes)
4. **Instalar dependencias de Python:**
   ```bash
   pip3 install -r requirements.txt
   ```

---

## Automatización con Crontab

Este repositorio está diseñado para ejecutarse automáticamente todos los días usando `crontab` en una instancia EC2 de AWS.

1. Conéctate a tu instancia EC2.
2. Edita el crontab con el siguiente comando:
   ```bash
   crontab -e
   ```
3. Agrega la siguiente línea para ejecutar el script todos los días a las 8:00 AM:
   ```bash
   0 8 * * * cd /rutadelproyecto && /usr/bin/python3 main.py >> log.txt 2>&1
   ```
   > **Nota:** Cambia `/rutadelproyecto` por la ruta absoluta en tu servidor.

💡 para ver como se formatean los comandos en crontab [Crontab Guru](https://crontab.guru/)

---

## Variables de Entorno

Crea un archivo llamado `.env` en la raíz del proyecto con las siguientes credenciales:

```env
API_KEY_WAPI=tu_api_key_de_weatherapi
PHONE_NUMBER=numero_twilio
TWILIO_AUTH_TOKEN=tu_auth_token
TWILIO_SID=tu_sid
MY_PHONE_NUMBER=tu_numero_destino
```

---

## Requisitos y Recursos

### Librerías necesarias

- pandas
- requests
- beautifulsoup4
- tqdm
- python-dotenv
- twilio

Instálalas con:
```bash
pip3 install -r requirements.txt
```

### Enlaces Útiles

- [WeatherAPI](https://www.weatherapi.com/) — API Key de clima.
- [Twilio](https://www.twilio.com/) — Configura tu número de envío.
- [Crontab Guru](https://crontab.guru/) — Validador de expresiones cron.

---

## Archivo de Log

El archivo `log.txt` registra el estado de cada ejecución. Es la herramienta principal para monitorear que la automatización en la nube se esté realizando correctamente y diagnosticar posibles errores de conexión.