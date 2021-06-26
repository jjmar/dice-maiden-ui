import tkinter as tk
from command import Command, Modifier, generate_roll_string
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
        roll = generate_roll_string(command, Modifier(False, False, 0, False))
        pyperclip.copy(roll)
        self.master.frames[OutputFrame].display_roll(roll)

        print(self.master.frames[ModifiersFrame].modifier.advantage.get())
        print(self.master.frames[ModifiersFrame].modifier.disadvantage.get())
        print(self.master.frames[ModifiersFrame].modifier.critical_hit.get())
        print(self.master.frames[ModifiersFrame].modifier.extra_modifer.get())


class ModifiersFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        self.modifier = Modifier(False, False, 0, False)
        self.generate_widgets()

    def generate_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        lbl_advantage = tk.Label(self, text='Advantage')
        lbl_disadvantage = tk.Label(self, text='Disadvantage')
        lbl_critical_hit = tk.Label(self, text='Critical Hit')
        lbl_modifiers = tk.Label(self, text='Extra Modifiers')


        self.modifier.advantage = tk.BooleanVar(self, value=False)
        self.modifier.disadvantage = tk.BooleanVar(self, value=False)
        self.modifier.critical_hit = tk.BooleanVar(self, value=False)
        self.modifier.extra_modifer = tk.IntVar(self, value=0)


        chk_advantage = tk.Checkbutton(self, text='Advantage', variable=self.modifier.advantage)
        chk_disadvantage = tk.Checkbutton(self, text='Disadvantage', variable=self.modifier.disadvantage)
        chk_critical_hit = tk.Checkbutton(self, text='Critical Hit', variable=self.modifier.critical_hit)

        frm_modifier = tk.Frame(self)
        lbl_modifier = tk.Label(frm_modifier, text='Extra Modifiers')
        scrl_modifier = tk.Scale(frm_modifier, from_=-20, to=20, orient=tk.HORIZONTAL,
                                 length=250, variable=self.modifier.extra_modifer)
        lbl_modifier.pack()
        scrl_modifier.pack(side=tk.LEFT, expand=True)

        # chk_advantage.pack(side=tk.LEFT)
        # chk_disadvantage.pack(side=tk.LEFT)
        # chk_critical_hit.pack(side=tk.LEFT)
        # scrl_extra_modifier.pack(side=tk.LEFT, fill=tk.BOTH)
        chk_advantage.grid(row=0, column=0, sticky='w')
        chk_disadvantage.grid(row=0, column=1, sticky='w')
        chk_critical_hit.grid(row=0, column=2, sticky='w')

        # scrl_modifier.grid(row=1, column=0)
        # lbl_modifier.grid(row=1, column=0, sticky='e')
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
