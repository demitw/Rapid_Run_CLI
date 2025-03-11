# Horse Racing Management System

## Overview
The **Horse Racing Management System** is a Python-based console application that allows users to manage horse details, conduct races, and visualize race results. The program enables users to add, update, and delete horse information, randomly select winners, and analyze race results using a text-based visualization.

## Features
- **Horse Management:**
  - Add horse details (ID, name, jockey, age, breed, races participated, wins, and group).
  - Update existing horse details.
  - Delete horse details (only before the race starts).
  - View horse details sorted by Horse ID.
  
- **Race Management:**
  - Randomly select four horses for the major race round.
  - Assign random race completion times to selected winners.
  - Display winners based on race completion times.
  - Save horse details to a text file.
  - Load previously saved horse details from a file.
  
- **Race Visualization:**
  - Text-based race completion time visualization using stars.
  - Display average race times of horses.

## Installation & Execution
### Requirements
- Python 3.x
- No external dependencies (only uses built-in Python modules)

### Running the Program
1. Clone or download the script.
2. Open a terminal or command prompt in the script's directory.
3. Run the script using:
   ```sh
   python horse_race.py
   ```
4. Follow the menu instructions to interact with the system.

## Usage
The application provides a menu for different actions:
- **AHD** – Add horse details
- **UHD** – Update horse details
- **DHD** – Delete horse details
- **VHD** – View registered horse details sorted by Horse ID
- **SHD** – Save horse details to a text file
- **LHD** – Load horse details from a text file
- **SDD** – Select four horses randomly for the major round
- **WHD** – Display winning horses’ details
- **VWH** – Visualize the time of the winning horses
- **ARH** – Display average race time of all horses
- **ESC** – Exit the program

## Data Storage
- Horse details are stored in memory while the program is running.
- A text file (`horse_details.txt`) is used to save and load horse details for future reference.

## Limitations
- Race results are randomly generated, and actual racing performance is not simulated.

## Future Improvements
- Implement a database for persistent storage.
- Add a graphical interface for better user interaction.
- Allow dynamic race simulations with animations.
- Incorporate historical race data analysis.

## Author
- Developed by:Demini Waidyanatha.

