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
    

