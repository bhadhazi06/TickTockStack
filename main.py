import tkinter as tk
from orchestrator import Orchestrator


def update_clock():
    if orchestrator.timers:
        orchestrator.countdown()
        current = orchestrator.timers[orchestrator.current_timer]

        # Update the main time
        timer_label.config(text=current.get_time_str())
        # Update the name label to show which timer is active
        current_task_label.config(text=current.name)
    else:
        timer_label.config(text="00:00:00")
        current_task_label.config(text="No Timers Added")

    root.after(1000, update_clock)


def get_time_values():
    try:
        # Get the name from the new entry field
        timer_name = name_entry.get() or "Timer"

        h = int(hour_entry.get() or 0)
        m = int(min_entry.get() or 0)
        s = int(sec_entry.get() or 0)

        # Forward BOTH the time tuple and the name to the orchestrator
        orchestrator.add_timer(time=(h, m, s), name=timer_name)

        # Optional: Reset the name field for the next entry
        name_entry.delete(0, tk.END)
        name_entry.insert(0, "Timer")

    except ValueError:
        print("Please enter valid numbers for time!")

def start_timer():
    orchestrator.on = True

def pause_timer():
    orchestrator.on = False

def reset_timer():
    orchestrator.reset_timer()

orchestrator = Orchestrator()

root = tk.Tk()
root.title("Timer App")
root.geometry("300x500")
root.configure(pady=20)

# --- 1. Timer Display ---
# Using a large font for the main clock
current_task_label = tk.Label(root, text="Waiting...", font=("Helvetica", 14), fg="gray")
current_task_label.pack()

timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 40))
timer_label.pack(pady=40)

# --- 2. Control Buttons ---
# We create a frame to hold buttons horizontally
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Circular-style buttons (approximated with padding/width)
btn_reset = tk.Button(button_frame, text="↺", width=4, font=("Arial", 14), command=reset_timer)
btn_play  = tk.Button(button_frame, text="▶", width=4, font=("Arial", 14), command=start_timer)
btn_pause = tk.Button(button_frame, text="||", width=4, font=("Arial", 14), command=pause_timer)

# Placing them in a row
btn_reset.grid(row=0, column=0, padx=10)
btn_play.grid(row=0, column=1, padx=10)
btn_pause.grid(row=0, column=2, padx=10)

# --- 3. Input & Add Section (Updated) ---
# Container for the three input boxes
input_frame = tk.Frame(root)
input_frame.pack(pady=(40, 5))

# Common settings for the input boxes
entry_params = {"width": 3, "font": ("Helvetica", 18), "justify": 'center'}

# Hours
hour_entry = tk.Entry(input_frame, **entry_params)
hour_entry.insert(0, "0")
hour_entry.grid(row=0, column=0, padx=5)

# Separator Label (Optional, for visual clarity)
tk.Label(input_frame, text=":", font=("Helvetica", 18)).grid(row=0, column=1)

# Minutes
min_entry = tk.Entry(input_frame, **entry_params)
min_entry.insert(0, "0")
min_entry.grid(row=0, column=2, padx=5)

# Separator Label
tk.Label(input_frame, text=":", font=("Helvetica", 18)).grid(row=0, column=3)

# Seconds
sec_entry = tk.Entry(input_frame, **entry_params)
sec_entry.insert(0, "0")
sec_entry.grid(row=0, column=4, padx=5)

# --- New Name Input Section ---
name_label = tk.Label(root, text="Timer Name:")
name_label.pack(pady=(10, 0))

name_entry = tk.Entry(root, font=("Helvetica", 12), justify='center', width=20)
name_entry.insert(0, "Timer") # Default value as requested
name_entry.pack(pady=(0, 10))

# The Add Button stays below the frame
btn_add = tk.Button(root, text="ADD", width=10, command=get_time_values)
btn_add.pack(pady=10)

update_clock()

root.mainloop()