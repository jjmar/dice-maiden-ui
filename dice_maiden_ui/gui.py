import tkinter as tk


class DiceMaidenApp(tk.Frame):
    def __init__(self, root, config):
        tk.Frame.__init__(self, root)
        self.config = config
        self.configure_window()
        self.generate_widgets()

    def configure_window(self):
        self.master.minsize(800, 400)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky='nsew')

    def generate_widgets(self):
        bman = CommandsFrame(self, text='Commands')
        main = ModifiersFrame(self, text='Modifiers')
        third = OutputFrame(self, text='Output')

        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        bman.grid(row=0, column=0, sticky='nsew')
        main.grid(row=1, column=0, sticky="nsew")
        third.grid(row=2, column=0, sticky='nsew')


class CommandsFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        test = tk.Label(self, text='Commands', background='red')
        test.pack(expand=True, fill=tk.Y)


class ModifiersFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        test = tk.Label(self, text='Modifiers')
        test.grid()


class OutputFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        test = tk.Label(self, text='Status')
        test.pack()