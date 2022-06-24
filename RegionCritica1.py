import threading
import time
import logging
import contextlib

'''
    Implementación utilizando una función decorator y los recursos como variables globales
'''
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s',datefmt='%H:%M:%S',level=logging.INFO)

# Recursos como variables globales
variable1 = 0
variable2 = 0
lock = threading.Lock()

# region id_region do
# begin
#       codigo
# end

def region(do):
    global lock
    def wrapper():
        with lock:
            logging.info(f'{lock}, {lock.locked()}')
            do()
        logging.info(f'{lock}, {lock.locked()}')
    return wrapper

@region
def incrementar_variable():
    global variable1
    variable1 += 1

@region
def mostrar_variable():
    global variable1
    logging.info(f'variable1 = {variable1}')

def funcion():
    global variable1
    for i in range(5):
        incrementar_variable()

hilos = []

for i in range(4):
    t = threading.Thread(target=funcion)
    t.start()
    hilos.append(t)

for k in hilos:
    k.join()

mostrar_variable()