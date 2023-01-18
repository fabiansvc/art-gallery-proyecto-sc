# pip install simpy

import simpy
import numpy as np
import random

class Simulation():
    def __init__(self):
        pass
        # Datos de la simulación
        self.SEMILLA = 42  # Semilla generador
        self.MAX_CAPACIDAD = 2  # Cantidad de clientes dentro de la galeria
        self.CANT_PROM_CLIENTES = 2  # Cantidad de clientes x cantidad de tiempo
        self.TIEMPO_SIMULACION = 100  # Duración de la simulación
        self.TIEMPO_LLEGADA = 10  # Tiempo en que llegan x cantidad de clientes
        # Tiempo en que un cliente tarda en recorrer la exposicón de la galeria
        self.TIEMPO_RECORRIDO = 5

    def recorrido_galeria(self, env, name):
        # Distribución exponencial
        tiempo = random.expovariate(1.0 / self.TIEMPO_RECORRIDO)
        yield env.timeout(tiempo)  # tiempo en que el cliente recorre la galeria
        print('%05.02f %s: Termina el recorrido, duración %05.02f' %
            (env.now, name, tiempo))


    def cliente(self, env, name, capacidad):
        llego = env.now  # tiempo de llegada del cliente
        print('%05.02f %s: Llega a la galeria' % (llego, name))

        with capacidad.request() as request:  # Espera su turno
            yield request  # Obtiene turno
            print('%05.02f %s: Ingresa a la galeria, espero %05.02f' %
                (env.now, name, env.now - llego))
            # Invoca al proceso del recorrido
            yield env.process(self.recorrido_galeria(env, name))
            print('%05.02f %s: Deja la galeria' % (env.now, name))


    def llegada_clientes(self, env, min, max, n, capacidad):
        for i in range(min, max):  # Para n clientes
            tiempo = random.uniform(0, self.TIEMPO_LLEGADA / n)  # Ditribución uniforme
            yield env.timeout(tiempo)  # Tiempo que tarda en llegar cada cliente
            # Invoca al proceso del cliente
            env.process(self.cliente(env, 'Cliente %02d' % i, capacidad))


    def principal(self, env, capacidad):
        total = 0

        while True:
            if env.now < 70:
                # Distribución de poisson
                n = np.random.poisson(self.CANT_PROM_CLIENTES)
                print('%05.02f Llegará(n) %d cliente(s)' % (env.now, n))

                if n > 0:
                    min = total + 1
                    max = n + min
                    total += n
                    # Invoca al proceso de llegada
                    env.process(self.llegada_clientes(env, min, max, n, capacidad))

            # Tiempo que tarda en llegar más clientes
            yield env.timeout(self.TIEMPO_LLEGADA)

            print("------------------- Bienvenido Simulación de una Galeria de Arte ------------------")

    def start(self):
        random.seed(self.SEMILLA)
        np.random.seed(self.SEMILLA)  # Cualquier valor
        # Crea el objeto entorno de simulación
        env = simpy.rt.RealtimeEnvironment(strict=False)
        # Crea los recursos (Cantidad de clientes dentro de la galeria)
        serv = simpy.Resource(env, self.MAX_CAPACIDAD)
        env.process(self.principal(env, serv))  # Invoca el proceso principal
        env.run(until=self.TIEMPO_SIMULACION)  # Inicia la simulación
