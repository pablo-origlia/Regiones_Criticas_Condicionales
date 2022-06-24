import threading
import time
import logging
import contextlib

'''
    Implementación utilizando una función decorator y los recursos agrupados en una clase sin instanciar (variables de clase)
'''

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# Recurso
class recurso1():
    variable1 = 0
    variable2 = 0
    lock=threading.Lock()

# region id_region do
# begin
#       codigo
# end

def region(do):
    def wrapper():
        with recurso1.lock:
            logging.info(f'{recurso1.lock}, {recurso1.lock.locked()}')
            do()
        logging.info(f'{recurso1.lock}, {recurso1.lock.locked()}')
    return wrapper

@region
def incrementar_variable():
    recurso1.variable1 += 1

@region
def mostrar_variable():
    logging.info(f'variable1 = {recurso1.variable1}')

def funcion():
    for i in range(6):
        incrementar_variable()

hilos = []

for i in range(4):
    t = threading.Thread(target=funcion)
    t.start()
    hilos.append(t)

for k in hilos:
    k.join()

mostrar_variable()
print(recurso1.variable1, recurso1.variable2)