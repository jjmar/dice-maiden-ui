import tkinter as tk
from command import Command


class DiceMaidenApp(tk.Frame):
    def __init__(self, root, config):
        tk.Frame.__init__(self, root)
        self.config = config
        self.commands = [Command(c) for c in config['commands']]
        self.configure_window()
        self.generate_widgets()

    def configure_window(self):
        self.master.minsize(800, 400)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    def generate_widgets(self):
        self.grid(row=0, column=0, sticky='nsew')

        frm_commands = CommandsFrame(self, text='Commands', padx='5', pady='5')
        frm_options = OptionsFrame(self, text='Options')
        frm_output = OutputFrame(self, text='Output')

        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        frm_commands.grid(row=0, column=0, sticky='nsew')
        frm_options.grid(row=1, column=0, sticky="nsew")
        frm_output.grid(row=2, column=0, sticky='nsew')


class CommandsFrame(tk.LabelFrame):
    MAX_COLUMNS = 6

    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        commands = self.master.commands

        row = 0
        column = 0

        for c in commands:
            self.grid_rowconfigure(row, weight=1)
            self.columnconfigure(column, weight=1)

            b = tk.Button(self, text=c.name, width=1)
            b.grid(column=column, row=row, sticky='nsew')

            column += 1

            if column >= self.MAX_COLUMNS:
                row += 1
                column = 0


class OptionsFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        test = tk.Label(self, text='Options')
        test.grid()


class OutputFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        test = tk.Label(self, text='Status')
        test.pack()