import tkinter as tk
from simulation import Simulation
top = tk.Tk()


class ArtGallery():
    def __init__(self, top):
        super().__init__()
        self.height = 512
        self.width = 512
        self.canvas = tk.Canvas(
            top, bg="white", height=self.height, width=self.width)
        self.canvas.pack()
        tk.Button(text="Start", command=self.start).pack()

    def draw(self):
        self.canvas.create_rectangle(2, 224, 256, 288, width=1, fill='white')
        self.canvas.create_rectangle(256, 2, 512, 512, width=1, fill='white')

        self.canvas.create_rectangle(280, 4, 344, 32, width=1, fill='red')
        self.canvas.create_rectangle(352, 4, 416, 32, width=1, fill='green')
        self.canvas.create_rectangle(424, 4, 488, 32, width=1, fill='yellow')

        self.canvas.create_rectangle(
            258, 52 + 24, 290, 116 + 24, width=1, fill='red')
        self.canvas.create_rectangle(
            258, 124 + 24, 290, 188 + 24, width=1, fill='red')
        self.canvas.create_rectangle(
            258, 268 + 24, 290, 332 + 24, width=1, fill='red')
        self.canvas.create_rectangle(
            258, 340 + 24, 290, 404 + 24, width=1, fill='red')

        self.canvas.create_rectangle(
            478, 52 + 24, 510, 116 + 24, width=1, fill='red')
        self.canvas.create_rectangle(
            478, 124 + 24, 510, 188 + 24, width=1, fill='red')
        self.canvas.create_rectangle(
            478, 196 + 24, 510, 260 + 24, width=1, fill='red')
        self.canvas.create_rectangle(
            478, 268 + 24, 510, 332 + 24, width=1, fill='red')
        self.canvas.create_rectangle(
            478, 340 + 24, 510, 404 + 24, width=1, fill='red')

        self.canvas.create_rectangle(280, 478, 344, 510, width=1, fill='red')
        self.canvas.create_rectangle(352, 478, 416, 510, width=1, fill='green')
        self.canvas.create_rectangle(
            424, 478, 488, 510, width=1, fill='yellow')

    def start(self):              
        def loop():
            simulation = Simulation()
            simulation.start()
        self.canvas.after(1000, loop) 
        
art_gallery = ArtGallery(top)
art_gallery.draw()

top.mainloop()
