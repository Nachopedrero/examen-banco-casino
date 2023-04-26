import threading

class Cliente:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.saldo = 100
        self.lock = threading.Lock()
        self.num_ingresos_20 = 0
        self.num_ingresos_50 = 0
        self.num_ingresos_100 = 0
        self.num_retiros_20 = 0
        self.num_retiros_50 = 0
        self.num_retiros_100 = 0
    def ingresar_20(self):
        while self.num_ingresos_20 < 60:
            with self.lock:
                self.saldo += 20
                self.num_ingresos_20 += 1
    def ingresar_50(self):
        while self.num_ingresos_50 < 20:
            with self.lock:
                self.saldo += 50
                self.num_ingresos_50 += 1
    def ingresar_100(self):
        while self.num_ingresos_100 < 40:
            with self.lock:
                self.saldo += 100
                self.num_ingresos_100 += 1
    def retirar_20(self):
        while self.num_retiros_20 < 60:
            with self.lock:
                if self.saldo >= 20:
                    self.saldo -= 20
                    self.num_retiros_20 += 1
                    
        
    def retirar_50(self):
        while self.num_retiros_50 < 20:
            with self.lock:
                if self.saldo >= 50:
                    self.saldo -= 50
                    self.num_retiros_50 += 1
                   
        
    def retirar_100(self):
        while self.num_retiros_100 < 40:
            with self.lock:
                if self.saldo >= 100:
                    self.saldo -= 100
                    self.num_retiros_100 += 1
                  

# Crear un objeto de cliente
cliente = Cliente("ejemplo")

# Crear los hilos
hilo_ingreso_20 = threading.Thread(target=cliente.ingresar_20)
hilo_ingreso_50 = threading.Thread(target=cliente.ingresar_50)
hilo_ingreso_100 = threading.Thread(target=cliente.ingresar_100)
hilo_retiro_20 = threading.Thread(target=cliente.retirar_20)
hilo_retiro_50 = threading.Thread(target=cliente.retirar_50)
hilo_retiro_100 = threading.Thread(target=cliente.retirar_100)

# Iniciar los hilos
hilo_ingreso_20.start()
hilo_ingreso_50.start()
hilo_ingreso_100.start()
hilo_retiro_20.start()
hilo_retiro_50.start()
hilo_retiro_100.start()

# Esperar a que los hilos terminen
hilo_ingreso_20.join()
hilo_ingreso_50.join()
hilo_ingreso_100.join()
hilo_retiro_20.join()
hilo_retiro_50.join()
hilo_retiro_100.join()


print(cliente.saldo)