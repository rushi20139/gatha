import tkinter as tk
from tkinter import filedialog
import os, sys

# Set the TCL_LIBRARY explicitly using Tkinter
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
tcl_library = os.path.join(bundle_dir, 'tcl')
tk.Tcl().eval('set ::tcl_library {' + tcl_library + '}')

# Set file dialog initial directory
filedialog.Directory(initialdir=tcl_library)
def exit_app():
    root.destroy()

def main():
    global root
    # Create the main window
    root = tk.Tk()
    root.title("Full Screen App")

    # Full screen
    root.attributes("-fullscreen", True)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", command=exit_app)
    exit_button.pack(side="bottom", pady=20)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
