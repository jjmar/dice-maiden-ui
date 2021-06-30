import tkinter as tk

from gui import DiceMaidenApp


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceMaidenApp(root)
    root.mainloop()

# Code Refactoring Ideas

# 1) Remove as much logic out of gui classes
# 2) Investigate whether I can replace command/modifier classes with dicts or something
# 3) Throw dialog error if config file is invalid
