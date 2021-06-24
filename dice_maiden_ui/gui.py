import tkinter as tk


class DiceMaidenApp(tk.Frame):

    def __init__(self, master, config):
        tk.Frame.__init__(self, master)
        self.master = master
        self.config = config

        self.configure_gui()
        self.generate_widgets()

    def configure_gui(self):
        self.master.title('Dice Maiden UI')

    def generate_widgets(self):
        pass
