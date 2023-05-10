import tkinter as tk
from tkinter import filedialog
import os

# Define the size of each portion in bytes
portion_size = 1024 * 1024 * 1024  # 1 GB

# Define the path to the output folder
output_folder = "C:/Users/HP-EliteBook/Downloads/Programs/passwords"

# Create the GUI window
root = tk.Tk()
root.withdraw()

# Prompt the user to select the input file
input_file_path = filedialog.askopenfilename(title="Select Password File", filetypes=(("Text Files", "*.txt"),))

# Loop through the input file in chunks of portion_size bytes
with open(input_file_path, "rb") as input_file:
    portion_number = 0
    while True:
        # Read a portion of the input file
        portion_data = input_file.read(portion_size)

        # Check if we've reached the end of the file
        if not portion_data:
            break

        # Write the portion to a file in the output folder
        portion_file_path = os.path.join(output_folder, f"passwords_{portion_number:04}.txt")
        with open(portion_file_path, "wb") as portion_file:
            portion_file.write(portion_data)

        portion_number += 1

# Notify the user that the operation is complete
tk.messagebox.showinfo(title="Operation Complete", message="The file has been split into portions and saved to the output folder.")
