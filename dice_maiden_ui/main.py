from gui import DiceMaidenApp
from configuration import get_config

import tkinter as tk

if __name__ == "__main__":
    config = get_config()

    root = tk.Tk()
    app = DiceMaidenApp(root, config)
    root.mainloop()
