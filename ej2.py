import time
import random

class Casino:
    def __init__(self):
        self.saldo = 50000
        self.numero_actual = 10
    def tirar_bola(self):
        while True:
            time.sleep(3)  # Esperar 10 segundos
            numero = random.randint(0, 36)  # Generar un número aleatorio entre 0 y 36
            self.numero_actual = numero
            print(f"La bola cayó en el número {numero}")
            
casino = Casino()



class Jugadornums:
    def __init__(self):
        self.dinero = 1000

    def apostar(self, ):
        global casino
        numero = random.randint(0, 36)  # Generar un número aleatorio entre 0 y 36
        self.dinero -= 10  # Restar 10 euros al dinero del jugador por la apuesta
        if numero == casino.numero_actual:  # Si el número coincide con el de la bola
            dinero_ganado = 360  # El jugador gana 360 euros (36 veces la apuesta)
            self.dinero += dinero_ganado
            casino.saldo -= dinero_ganado  # Restar el dinero ganado al saldo del casino
            
        else:
            pass

        if self.dinero <= 0:
            print("El jugador de números se ha quedado sin dinero.")    


class JugadorPares:
    def __init__(self):
        self.dinero = 1000

    def apostar(self, ):
        global casino
        paridad = random.choice(["par", "impar"])  # Generar una paridad aleatoria
        self.dinero -= 10  # Restar 10 euros al dinero del jugador por la apuesta
        
        numero = casino.numero_actual  # Obtener el número de la bola
        if (paridad == "par" and numero % 2 == 0) or (paridad == "impar" and numero % 2 != 0):
            dinero_ganado = 20  # El jugador gana 20 euros (2 veces la apuesta)
            self.dinero += dinero_ganado
            casino.saldo -= dinero_ganado  # Restar el dinero ganado al saldo del casino
            
        else:
            pass

        if self.dinero <= 0:
            print("El jugador de números pares o impares se ha quedado sin dinero.")


class JugadorMartingala:
    def __init__(self):
        self.dinero = 1000
        self.apuesta = 10

    def apostar(self, ):
        global casino
        numero = random.randint(0, 36)
        self.dinero -= self.apuesta
        if numero == casino.numero_actual:
            dinero_ganado = 36 * self.apuesta
            self.dinero += dinero_ganado
            casino.saldo -= dinero_ganado
            self.apuesta = 10  # Si se gana, se vuelve a la apuesta inicial
        else:
            self.apuesta *= 2  # Si se pierde, se dobla la apuesta

        if self.dinero <= 0:
            print("El jugador de martingala se ha quedado sin dinero.")
from threading import Thread

# Creamos los jugadores
jugador1 = Jugadornums()
jugador2 = Jugadornums()
jugador3 = Jugadornums()
jugador4 = Jugadornums()

jugador_pares1 = JugadorPares()
jugador_pares2 = JugadorPares()
jugador_pares3 = JugadorPares()
jugador_pares4 = JugadorPares()

jugador_martingala1 = JugadorMartingala()
jugador_martingala2 = JugadorMartingala()
jugador_martingala3 = JugadorMartingala()
jugador_martingala4 = JugadorMartingala()

# Creamos los hilos
jugadores = [jugador1, jugador2, jugador3, jugador4]
jugadores_pares = [jugador_pares1, jugador_pares2, jugador_pares3, jugador_pares4]
jugadores_martingala = [jugador_martingala1, jugador_martingala2, jugador_martingala3, jugador_martingala4]

threads = []


def jugar_jugador(jugador):
    
    while jugador.dinero > 10:
        jugador.apostar()

def jugar_jugador_pares(jugador):
    
    while jugador.dinero > 10:
        jugador.apostar()

def jugar_jugador_martingala(jugador):
    
    while jugador.dinero > 10:
        jugador.apostar()

for jugador in jugadores:
    t = Thread(target=jugar_jugador, args=(jugador,))
    threads.append(t)
    t.start()

for jugador_pares in jugadores_pares:
    t = Thread(target=jugar_jugador_pares, args=(jugador_pares,))
    threads.append(t)
    t.start()

for jugador_martingala in jugadores_martingala:
    t = Thread(target=jugar_jugador_martingala, args=(jugador_martingala,))
    threads.append(t)
    t.start()


# Esperamos a que terminen los hilos
for t in threads:
    t.join()
