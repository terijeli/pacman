Pacman Project
This project implements a Finite State Machine (FSM) to control ghost behavior in a Pacman style game. 
It was developed by Jelinkova Tereza for the KOL304CR Games and AI module, Coventry University. Please note the video could not be uploaded here since it has over 25MB (GitHub limit) and can be found as the appendix material in Wiseflow.

Features
- FSM states: chase, scatter, frightened and eaten
- Ghosts switch states based on timers, collisions and player actions
- Visual debugging using lines, logs, and markers to show AI decision-making
- Real-time behavior integrated into a working Pacman environment

Ghost behavior changes based on FSM states:
  - 1. Chase: Ghost actively chases Pacman (red)
  - 2. Scatter: Ghost moves to the corner (dark blue)
  - 3. Frightened: Ghost moves randomly (light blue)

- state changes every 30 seconds (visible through the movement and the color)
- Each state is always written above for the clarity


Structure
- `main.py` - the main entry to the game. It initializes the display, creates game entities, handles input, updates logic + runs the game loop

- `pacman.py` - shows the `Pacman` class. It handles its movement based on key input (+ the "mounth eating mode"), draws the animated Pacman figure and displays the "Pacman" label

- `ghost.py` - shows another character, the `Ghost` class. It takes care of FSM-driven movement and behaviour logic, draws the ghost figure and the "Ghost" label + changes the colour depending on current state

- `states.py` - speaks for ghost behaviors as separate FSM state classes: `ChaseState`, `ScatterState`, and `FrightenedState`. Each of them contains movement logic specific to that behavior

- `game_logic.py` - controls the high-level game logic, especially switching the ghost’s state every 30 seconds and invoking the behavior logic from FSM states

How to run the code?
Open `main.py` and in the new terminal, write "python3 main.py".
