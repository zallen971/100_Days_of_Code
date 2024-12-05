import tkinter as tk
import json

# Initialize the notes list
notes = []

def add_note():
    note_text = note_entry.get("1.0", tk.END)
    notes.append(note_text)
    note_entry.delete("1.0", tk.END)
    update_notes_display()
    save_notes()  # Save notes after adding

def delete_note():
    selected_index = notes_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del notes[index]
        update_notes_display()
        save_notes()  # Save notes after deleting

def update_notes_display():
    notes_listbox.delete(0, tk.END)
    for note in notes:
        notes_listbox.insert(tk.END, note)

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            loaded_notes = json.load(f)
            notes.extend(loaded_notes)  # Append loaded notes to the existing list
            update_notes_display()
    except FileNotFoundError:
        pass  # File doesn't exist, start with an empty list

# Create the main window
window = tk.Tk()
window.title("Notepad")

# Create a frame to hold the note entry
note_entry_frame = tk.Frame(window, height=100)  # Adjust height as needed
note_entry_frame.pack(pady=5)

# Create a text box for adding notes
note_entry = tk.Text(note_entry_frame, width=75, height=5)  # Adjust height as needed
note_entry.pack(fill="x")

# Create a button to add notes
add_button = tk.Button(window, text="Add Note", command=add_note)
add_button.pack(pady=10)

# delete button for the notes
delete_note = tk.Button(window, text="Delete Note", command=delete_note)
delete_note.pack(pady=10)

# Create a listbox to display notes
notes_listbox = tk.Listbox(window, height=15, width=100)
notes_listbox.pack(pady=10)
notes_listbox.bind("<Double-1>", delete_note)  # Bind double-click to delete_note

# load notes on startup
load_notes()

window.mainloop()