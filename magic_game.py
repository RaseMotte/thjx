from enum import Enum

class CreatureColor(Enum):
    WHITE = "White" # Right of the head
    GREEN = "Green" # Left of the head
    BLUE = "Blue" # Halt !

class CreatureType(Enum):
    A = "Aetherborn"
    B = "Basilik"
    C = "Cephalid"
    D = "Demon"
    E = "Elf"
    F = "Faerie"
    G = "Giant"
    H = "Harpy"
    I = "Illusion"
    J = "Juggernaut"
    K = "Kavu"
    L = "Leviathan"
    M = "Myr"
    N = "Noggle"
    O = "Orc"
    P = "Pegasus"
    Q = "Assasin"
    R = "Rhino"
    S = "Silver"

class Token:
    def __init__(self, color, creature_type, power_toughness=2, is_vampire=False):
        """
        Define a symbol on the tape.

        Parameters:
        ----------
        color : CreatureColor
            Define if its at the right or left of the head.

        type : CreatureType
            Define the equivalent symbol in instruction table.

        power_toughness : int
            Power and toughness of the creature. We use only one int to
            represent both as they must always be equal for the turing
            machine to operate properly.
            Represent the distance to head.
            (2/2) : indicates where the head is at.
            (3/3) : distance of one to the head
            ect ect

        is_vampire : Bool
            Whereas the token as the type vampire added to its type.
        """
        self.color = color
        self.creature_type = creature_type
        self.power_toughness = power_tougness
        self.is_vampire = is_vampire

    def __str__(self):
        return "%s : %s" % (CreatureType[self.creature_type],
                CreatureColor[self.color])

    def add_marker(self, marker_value):
        print("%s marked with (%d/%d)" % (marker_value, marker_value))
        self.power_tougness += marker_value
        if self.power_tougness == 0:
            self.die()

    def die(self):
        print("DIED")
        self.color = None
        self.creature_type = None
        self.power_toughness = 0
        self.is_vampire = False

    def is_not_dead(self):
        return self.color or self.creature_type or self.power_toughness \
                      or self.is_vampire

    def replace(self, color, creature_type):
        if self.is_not_dead():
            raise ValueError("Creature must be dead to be replaced.")
        self.color = color
        self.creature_type = creature_type
        self.power_toughness = 2
        self.is_vampire = False

