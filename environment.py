class Environment:

    def __init__(self, canvas):
        self.canvas = canvas
        
    def draw(self):
        # cesped
        self.canvas.create_rectangle(0, 0, 512, 512, width=1, fill='#82E0AA')

        # camino w=256 h=64
        self.canvas.create_rectangle(0, 224, 256, 288, width=1, fill='#CA6F1E')

        # galeria de arte w=256 h=384
        self.canvas.create_rectangle(256, 64, 512, 448, width=1, fill='#E5E7E9')

        # cuadros izq w=10 h=30 espacio-pared=2 espacio-entre-cuadros=60
        self.canvas.create_rectangle(258, 194, 258 + 10, 194 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(258, 134, 258 + 10, 134 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(258, 74, 258 + 10, 74 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(258, 288, 258 + 10, 288 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(258, 348, 258 + 10, 348 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(258, 408, 258 + 10, 408 + 30, width=1, fill='#34495E')

        # cuadros arr w=30 h=10
        self.canvas.create_rectangle(304, 66, 304 + 30, 66 + 10, width=1, fill='#34495E')
        self.canvas.create_rectangle(364, 66, 364 + 30, 66 + 10, width=1, fill='#34495E')
        self.canvas.create_rectangle(424, 66, 424 + 30, 66 + 10, width=1, fill='#34495E')

        # cuadros abj w=30 h=10
        self.canvas.create_rectangle(304, 436, 304 + 30, 436 + 10, width=1, fill='#34495E')
        self.canvas.create_rectangle(364, 436, 364 + 30, 436 + 10, width=1, fill='#34495E')
        self.canvas.create_rectangle(424, 436, 424 + 30, 436 + 10, width=1, fill='#34495E')

        # cuadros der w=10 h=30
        self.canvas.create_rectangle(500, 194, 500 + 10, 194 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(500, 134, 500 + 10, 134 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(500, 74, 500 + 10, 74 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(500, 288, 500 + 10, 288 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(500, 348, 500 + 10, 348 + 30, width=1, fill='#34495E')
        self.canvas.create_rectangle(500, 408, 500 + 10, 408 + 30, width=1, fill='#34495E')

        