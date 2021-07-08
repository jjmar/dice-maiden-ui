import tkinter as tk

from dice_maiden_ui.gui import DiceMaidenApp


def run():
    root = tk.Tk()
    DiceMaidenApp(root)
    root.mainloop()


if __name__ == "__main__":
    run()
