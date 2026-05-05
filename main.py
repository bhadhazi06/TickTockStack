import customtkinter as ctk
from tkinter import messagebox
from orchestrator import Orchestrator

# Standard CustomTkinter Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def update_clock():
    refresh_queue_display()
    if orchestrator.timers:
        orchestrator.countdown()
        current = orchestrator.timers[orchestrator.current_timer]

        # Update the main time and task labels
        timer_label.configure(text=current.get_time_str())
        current_task_label.configure(text=current.name.upper(), text_color="#3B8ED0")

        if current.done:
            pause_timer()
            current.done = False
            if orchestrator.current_timer + 1 < len(orchestrator.timers):
                orchestrator.current_timer += 1
                messagebox.showinfo("Timer done", f"{current.name} Done.")
            else:
                messagebox.showinfo("All timers done.", "All timers are done.")
                orchestrator.current_timer = 0
    else:
        timer_label.configure(text="00:00:00")
        current_task_label.configure(text="NO TIMERS ADDED", text_color="gray")

    root.after(1000, update_clock)


def full_reset():
    orchestrator.timers = []
    orchestrator.current_timer = 0
    orchestrator.on = False
    refresh_queue_display()


def get_time_values():
    try:
        timer_name = name_entry.get() or "Timer"
        h = int(hour_entry.get() or 0)
        m = int(min_entry.get() or 0)
        s = int(sec_entry.get() or 0)

        orchestrator.add_timer(time=(h, m, s), name=timer_name)

        # Reset name entry but keep the focus out of it
        name_entry.delete(0, 'end')
        name_entry.insert(0, "Timer")
        refresh_queue_display()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for time!")


def refresh_queue_display():
    queue_textbox.configure(state="normal")
    queue_textbox.delete("1.0", "end")

    for i, timer in enumerate(orchestrator.timers):
        prefix = "▶ " if i == orchestrator.current_timer else "  "
        status = "(Done)" if timer.done else timer.get_time_str()
        queue_textbox.insert("end", f"{prefix}{timer.name}: {status}\n")

    queue_textbox.configure(state="disabled")


def start_timer(): orchestrator.on = True


def pause_timer(): orchestrator.on = False


def reset_timer():
    orchestrator.reset_timer()
    refresh_queue_display()


def next_timer():
    if orchestrator.timers and orchestrator.current_timer < len(orchestrator.timers) - 1:
        orchestrator.current_timer += 1
        orchestrator.on = False
        orchestrator.reset_timer()
        refresh_queue_display()


def prev_timer():
    if orchestrator.timers and orchestrator.current_timer > 0:
        orchestrator.current_timer -= 1
        orchestrator.on = False
        orchestrator.reset_timer()
        refresh_queue_display()


# Initialize Logic
orchestrator = Orchestrator()

# --- UI Setup ---
root = ctk.CTk()
root.title("TickTockStack")
root.geometry("450x850")
root.resizable(False, False)

# 1. Header
current_task_label = ctk.CTkLabel(root, text="WAITING...", font=("Helvetica", 16, "bold"))
current_task_label.pack(pady=(40, 0))

timer_label = ctk.CTkLabel(root, text="00:00:00", font=("Helvetica", 70, "bold"))
timer_label.pack(pady=20)

# 2. Controls
button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.pack(pady=10)

btn_reset = ctk.CTkButton(button_frame, text="↺", width=60, font=("Arial", 20), command=reset_timer)
btn_reset.grid(row=0, column=0, padx=10)

btn_play = ctk.CTkButton(button_frame, text="▶", width=80, height=40, font=("Arial", 20), command=start_timer)
btn_play.grid(row=0, column=1, padx=10)

btn_pause = ctk.CTkButton(button_frame, text="||", width=60, font=("Arial", 20), command=pause_timer)
btn_pause.grid(row=0, column=2, padx=10)

# 3. Queue (The Stack)
ctk.CTkLabel(root, text="THE STACK", font=("Helvetica", 12, "bold"), text_color="gray").pack(pady=(20, 0))
queue_textbox = ctk.CTkTextbox(root, width=350, height=150, corner_radius=15, border_width=2)
queue_textbox.pack(pady=10)

# 4. Input Section
input_container = ctk.CTkFrame(root, corner_radius=20)
input_container.pack(pady=20, padx=40, fill="x")

input_row = ctk.CTkFrame(input_container, fg_color="transparent")
input_row.pack(pady=10)

# We use placeholder_text so we don't need the clear_entry function anymore!
entry_style = {"width": 50, "justify": "center", "font": ("Helvetica", 18)}
hour_entry = ctk.CTkEntry(input_row, placeholder_text="0", **entry_style)
hour_entry.grid(row=0, column=0, padx=5)
ctk.CTkLabel(input_row, text=":", font=("Helvetica", 18)).grid(row=0, column=1)
min_entry = ctk.CTkEntry(input_row, placeholder_text="0", **entry_style)
min_entry.grid(row=0, column=2, padx=5)
ctk.CTkLabel(input_row, text=":", font=("Helvetica", 18)).grid(row=0, column=3)
sec_entry = ctk.CTkEntry(input_row, placeholder_text="0", **entry_style)
sec_entry.grid(row=0, column=4, padx=5)

name_entry = ctk.CTkEntry(input_container, placeholder_text="Timer Name", width=200)
name_entry.pack(pady=(0, 10))

# 5. Global Actions
btn_add = ctk.CTkButton(root, text="+ ADD TO STACK", font=("Helvetica", 14, "bold"), command=get_time_values)
btn_add.pack(pady=5)

btn_clear = ctk.CTkButton(root, text="CLEAR QUEUE", fg_color="transparent", text_color="red", hover_color="#331111",
                          command=full_reset)
btn_clear.pack(pady=5)

# 6. Navigation
nav_frame = ctk.CTkFrame(root, fg_color="transparent")
nav_frame.pack(side="bottom", pady=30)

ctk.CTkButton(nav_frame, text="◀ Prev", width=100, command=prev_timer).grid(row=0, column=0, padx=10)
ctk.CTkButton(nav_frame, text="Next ▶", width=100, command=next_timer).grid(row=0, column=1, padx=10)

update_clock()
root.mainloop()