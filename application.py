from tkinter import *
from environment import Environment
from simulation import Simulation
import tkinter.scrolledtext as tkscrolled

class Application(Frame):

    def __init__(self, root):
        super().__init__(root)

        self.canvas = Canvas(self, bg='white', highlightthickness=1, highlightbackground='black', height=511, width=511)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.result = tkscrolled.ScrolledText(self, width=100, wrap='word',  bg="white", state=DISABLED)
        self.result.pack(side=RIGHT, fill=BOTH, expand=True)

        self.start_button = Button(text='Iniciar Simulación', command=self.start_simulation)
        self.start_button.pack(side=BOTTOM)

        self.environment = Environment(self.canvas)
        self.environment.draw()

        self.simulation = Simulation(self.canvas, self.result)

    def start_simulation(self):
        self.start_button.configure(text='Detener Simulación')
        self.simulation.start()

    def on_closing(self):
        self.master.destroy()