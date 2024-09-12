import os
import customtkinter as ctk
from tkinter import messagebox

# Function to parse the input structure and return a list of directories and files
def parse_structure(input_string):
    structure = []
    lines = input_string.strip().split('\n')
    base_indent = None
    current_path = []

    for line in lines:
        stripped = line.lstrip('│├└─ ')
        indent = len(line) - len(stripped)

        if stripped.endswith('/'):
            # It's a directory
            if base_indent is None or indent < base_indent:
                base_indent = indent
            dir_name = stripped.rstrip('/')
            # Adjust current path based on indentation
            while len(current_path) > (indent - base_indent) // 4:
                current_path.pop()
            current_path.append(dir_name)
            structure.append(('/'.join(current_path), 'dir'))
        elif stripped != "":
            # It's a file
            file_name = stripped.split(' ')[0]
            structure.append(('/'.join(current_path + [file_name]), 'file'))

    return structure

# Function to create folders and files based on the parsed structure
def create_structure(structure, base_folder):
    try:
        for path, type_ in structure:
            full_path = os.path.join(base_folder, path)
            if type_ == 'dir':
                os.makedirs(full_path, exist_ok=True)
            elif type_ == 'file':
                with open(full_path, 'w') as file:
                    pass  # Create an empty file
        messagebox.showinfo("Success", f"Folder and file structure created in {base_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create structure: {e}")

# Function triggered when the user clicks the "Create Structure" button
def create_structure_from_input():
    input_structure = structure_input.get("1.0", ctk.END).strip()
    project_base_folder = path_input.get().strip()

    if not input_structure:
        messagebox.showwarning("Warning", "Please enter the folder/file structure.")
        return

    if not project_base_folder:
        messagebox.showwarning("Warning", "Please enter the full path to the project folder.")
        return

    parsed_structure = parse_structure(input_structure)
    create_structure(parsed_structure, project_base_folder)

# Setup CustomTkinter window
app = ctk.CTk()
app.title("Folder Structure Creator")
app.geometry("600x500")

# Folder Structure Input
structure_label = ctk.CTkLabel(app, text="Enter Folder/File Structure:")
structure_label.pack(pady=10)

structure_input = ctk.CTkTextbox(app, width=500, height=200)
structure_input.pack(pady=10)

# Project Folder Path Input
path_label = ctk.CTkLabel(app, text="Enter Full Path to Project Folder:")
path_label.pack(pady=10)

path_input = ctk.CTkEntry(app, width=500)
path_input.pack(pady=10)

# Button to Create Structure
create_button = ctk.CTkButton(app, text="Create Structure", command=create_structure_from_input)
create_button.pack(pady=20)

# Run the application
app.mainloop()
