from enum import Enum

class States(Enum):
    idle = 0
    run = 1
    get_damage = 2
    attack = 3