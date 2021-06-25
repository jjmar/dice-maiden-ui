import tkinter as tk
from command import Command
from functools import partial
import pyperclip


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

        self.frames = {}

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

        self.frames[CommandsFrame] = frm_commands
        self.frames[OptionsFrame] = frm_options
        self.frames[OutputFrame] = frm_output


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

            b = tk.Button(self, text=c.name, width=1, wraplength=100, command=partial(self.click_command, c))
            b.grid(column=column, row=row, sticky='nsew')

            column += 1

            if column >= self.MAX_COLUMNS:
                row += 1
                column = 0

    def click_command(self, command):
        roll = command.to_dice_maiden_roll()
        pyperclip.copy(roll)
        self.master.frames[OutputFrame].display_roll(roll)


class OptionsFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        pass


class OutputFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()
        self.after_id = None

    def display_roll(self, text):
        if self.after_id:
            self.statusbar.after_cancel(self.after_id)

        self.statusbar.config(text=text, fg='green')
        self.after_id = self.statusbar.after(5000, self.hide_roll)

    def hide_roll(self):
        self.after_id = None
        self.statusbar.config(text='')

    def generate_widgets(self):
        self.statusbar = tk.Label(self)
        self.statusbar.pack(expand=True, fill=tk.BOTH)
