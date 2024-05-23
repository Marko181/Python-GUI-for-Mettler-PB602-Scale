# Seminar 3 AVMS: Mettler PB602 Scale

## Goals: 
- connect to the scale over RS232
- send commands using python
- read from the scale
- create GUI for 6 buttons
- add current temperature, pressure, humidity, date and time
- get measuring time of the scale
- count the number of weights on the scale

## Usage:
1. Connect Mettler PB602 scale with your PC
2. Download files: [tehtnica_GUI.py](tehtnica_GUI.py) and [state_mng.py](state_mng.py)
3. Install following python libraries:
   ```bash
   pip install nicegui
   
   pip install requests

   pip install serial
4. Run tehtnica_GUI.py
