import time
import tkinter as tk
from tkinter import StringVar

def update_time():
    if running:
        global elapsed_time
        elapsed_time = time.time() - start_time
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        time_var.set(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_time)

def start_stopwatch():
    global start_time, running
    if not running:
        start_time = time.time() - elapsed_time
        running = True
        start_button.config(state="disabled")  # Disable start when running
        update_time()

def pause_stopwatch():
    global running
    running = False
    start_button.config(state="normal")  # Enable start button when paused

def reset_stopwatch():
    global start_time, elapsed_time, running
    running = False
    elapsed_time = 0
    time_var.set("00:00:00")
    start_button.config(state="normal")  # Enable start button on reset

# Initialize GUI
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x200")  # Set window size
root.resizable(False, False)  # Disable resizing

time_var = StringVar()
time_var.set("00:00:00")

# Time Display
time_label = tk.Label(root, textvariable=time_var, font=("Arial", 30), bg="black", fg="white")
time_label.pack(pady=20)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack()

# Buttons with Padding
start_button = tk.Button(button_frame, text="Start", command=start_stopwatch, width=8)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Pause", command=pause_stopwatch, width=8)
pause_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_stopwatch, width=8)
reset_button.grid(row=0, column=2, padx=5)

# Variables
start_time = 0
elapsed_time = 0
running = False

root.mainloop()
