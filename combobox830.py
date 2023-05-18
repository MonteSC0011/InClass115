#
import tkinter as tk
from tkinter import ttk

#
def on_select(event):
    
    #Create an item object that obtains the value of the selected item. 
    selected_item = event.widget.get()
    print("Selected item:", selected_item)
  
#    
root = tk.Tk()
root.title("Monte is silly")

