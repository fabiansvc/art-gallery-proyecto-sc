from tkinter import Tk
from application import Application

class Main:

    def __init__(self):
        root = Tk()
        root.title("Simulación de una Galeria de Arte")
        root.resizable(0, 0)
        root.geometry("1000x500")

        app = Application(root)
        app.pack(padx=2, pady=2)
        
        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        root.mainloop()

if __name__ == "__main__":
    Main()