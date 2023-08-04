import pyttsx3
import speech_recognition as sr
import pywhatkit
import pywhatkit as pwk
import webbrowser
import datetime
import wikipedia
import os
import requests



API_KEY = "0465bb616c5a3dfb2d02047eee12a5d8"


id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"    

def audio_texto():

    r = sr.Recognizer()
    
    with sr.Microphone() as origen:

        r.pause_threshold = 0.8

        print("ya puedes hablar")

        audio = r.listen(origen)

        try:
            pedido = r.recognize_google (audio, language= "es-ar")

            print ("dijiste:" + pedido)

            return pedido
        except sr.UnknownValueError:

                print ("modula qliao")

                return "sigo esperando"
        
        except:
                print ("modula qliao")

                return "sigo esperando"
        

def hablar(mensaje):
    engine = pyttsx3.init()
    engine.setProperty("voice", id1)

    engine.say(mensaje)
    engine.runAndWait()




def dia():
    dia = datetime.date.today()
    dia_semana = dia.weekday()

    calendario = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo",
    }

    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre",
    }

    numero_dia = dia.day
    numero_mes = dia.month
    nombre_dia = calendario[dia_semana]
    nombre_mes = meses[numero_mes]

    hablar(f"Hoy es {nombre_dia}, {numero_dia} de {nombre_mes}.")



def hora():
      
      hora = datetime.datetime.now()
      hora = (f"en este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos")
      print(hora)

      hablar(hora)

def obtener_clima(ciudad):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": ciudad,
        "appid": API_KEY,
        "lang": "es",
        "units": "metric"
    }
    respuesta = requests.get(base_url, params=parametros)
    datos_clima = respuesta.json()

    if datos_clima["cod"] == "404":
        return "No se encontró información del clima para esa ciudad."
    else:
        clima_desc = datos_clima["weather"][0]["description"]
        temp_actual = datos_clima["main"]["temp"]
        humedad = datos_clima["main"]["humidity"]
        viento = datos_clima["wind"]["speed"]

        mensaje_clima = f"El clima en {ciudad.capitalize()} es {clima_desc}. La temperatura actual es {temp_actual}°C. La humedad es {humedad}% y la velocidad del viento es {viento} km/h."

        return mensaje_clima

def saludo():
      
      hora = datetime.datetime.now()
      if hora.hour < 6  or hora.hour > 20:
            momento = "buenas noches"
      elif hora.hour >= 6  and hora.hour <13:
            momento = "buen día"
      else: momento = "buenas tardes"
      
      hablar(f"Hola jota, {momento}, ¿que necesitas?")

def spotify():
    if os.name == "nt":  # Windows
        os.system("start spotify:")



   
def activacion():
    while True:
        pedido = audio_texto().lower()

        if "hola l" in pedido:
            return True

def hacer_pedidos():
    if activacion():
        saludo()
    comenzar = True

   

    while comenzar:
            pedido = audio_texto().lower()

            if "gracias" in pedido:
                  hablar("no hay de que")

            if "abre youtube"  in pedido:
                  hablar("abriendo youtube")
                  webbrowser.open("https://www.youtube.com")
                  continue
            elif "abre el navegador" in pedido:
                  hablar("abriendo el navegador")
                  webbrowser.open("https://www.google.com/?hl=es")
                  continue
            elif "qué día es hoy" in pedido:
                  dia()
                  continue
            elif "qué hora es" in pedido:
                  hora()
                  continue
            elif "busca en wikipedia" in pedido:
                  hablar("iendo hermano")
                  pedido = pedido.replace("wikipedia", "")
                  wikipedia.set_lang("es")
                  resultado = wikipedia.summary(pedido, sentences = 1)
                  hablar("wikipedia dice lo siguiente")
                  hablar(resultado)
                  continue
            elif "busca" in pedido:
                  hablar("iendo hermano")
                  pedido = pedido.replace("busca", "")
                  pywhatkit.search(pedido)
                  hablar("esto es lo que he encontrado")
                  continue
            elif "abre whatsapp" in pedido:
                  webbrowser.open("https://web.whatsapp.com/")
                  continue
            elif "abre spotify" in pedido:
                  hablar("iendo hermano")
                  spotify()
                  continue
            elif "dame el clima de" in pedido:
                  ciudad = pedido.replace("dame el clima de", "").strip()
                  clima = obtener_clima(ciudad)
                  hablar(clima)
            elif "nos vemos" in pedido:
                  hablar("nos vemos hermano, cuidate")
                  break


                  
hacer_pedidos()