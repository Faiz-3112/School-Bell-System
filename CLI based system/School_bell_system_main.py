import pygame
import time
import datetime

def sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    n = 1
    while n < 5:
        pygame.mixer.music.play()
        time.sleep(0.5)  # Adjusted to avoid playing all bells at once
        n += 1

# Custom schedule: Define period lengths and recess duration
SCHEDULE = {
    "assembly": {"start_time": "07:00", "duration": 10},  # Duration in minutes
    "periods": [
        {"start_time": "07:10", "duration": 40},
        {"start_time": "07:50", "duration": 40},
        {"start_time": "08:30", "duration": 40},
        {"start_time": "09:10", "duration": 40},
        {"start_time": "09:50", "duration": 40},  # Before recess
    ],
    "recess": {"start_time": "10:30", "duration": 20},
    "afternoon_periods": [
        {"start_time": "10:50", "duration": 40},
        {"start_time": "11:30", "duration": 40},
        {"start_time": "12:10", "duration": 40},
        {"start_time": "12:50", "duration": 40},
    ],
}

def get_user_input():
    print('WELCOME')
    print('ENTER WHETHER TODAY IS:')
    print("1 - FULL DAY     2 - HALF DAY ")
    user = int(input(''))
    return user

def current_time():
    return datetime.datetime.now().strftime("%H:%M")

def wait_until(target_time):
    # Keep checking the system clock until the target time is reached
    while current_time() != target_time:
        print(f"Waiting for {target_time}... Current time: {current_time()}")
        time.sleep(10)

def run_schedule(schedule, is_half_day):
    # Assembly
    wait_until(schedule["assembly"]["start_time"])
    print("Assembly time! Ringing the assembly bell.")
    sound("assembly call.mp3")

    # Morning periods
    for i, period in enumerate(schedule["periods"]):
        wait_until(period["start_time"])
        print(f"Period {i+1} begins. Ringing the period bell.")
        sound("PERIOD BELL.mp3")
        print(f"Period {i+1} ends at {current_time()}.")

        # Half day check: end after 4 periods
        if is_half_day and i == 3:
            print("Half day schedule is over. Students can go home.")
            sound("PERIOD BELL.mp3")
            return

    # Recess
    wait_until(schedule["recess"]["start_time"])
    print("Recess time! Ringing the recess bell.")
    sound("assembly call.mp3")
    print(f"Recess ends at {current_time()}.")

    # Afternoon periods (for full day)
    if not is_half_day:
        for j, period in enumerate(schedule["afternoon_periods"]):
            wait_until(period["start_time"])
            print(f"Period {j+6} begins. Ringing the period bell.")
            sound("PERIOD BELL.mp3")
            print(f"Period {j+6} ends at {current_time()}.")

    print("The school day is over. Time to go home!")
    sound("PERIOD BELL.mp3")


# Ask whether it's a full day or half day
user = get_user_input()

# Run the schedule based on the current time
run_schedule(SCHEDULE, is_half_day=(user == 2))
