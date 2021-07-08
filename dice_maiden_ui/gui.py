import tkinter as tk
from tkinter import filedialog
from functools import partial

import pyperclip
import json
import jsonschema

from dice_maiden_ui.roll import generate_roll_string
from dice_maiden_ui.models import Modifiers
from dice_maiden_ui.configuration import validate_config_against_schema


class DiceMaidenApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.frames = {}
        self.commands = []
        self.current_modifiers = None
        self.configure_window()
        self.generate_initial_ui()

    def configure_window(self):
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky='nsew', padx='8', pady='8')

    def generate_initial_ui(self):
        btn_open = tk.Button(self, text='Open Character', command=self.open_file)
        btn_open.grid(row=0, column=0)

    def open_file(self):
        file = filedialog.askopenfile(title='Please select a dice maiden ui configuration file',
                                      filetypes=[('JSON File', ['.json'])])

        if not file:
            return

        try:
            config_json = json.load(file)
        except json.decoder.JSONDecodeError:
            tk.messagebox.showerror(title='Invalid JSON', message='JSON file is formatted incorrectly')
            return

        try:
            validate_config_against_schema(config_json)
        except jsonschema.ValidationError as e:
            tk.messagebox.showerror(title='Configuration file doesnt match schema', message=e.message)
            return

        self.commands = config_json['commands']
        self.current_modifiers = Modifiers(tk.BooleanVar(self), tk.BooleanVar(self), tk.IntVar(), tk.BooleanVar())
        self.generate_main_ui()

    def generate_main_ui(self):
        self.master.minsize(800, 400)

        frm_commands = CommandsFrame(self, text='Commands', padx='5', pady='5')
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

    def click_command(self, command):
        roll = generate_roll_string(command['num_dice'], command['num_dice_sides'], command['modifier'],
                                    self.current_modifiers.extra_modifier.get(),
                                    self.current_modifiers.advantage.get(),
                                    self.current_modifiers.disadvantage.get(),
                                    self.current_modifiers.critical_hit.get())

        pyperclip.copy(roll)

        self.frames[OutputFrame].display_roll(roll)
        self.current_modifiers.reset()


class CommandsFrame(tk.LabelFrame):
    MAX_COLUMNS = 6

    def __init__(self,  *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        row = 0
        column = 0

        for c in self.master.commands:
            self.grid_rowconfigure(row, weight=1)
            self.columnconfigure(column, weight=1)

            b = tk.Button(self, text=c['name'], width=1, wraplength=100, command=partial(self.master.click_command, c))
            b.grid(column=column, row=row, sticky='nsew')

            column += 1

            if column >= self.MAX_COLUMNS:
                row += 1
                column = 0


class ModifiersFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.generate_widgets()

    def generate_widgets(self):
        modifiers = self.master.current_modifiers

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        chk_advantage = tk.Checkbutton(self, text='Advantage', variable=modifiers.advantage)
        chk_disadvantage = tk.Checkbutton(self, text='Disadvantage', variable=modifiers.disadvantage)
        chk_critical_hit = tk.Checkbutton(self, text='Critical Hit', variable=modifiers.critical_hit)

        frm_modifier = tk.Frame(self)
        lbl_modifier = tk.Label(frm_modifier, text='Extra Modifiers')
        scale_modifier = tk.Scale(frm_modifier, from_=-20, to=20, orient=tk.HORIZONTAL,
                                  length=250, variable=modifiers.extra_modifier)
        lbl_modifier.pack()
        scale_modifier.pack(side=tk.LEFT, expand=True)

        chk_advantage.grid(row=0, column=0, sticky='w')
        chk_disadvantage.grid(row=0, column=1, sticky='w')
        chk_critical_hit.grid(row=0, column=2, sticky='w')

        frm_modifier.grid(row=0, column=3, sticky='nesw')


class OutputFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.lbl_output = None
        self.after_id = None
        self.generate_widgets()

    def generate_widgets(self):
        self.lbl_output = tk.Label(self)
        self.lbl_output.pack(expand=True, fill=tk.BOTH)

    def display_roll(self, text):
        if self.after_id:
            self.lbl_output.after_cancel(self.after_id)

        self.lbl_output.config(text=text, fg='green')
        self.after_id = self.lbl_output.after(5000, self.hide_roll)

    def hide_roll(self):
        self.after_id = None
        self.lbl_output.config(text='')
