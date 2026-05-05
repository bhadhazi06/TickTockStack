import tkinter as tk
from orchestrator import Orchestrator

def update_clock():
    # 1. Tell the orchestrator to perform the logic
    # Check if there are actually timers to count down
    if orchestrator.timers:
        orchestrator.countdown()

        # 2. Update the label on the screen
        current = orchestrator.timers[orchestrator.current_timer]
        timer_label.config(text=current.get_time_str())

    # 3. Schedule this function to run again in 1 second (1000ms)
    root.after(1000, update_clock)


def get_time_values():
    try:
        # .get() retrieves the string; int() converts it to a number
        # We use or '0' to handle cases where the user deletes the default 0
        h = int(hour_entry.get() or 0)
        m = int(min_entry.get() or 0)
        s = int(sec_entry.get() or 0)

        orchestrator.add_timer(time = (h,m,s))
    except ValueError:
        # This triggers if someone types "abc" instead of a number
        print("Please enter valid numbers only!")
        return 0, 0, 0

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

# The Add Button stays below the frame
btn_add = tk.Button(root, text="ADD", width=10, command=get_time_values)
btn_add.pack(pady=10)

update_clock()

root.mainloop()