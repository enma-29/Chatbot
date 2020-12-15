import random
import requests as requests

#hola senior
url = "https://api.telegram.org/bot1405694549:AAFXfSbubq3dNsXLSisL_EV3vbtM5SnlU5M/"
#tomar el id del chat
def id_chat(update):
	chat_id = update["message"]["chat"]["id"]
	return chat_id

#toma el mensaje recibido
def nombre(update):
	nombre = update["first_name"]
	return  nombre

def mensaje(update):
	txt = update["message"]["text"]
	return  txt


#tomamos la ultima actualizacion
def ult_act(req):
	response = requests.get(req + "getUpdates")
	response = response.json()
	result = response["result"]
	total_act = len(result) - 1
	return result[total_act]
	
	#toma el ultimo archivo de mensaje actualizado

#enviar mensaje
def send_msj(chat_id, txt):
	prm ={"chat_id": chat_id, "text": txt}
	response = requests.post(url + "sendMessage", data=prm)
	return response

def nombre(update):
	nombre = update["message"]["from"]["last_name"]
	return nombre

#funcion main
def main():
	menu = "\n\nMenu:\n1\n2\n3\n4"
	update_id = ult_act(url)["update_id"]

	while True:
		update = ult_act(url)

		if update_id == update["update_id"]:
			if mensaje(update).lower() == "hi" or mensaje(update).lower() == "hello":
				send_msj(id_chat(update),'Hola señor '+nombre(update)+', bienvenido a nuestro ChatBot\n'+menu)

			elif mensaje(update) == "1":
				bn = "Hola 1"
				send_msj(id_chat(update),
						bn + menu)
			elif mensaje(update) =="2":
				chiste = "Hola 2"
				send_msj(id_chat(update),chiste + menu)
			elif mensaje(update)=="3":
				alago = "Hola 3"
				send_msj(id_chat(update), alago + menu)
			elif mensaje(update) == "4":
				despedida = "Hola 4"
				send_msj(id_chat(update), despedida)
				update_id += 1
			else:
				send_msj(id_chat(update), "opcion no valida")
			update_id += 1

main()