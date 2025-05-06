Pacman Project
This project implements a Finite State Machine (FSM) to control ghost behavior in a Pacman-style game. 
It was developed by Jelinkova Tereza for the KOL304CR Games and AI module at Coventry University.

Features
- FSM states: chase, scatter, frightened and eaten
- Ghosts switch states based on timers, collisions and player actions
- Visual debugging using lines, logs, and markers to show AI decision-making
- Real-time behavior integrated into a working Pacman environment


Structure
- `fsm/` – AI state classes and logic
- `ghost.py/` - ghost code
- `pacman.py/` - pacman code
- `main.py/` - main game code
