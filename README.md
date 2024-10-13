# School Bell System

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg) 
![Pygame](https://img.shields.io/badge/pygame-2.0.0-orange.svg)

Welcome to the **School Bell System** project! This project is designed to help manage the school bell timings for both full and half days. It includes two versions: a Graphical User Interface (GUI) version and a Command Line Interface (CLI) version.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Contributing](#contributing)

## Features
- **GUI-based version**: Provides a user-friendly interface to manage bell timings.
- **CLI-based version**: Allows scheduling through command line input.
- **Customizable schedules**: Easily configure the bell timings and periods.
- **Audio notifications**: Plays audio alerts for assembly and periods.
- **Log tracking**: Records actions taken by the system for review.

## Installation
To run this project, ensure you have Python installed on your system. Follow these steps to set up the project:

1. Clone this repository:
   ```
   git clone https://github.com/Faiz-3112/school-bell-system.git
   cd school-bell-system
   ```
2. Install required dependencies:
   ```
   pip install pygame
   ```
3. Place your audio files in the assets directory.
   
# Usage
## GUI Version 
 - To run the GUI version, execute the following command:

    click this [GUI Based System](https://github.com/Faiz-3112/School-Bell-System/tree/7c71211ae38bf28cf4846b3f9dc85b25af54be97/GUI%20based%20System)

       python GUI/GUI_based_bell_system.py
## CLI Version 

 - To run the CLI version, execute the following command:

   click this [CLI_School_bell_system_main](https://github.com/Faiz-3112/School-Bell-System/blob/7c71211ae38bf28cf4846b3f9dc85b25af54be97/CLI%20based%20system)

       python School_bell_system_main.py
   
## Project Structure
```
.
├── CLI/
│   ├── School_bell_system_main.py        # Main Python script for the CLI version
│   ├── bell_schedule.json                # Configuration file for bell timings
│   ├── bell_system.log                   # Log file to track system actions
│   └── README.md                         # Documentation for the CLI version
└── GUI/
    ├── assets/
    │   ├── assembly call.mp3             # Assembly bell sound
    │   ├── PERIOD BELL.mp3               # Period bell sound
    │   └── Old-alarm-clock-sound.mp3     # Optional old bell sound
    ├── GUI_based_bell_system.py          # Main Python script for the GUI version
    └── README.md                         # Documentation for the GUI version
```
## License
**This project is licensed under the MIT License - see the [LICENSE](LICENSE) file in the root directory for details.**

## Contributing
**Contributions are welcome! If you have suggestions for improvements or features, please create an issue or submit a pull request.**
