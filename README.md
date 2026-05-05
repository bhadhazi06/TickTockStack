![TickTockStack Icon](icon.ico)
#  TickTockStack
**TickTockStack** is a sleek, linear productivity timer designed to keep you focused. Built with a modern glassmorphic interface using `CustomTkinter`, it allows you to queue up tasks in a "stack," providing a clear visual flow of your session with real-time updates and intuitive navigation.

---

##  Quick Start

To get this project running locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/bhadhazi06/TickTockStack
cd ticktockstack
```
### 2. Install Dependencies
```bash
pip install customtkinter
```
### 3. Run the app
```bash
python main.py
```

## How to use
### 1. Build Your Stack
Set the Time: Enter the hours, minutes, and seconds in the input fields. You don't need to delete the zeros—just click and type!

Name the Task: Give your timer a label (e.g., "Deep Work" or "Coffee Break").

Add to Stack: Click + ADD TO STACK. Your task will appear in the queue box.

### 2. Manage the Flow
Start/Pause: Use the ▶ (Play) and || (Pause) buttons to control the active timer.

Reset: The ↺ button resets the current timer back to its original duration.

Navigate: Use ◀ Prev and Next ▶ to manually skip between tasks in your stack.

### 3. Automated Progression
Once a timer hits 00:00:00, the app will notify you and automatically move the "Active" pointer (▶) to the next task in the stack.

### 4. Clean Slate
Click CLEAR QUEUE at any time to wipe the stack and start fresh.

