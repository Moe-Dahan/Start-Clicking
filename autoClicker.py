import tkinter as tk
from pynput.mouse import Button, Controller
import time
from pynput import keyboard
import threading


running = False  # Global flag
# scans to scee if running still = False
def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        mouse = Controller()
        # Press and release
        mouse.press(Button.left)
        time.sleep(0.001)
        mouse.release(Button.left)
    # After 1 second, call scanning again (create a recursive loop)
    root.after(1, scanning)
# enable the the scan
def Start_Clicking():
    # Enable scanning by setting the global flag to True.
    global running
    running = True
def Stop_Clicking():
    # Stop scanning by setting the global flag to False.
    global running
    running = False
# the listner for f1 start and f2 stop keys
def on_release(key):
    if key == keyboard.Key.f1:
        Start_Clicking()
    elif key == keyboard.Key.f2:
        Stop_Clicking()
    if key == keyboard.Key.esc:
        # Stop listener
        return False
        
root = tk.Tk()
root.title('Start Clicking')
root.geometry('245x110')
root.config(bg='red')
root.iconbitmap("icons\\Iconsmind-Outline-Cursor-Click.ico")

autoClickerTitle = tk.Frame(root, bg='red')
autoLabel = tk.Label(autoClickerTitle, text="START CLICKING", font=("Comic Sans MS", 12, "bold"), bg='red', fg='white').grid(row=0, column=1, padx=45)
autoClickerTitle.place(x=0, y=0)

button_frame = tk.Frame(root, bg='red')
start_clicking = tk.Button(button_frame, text='Start Clicking (Press f1)', font=("Comic Sans MS", 10, "bold"), fg='white', bg='green', command=Start_Clicking, width=20).grid(row=0, column=1, padx=35)
stop_clicking = tk.Button(button_frame, text='Stop Clicking (Press f2)', font=("Comic Sans MS", 10, "bold"), fg='white', bg='red', command=Stop_Clicking, width=20).grid(row=1, column=1, padx=35)
button_frame.place(x=0, y=35)
root.after(1, scanning)

listener = keyboard.Listener(on_release=on_release)
listener.start()
while root.mainloop():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
    if root.destroy():
        on_release(key=keyboard.Key.esc)

