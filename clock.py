class Clock:

    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.canvas = canvas
        self.time = None

    def draw(self, tag):    
        self.train = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
        self.tick(tag)

    def tick(self, tag):
        self.canvas.delete(self.time)
        self.time = self.canvas.create_text((self.x2 - self.x1) / 2 + self.x1, (self.y2 - self.y1) / 2 + self.y1, text=self.time_format(tag))
        self.canvas.update()

    def time_format(self, seconds):
        hours = int(seconds / 60 / 60)
        seconds -= hours * 60 * 60
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"