class Customer:

    def __init__(self, canvas, name):
        self.id_rectangle = None
        self.id_text = None
        self.name = name
        self.canvas = canvas
        self.state = True
        self.pos_x = 2
        self.pos_y = 228
        self.width = 20
        self.height = 20
        self.color = 'blue'

    def walk_to_the_entrance(self, env, waiting_queue):
        while True:
            self.delete()
            self.id_rectangle = self.canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.width, self.pos_y + self.height, fill=self.color)
            self.id_text = self.canvas.create_text(self.pos_x + 10, self.pos_y + 10, text=self.name, fill='white', font=('Helvetica 5 bold'))

            if self.pos_x == 234:
                break
            else:
                limit = 256 - (waiting_queue.index(self) + 1) * (self.width + 2)

                if self.pos_x < limit:
                    self.pos_x += 10

                    if self.pos_x >= limit:
                        self.pos_x = limit

                yield env.timeout(1)        
    
    def move_to_picture(self, env, data):
        limitx = data[1]
        limity = data[2]

        while True:
            self.delete()
            self.id_rectangle = self.canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.width, self.pos_y + self.height, fill=self.color)
            self.id_text = self.canvas.create_text(self.pos_x + 10, self.pos_y + 10, text=self.name, fill='white', font=('Helvetica 5 bold'))

            if data[0] == 'x+:y-':
                if self.pos_x < limitx:
                    self.pos_x += 10

                    if self.pos_x >= limitx:
                        self.pos_x = limitx
                elif self.pos_y > limity:
                    self.pos_y -= 10

                    if self.pos_y <= limity:
                        self.pos_y = limity
                else:
                    break
            elif data[0] == 'y-':
                if self.pos_y > limity:
                    self.pos_y -= 10

                    if self.pos_y <= limity:
                        self.pos_y = limity
                else:
                    break
            elif data[0] == 'x+':
                if self.pos_x < limitx:
                    self.pos_x += 10

                    if self.pos_x >= limitx:
                        self.pos_x = limitx
                else:
                    break
            elif data[0] == 'y+:x+':
                if self.pos_y < limity:
                    self.pos_y += 10

                    if self.pos_y >= limity:
                        self.pos_y = limity
                elif self.pos_x < limitx:
                    self.pos_x += 10

                    if self.pos_x >= limitx:
                        self.pos_x = limitx
                else:
                    break
            elif data[0] == 'y+':
                if self.pos_y < limity:
                    self.pos_y += 10

                    if self.pos_y >= limity:
                        self.pos_y = limity
                else:
                    break
            elif data[0] == 'y-:x-':
                if self.pos_y > limity:
                    self.pos_y -= 10

                    if self.pos_y <= limity:
                        self.pos_y = limity
                elif self.pos_x > limitx:
                    self.pos_x -= 10

                    if self.pos_x <= limitx:
                        self.pos_x = limitx
                else:
                    break
            elif data[0] == 'x-':
                if self.pos_x > limitx:
                    self.pos_x -= 10

                    if self.pos_x <= limitx:
                        self.pos_x = limitx
                else:
                    break
            elif data[0] == 'x-:y+':
                if self.pos_x > limitx:
                    self.pos_x -= 10

                    if self.pos_x <= limitx:
                        self.pos_x = limitx
                elif self.pos_y < limity:
                    self.pos_y += 10

                    if self.pos_y >= limity:
                        self.pos_y = limity
                else:
                    break

            yield env.timeout(1)
    
    def walk_to_the_exit(self, env):
        while True:
            self.delete()
            self.id_rectangle = self.canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.width, self.pos_y + self.height, fill=self.color)
            self.id_text = self.canvas.create_text(self.pos_x + 10, self.pos_y + 10, text=self.name, fill='white', font=('Helvetica 5 bold'))

            if self.pos_y > 264:
                self.pos_y -= 10
                
                if self.pos_y <= 264:
                    self.pos_y = 264
            elif self.pos_x > 2:
                self.pos_x -= 10
                
                if self.pos_x <= 2:
                    self.pos_x = 2
            else:
                self.delete()
                break

            yield env.timeout(1)

    def delete(self):
        self.canvas.delete(self.id_rectangle)
        self.canvas.delete(self.id_text)