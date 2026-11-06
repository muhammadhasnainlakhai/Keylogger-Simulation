# Keylogger Simulation (Educational Purpose Only)

This project was developed as part of the Cyber Security Internship Month 1 tasks at Arch Technologies. 

## Objective
To simulate a basic keylogger in a controlled and safe environment to understand how keystroke logging works and to analyze the potential risks associated with it.

## Tools & Libraries
* Python
* Pynput Library (`pip install pynput`)

## How it Works
* The script uses `pynput.keyboard.Listener` to monitor keystrokes.
* Normal characters are written directly to `keylog.txt`.
* Special keys (like Space, Enter, Esc) are formatted and logged.
* Pressing the `Esc` key safely stops the program.

## Disclaimer
This script is strictly for educational purposes. It was created to understand endpoint security and keylogging mechanics. Do not use this on any device without explicit permission.


<img width="959" height="475" alt="Screenshot 2026-11-06 233252" src="https://github.com/user-attachments/assets/1b1ad655-1fed-41f6-a310-3833ac6db428" />
