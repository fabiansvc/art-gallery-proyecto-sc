# pip install simpy

from clock import Clock
from customer import Customer
import simpy, numpy as np, random, math

class Simulation():

    def __init__(self, canvas, result):
        # Datos de la simulación
        self.seed = 40 # Semilla generador
        self.max_capacity = 5  # Cantidad de clientes dentro de la galeria
        self.arrival_time = 300 # Tiempo (seg) en que llegan x cantidad de clientes
        self.customer_quantity = 10 # Cantidad de clientes en x cantidad de tiempo
        self.observation_time = 30 # Tiempo en que un cliente tarda en observar una pintura

        # Otros datos
        self.canvas = canvas
        self.result = result
        self.waiting_queue = []

    def tour_gallery(self, env, custumer):
        coord_tour = [
            ('x+:y-', 278, 199),
            ('y-', 0, 139),
            ('y-', 0, 79),
            ('x+', 263, 0),
            ('y+:x+', 309, 86),
            ('x+', 369, 0),
            ('x+', 429, 0),
            ('x+:y-', 470, 79),
            ('y+', 0, 139),
            ('y+', 0, 79),
            ('y+', 0, 293),
            ('y+', 0, 353),
            ('y+', 0, 413),
            ('y-:x-', 309, 406),
            ('x-', 369, 0),
            ('x-', 429, 0),
            ('x-:y+', 278, 413),
            ('y-', 0, 353),
            ('y-', 0, 293)
        ]
        
        start = env.now

        for coord in coord_tour:
            # Ditribución exponencial
            R = random.random() 
            t = -self.observation_time * math.log(R)
            yield env.process(custumer.move_to_picture(env, coord))
            yield env.timeout(t)

        self.messsage('\n%05.02f Cliente%s: termina el recorrido, duración %05.02f' % (env.now, custumer.name, env.now - start))

    def custumer(self, env, custumer, capacity):
        # Tiempo de llegada del cliente
        arrived = env.now

        with capacity.request() as request:  # Espera su turno
            yield env.process(custumer.walk_to_the_entrance(env, self.waiting_queue))  
            yield request  # Obtiene turno

            self.messsage('\n%05.02f Cliente%s: ingreso a la galeria, espero %05.02f' % (env.now, custumer.name, env.now - arrived))
           
            # Remueve al cliente de la cola de espera
            self.waiting_queue.remove(custumer)

            # Invoca al proceso del recorrido
            yield env.process(self.tour_gallery(env, custumer))

            self.messsage('\n%05.02f Cliente%s: sale de la galeria' % (env.now, custumer.name))
            env.process(custumer.walk_to_the_exit(env))

    def arrival_of_each_customer(self, env, min, max, n, capacity):
        for i in range(min, max):  # Para n clientes
            # Ditribución exponencial
            #R = random.random() 
            #t = (-self.arrival_time / n) * math.log(R)

            custumer = Customer(self.canvas, '%02d'%i)

            # Se añade el cliente a la cola
            self.waiting_queue.append(custumer)

            self.messsage('\n%05.02f Cliente%s: llegó a la galeria' % (env.now, custumer.name))

            # Invoca al proceso del cliente
            env.process(self.custumer(env, custumer, capacity))

            # Tiempo que tarda en llegar cada cliente
            yield env.timeout(5)

    def gallery(self, env, capacity):
        total = 0

        while True:
            # Distribución de poisson
            n = np.random.poisson(self.customer_quantity)

            self.messsage('\n%05.02f Llegará(n) %d cliente(s)' % (env.now, n))

            if n > 0:
                min = total + 1
                max = n + min
                total += n

                # Invoca al proceso de llegada de cada cliente
                env.process(self.arrival_of_each_customer(env, min, max, n, capacity))

            # Tiempo que tarda en llegar más clientes
            yield env.timeout(self.arrival_time)

    def clock(self, env):
        clock = Clock(self.canvas, 2, 2, 100, 20, 'white')
        clock.draw(0)

        while True:
            yield env.timeout(1)
            clock.tick(env.now)

    def start(self):
        self.waiting_queue.clear()
        self.messsage('Inicia la simulación')

        # se establece la semilla
        random.seed(self.seed)
        np.random.seed(self.seed)

        # Crea el objeto entorno de simulación
        env = simpy.rt.RealtimeEnvironment(strict=False)

        # Crea los recursos (Cantidad de clientes dentro de la galeria)
        res = simpy.Resource(env, self.max_capacity)

        # Invoca el proceso del reloj
        env.process(self.clock(env))

        # Invoca el proceso de la galeria
        env.process(self.gallery(env, res)) 

        # Inicia la simulación
        env.run()

    def messsage(self, text):
        self.result.configure(state='normal')
        self.result.insert('end', text)
        self.result.configure(state='disabled')