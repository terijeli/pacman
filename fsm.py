from enum import Enum, auto

class GhostState(Enum):
    SCATTER = auto()
    CHASE = auto()
    FRIGHTENED = auto()
    DEAD = auto()
