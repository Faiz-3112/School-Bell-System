# 🎓 School Bell System - CLI Version 🔔

This is the CLI-based implementation of the **School Bell System**, a Python application that manages the ringing of school bells according to a predefined schedule. The CLI version is designed for users who prefer a simple, command-line-based interface without the need for a graphical user interface (GUI).

## 📋 Features

- 🖥️ **Command-Line Interface**: Simple, lightweight operation using the command line.
- ⏲️ **Customizable Schedule**: Define periods, recess durations, and specify whether it’s a full or half-day schedule.
- 🔊 **Audio Alerts**: Plays different bell sounds for assembly, periods, and recess.
- 🕒 **Real-Time Monitoring**: Tracks and prints the current time and status of each period.

## 🛠️ Requirements

**To run the CLI-based version, you need the following dependencies:**

- Python 3.x
- `pygame` (for playing audio files)

Install the required Python libraries by running:

```
pip install pygame
```

## 📂 Project Structure
```
CLI/
├── assets/
│   ├── assembly call.mp3             # Assembly bell sound
│   ├── PERIOD BELL.mp3               # Period bell sound
│   ├── Old-alarm-clock-sound.mp3     # Optional old bell sound
├── School_bell_system_main.py        # Main Python script for the CLI version
├── School_bell_system_test.py        # Test script for running unit tests
└── README.md                         # This documentation file
```
## 🚀 How to Run

**Clone the repository:**

- First, clone the repository to your local machine:

```
git clone https://github.com/Faiz-3112/School-Bell-System.git
```
- Navigate to the CLI folder:
```
cd SchoolBellSystem/CLI_based_system
```
- Run the program:

- Execute the following command to start the CLI-based bell system:

```
python School_bell_system_main.py
```

- Follow the prompts:

    Enter whether it's a full day or half day.

The system will then run according to the school schedule and ring the appropriate bell sounds at the designated times.

## 💡 Usage Instructions
 - Full Day: The system follows a predefined schedule for a full school day (with 5 periods before recess and 4 after).
 - Half Day: The system will only ring bells for 4 periods before the half-day schedule concludes.
 - Bell Sounds: You can modify or replace the sound files used for assembly, period bells, and other alerts in the assets/ folder.
## 🕒 Schedule Customization
   The schedule for periods, recess, and assembly is defined in bell_schedule.json. You can modify this file to fit your school's timing and requirements. The JSON structure includes:

```
{
  "assembly": {
    "start_time": "07:00",
    "duration": 10
  },
  "periods": [
    {"start_time": "07:10", "duration": 40},
    {"start_time": "07:50", "duration": 40},
    {"start_time": "08:30", "duration": 40},
    {"start_time": "09:10", "duration": 40},
    {"start_time": "09:50", "duration": 40}
  ],
  "recess": {
    "start_time": "10:30", "duration": 20
  },
  "afternoon_periods": [
    {"start_time": "10:50", "duration": 40},
    {"start_time": "11:30", "duration": 40},
    {"start_time": "12:10", "duration": 40},
    {"start_time": "12:50", "duration": 40}
  ]
}
```
## 🔊 Audio Files

  - The system uses the following audio files, located in the assets/ folder:

      assembly call.mp3: Plays for the assembly bell.
      PERIOD BELL.mp3: Plays at the start of each period.
      Old-alarm-clock-sound.mp3: (Optional) An alternate sound that can be used for other alerts.
      You can replace these audio files with your own, as long as they are in .mp3 format and the paths in the Python script are updated accordingly.

## 📝 Logging
The system logs actions such as bell rings and schedule events to bell_system.log. This can be useful for tracking or debugging the bell system’s behavior over time.

## ⚙️ Customization
You can modify the schedule, audio files, and other configurations directly in the Python code or the bell_schedule.json file. The system is flexible and can be adapted to fit different school schedules and requirements.
