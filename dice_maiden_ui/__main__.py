import tkinter as tk

from dice_maiden_ui.gui import DiceMaidenApp


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceMaidenApp(root)
    root.mainloop()
