#
import tkinter as tk
from tkinter import ttk


#
def on_select(event):
    
    selected_item = event.widget.get()
    print("Selected item:", selected_item)
    
#
root = tk.Tk()
root.title("Combobox Example")

#
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#
combo_box = ttk.Combobox(root, values=items)
combo_box.bind("<<ComboboxSelected>>", on_select)

    

