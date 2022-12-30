import tkinter as tk
from tinydb import TinyDB, Query, where
from tkinter import messagebox
import json

# Open the database
db = TinyDB('db.json')

# Define a query to select a specific row
Row = Query()

# Create the main window
window = tk.Tk()
window.title("HTTA Member Management")
window.geometry("600x400+300+200")
# Create a frame to hold the list of rows
frame = tk.Frame(window)
frame.pack()

# Create a scrollable list to display the rows
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)

listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# Populate the list with the rows from the database
for row in db.all():
    listbox.insert(tk.END, row)

# Create a delete button
def delete_row():
    # Get the index of the selected row
    index = listbox.curselection()[0]
    # Get the ID of the selected row
    row_id = listbox.get(index)
    #convert the row_id into a dictionary!
    row_dict = json.loads(row_id.replace("'",'"'))
    # Confirm that the user wants to delete the row
    confirm = tk.messagebox.askyesno("Delete row?", "Are you sure you want to delete this row?")
    if confirm:
        # get the key value to delete
        todel = row_dict.get('userid')
        # Delete the row from the database
        db.remove(where('userid')==todel)
        # Update the list
        listbox.delete(index)
#insert a delete button
button = tk.Button(window, text="Delete", command=delete_row)
button.pack()

# Create an input field and a button to add a new row
input_field = tk.Entry(window)
input_field.pack()

def add_row():
    # Get the data from the input field
    data = input_field.get()
    # Add the data as a new row in the database
    db.insert({'userid': data})
    # Clear the input field
    input_field.delete(0, tk.END)
    # Update the list
    listbox.insert(tk.END, {'userid': data})
# Add a member button
add_button = tk.Button(window, text="Add Member", command=add_row)
add_button.pack()
#Quit Button
quit_button = tk.Button(window, text="Quit", command=window.destroy)
quit_button.pack()

# Run the main loop
window.mainloop()
