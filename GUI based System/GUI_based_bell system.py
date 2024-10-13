import pygame
import time
import json
import os
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import logging

# Initialize logging
logging.basicConfig(filename='bell_system.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Initialize pygame for sound
pygame.mixer.init()

# Sound function with error handling
def play_sound(file):
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except pygame.error as e:
        logging.error(f"Error playing sound: {file} - {e}")
        messagebox.showerror("Error", f"Could not play the sound: {file}")

# Load schedule from JSON
def load_schedule():
    try:
        with open('bell_schedule.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Schedule configuration file not found.")
        messagebox.showerror("Error", "Configuration file not found. Please set up the schedule.")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        messagebox.showerror("Error", "Error reading configuration file.")
        return None

# Save schedule to JSON
def save_schedule(schedule):
    try:
        with open('bell_schedule.json', 'w') as f:
            json.dump(schedule, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving schedule: {e}")
        messagebox.showerror("Error", "Could not save the configuration file.")

# GUI for customization
def customize_schedule():
    def save_custom_schedule():
        try:
            assembly_time = assembly_entry.get()
            recess_time = recess_entry.get()
            full_day_periods = int(full_day_periods_entry.get())
            half_day_periods = int(half_day_periods_entry.get())
            period_duration = int(period_duration_entry.get())

            new_schedule = {
                "assembly_time": assembly_time,
                "recess_time": recess_time,
                "full_day_periods": full_day_periods,
                "half_day_periods": half_day_periods,
                "period_duration": period_duration
            }

            save_schedule(new_schedule)
            messagebox.showinfo("Saved", "Schedule saved successfully!")
            settings_window.destroy()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for periods and duration.")

    # Create customization window
    settings_window = tk.Toplevel()
    settings_window.title("Customize Schedule")

    tk.Label(settings_window, text="Assembly Time (HH:MM):").grid(row=0, column=0)
    assembly_entry = tk.Entry(settings_window)
    assembly_entry.grid(row=0, column=1)

    tk.Label(settings_window, text="Recess Time (HH:MM):").grid(row=1, column=0)
    recess_entry = tk.Entry(settings_window)
    recess_entry.grid(row=1, column=1)

    tk.Label(settings_window, text="Number of Full Day Periods:").grid(row=2, column=0)
    full_day_periods_entry = tk.Entry(settings_window)
    full_day_periods_entry.grid(row=2, column=1)

    tk.Label(settings_window, text="Number of Half Day Periods:").grid(row=3, column=0)
    half_day_periods_entry = tk.Entry(settings_window)
    half_day_periods_entry.grid(row=3, column=1)

    tk.Label(settings_window, text="Period Duration (in minutes):").grid(row=4, column=0)
    period_duration_entry = tk.Entry(settings_window)
    period_duration_entry.grid(row=4, column=1)

    tk.Button(settings_window, text="Save", command=save_custom_schedule).grid(row=5, column=1)

# Function to wait until the specified time
def wait_until(target_time):
    current = datetime.datetime.now().strftime("%H:%M")
    while current != target_time:
        current = datetime.datetime.now().strftime("%H:%M")
        print(f"Waiting for {target_time}... Current time: {current}")
        time.sleep(10)

# Main schedule handling
def run_schedule(is_half_day):
    schedule = load_schedule()
    if schedule is None:
        return

    period_duration = schedule.get("period_duration", 40)  # Default to 40 if missing
    assembly_time = schedule.get("assembly_time", "07:00")
    recess_time = schedule.get("recess_time", "10:30")
    full_day_periods = schedule.get("full_day_periods", 8)
    half_day_periods = schedule.get("half_day_periods", 4)

    wait_until(assembly_time)
    play_sound("assembly call.mp3")
    messagebox.showinfo("Assembly", "It's assembly time!")

    period_count = half_day_periods if is_half_day else full_day_periods

    for period in range(1, period_count + 1):
        for _ in range(period_duration):
            print(f"Period {period}, Current time: {datetime.datetime.now().strftime('%H:%M')}")
            time.sleep(60)  # Wait for 1 minute

        play_sound("PERIOD BELL.mp3")
        if period == half_day_periods and is_half_day:
            messagebox.showinfo("Half Day", "Half day is over!")
            break
        elif period == full_day_periods:
            messagebox.showinfo("Full Day", "Full day is over!")

    wait_until(recess_time)
    play_sound("assembly call.mp3")
    messagebox.showinfo("Recess", "It's recess time!")

# Main GUI window
def main():
    root = tk.Tk()
    root.title("School Bell System")

    tk.Label(root, text="School Bell System").pack(pady=10)

    tk.Button(root, text="Full Day", command=lambda: run_schedule(False)).pack(pady=5)
    tk.Button(root, text="Half Day", command=lambda: run_schedule(True)).pack(pady=5)
    tk.Button(root, text="Customize Schedule", command=customize_schedule).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
