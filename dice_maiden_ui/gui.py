import tkinter as tk
from tkinter import filedialog as fd
from command import Command, Modifier, generate_roll_string
from configuration import validate_config_against_schema
from functools import partial
import pyperclip
import json
import jsonschema


class DiceMaidenApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure_window()

    def configure_window(self):
        self.master.minsize(800, 400)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.generate_file_menu()
        self.grid(row=0, column=0, sticky='nsew', padx='8', pady='8')

    def open_file(self):
        file = fd.askopenfile(title='Please select a dice maiden ui configuration file',
                           filetypes=[('JSON File', ['.json'])])

        config_json = json.load(file)

        try:
            validate_config_against_schema(config_json)
        except jsonschema.ValidationError as e:
            tk.messagebox.showerror("Invalid Configuration", "Error - {}".format(e.message))

        self.generate_widgets(config_json)

    def generate_file_menu(self):
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar)
        file_menu.add_command(label='Open', command=self.open_file)
        menubar.add_cascade(label='File', menu=file_menu)
        self.master.config(menu=menubar)

    def generate_widgets(self, config):
        self.frames = {}

        frm_commands = CommandsFrame(self, config=config, text='Commands', padx='5', pady='5')
        frm_options = ModifiersFrame(self, text='Options')
        frm_output = OutputFrame(self, text='Output')

        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        frm_commands.grid(row=0, column=0, sticky='nsew')
        frm_options.grid(row=1, column=0, sticky="nsew")
        frm_output.grid(row=2, column=0, sticky='nsew')

        self.frames[CommandsFrame] = frm_commands
        self.frames[ModifiersFrame] = frm_options
        self.frames[OutputFrame] = frm_output


class CommandsFrame(tk.LabelFrame):
    MAX_COLUMNS = 6

    def __init__(self,  *args, **kwargs):
        config = kwargs.pop('config', None)
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets(config)

    def generate_widgets(self, config):
        commands = [Command(c) for c in config['commands']]

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
        modifier = self.master.frames[ModifiersFrame].modifier

        roll = generate_roll_string(command, modifier)
        pyperclip.copy(roll)
        self.master.frames[OutputFrame].display_roll(roll)

        modifier.reset()


class ModifiersFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.modifier = Modifier(tk.BooleanVar(self), tk.BooleanVar(self), tk.IntVar(), tk.BooleanVar())
        self.generate_widgets()

    def generate_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        chk_advantage = tk.Checkbutton(self, text='Advantage', variable=self.modifier.advantage)
        chk_disadvantage = tk.Checkbutton(self, text='Disadvantage', variable=self.modifier.disadvantage)
        chk_critical_hit = tk.Checkbutton(self, text='Critical Hit', variable=self.modifier.critical_hit)

        frm_modifier = tk.Frame(self)
        lbl_modifier = tk.Label(frm_modifier, text='Extra Modifiers')
        scrl_modifier = tk.Scale(frm_modifier, from_=-20, to=20, orient=tk.HORIZONTAL,
                                 length=250, variable=self.modifier.extra_modifier)
        lbl_modifier.pack()
        scrl_modifier.pack(side=tk.LEFT, expand=True)

        chk_advantage.grid(row=0, column=0, sticky='w')
        chk_disadvantage.grid(row=0, column=1, sticky='w')
        chk_critical_hit.grid(row=0, column=2, sticky='w')

        frm_modifier.grid(row=0, column=3, sticky='nesw')


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
