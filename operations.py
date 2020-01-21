#!/usr/local/bin/python3

from turing_machine import *
import sys

def add():

    STATE_1 = {
            # S (start) -> S, right, STATE_1
            CreatureType.S : (CreatureType.S, +1, 0, False),
            # U (unitary digit symbole) -> U, right, STATE_1
            CreatureType.D  : (CreatureType.D, +1, 0, False),
            # A (addition) -> A, right, STATE_1
            CreatureType.A : (CreatureType.D, +1, 0, False),
            # E (end operation symbol) -> E, left, STATE_2
            CreatureType.E : (CreatureType.E, -1, 1, False),
            }

    STATE_2 = {
            # D -> Q, HALT
            CreatureType.D : (CreatureType.Q, -1, 0, True)
            }

    instructions_table = InstructionTable(2, [STATE_1, STATE_2])
    init_tape = Tape([CreatureType.S, CreatureType.D,
        CreatureType.D, CreatureType.A, CreatureType.D, CreatureType.D,
                      CreatureType.E, CreatureType.E])

    res_tape = Tape([CreatureType.S, CreatureType.D, CreatureType.D,
                     CreatureType.D, CreatureType.D, CreatureType.Q])

    head_start = 0

    addition = TuringMachine(instructions_table, init_tape, head_start)
    addition.run()


def substraction():

    STATE_1 = {
            # S (start) -> S, right, STATE_1
            CreatureType.S : (CreatureType.B, +1, 0, False),
            # D -> D, right, STATE_1
            CreatureType.D : (CreatureType.A, +1, 0, False),
            # M (minus) -> M, right, STATE_2
            CreatureType.M : (CreatureType.O, +1, 1, False),

            # I -> D, left, STATE_1
            CreatureType.I : (CreatureType.D, -1, 0, False),
            # A -> R, left, STATE_1
            CreatureType.A : (CreatureType.R, -1, 0, False),
            # B -> S, right, STATE_2
            CreatureType.B : (CreatureType.S, +1, 1, False),
            # R -> A, right, STATE_1
            CreatureType.R : (CreatureType.A, +1, 0, False),

            # O -> M, left, STATE_1
            CreatureType.O : (CreatureType.M, -1, 0, False)
            }

    STATE_2 = {
            # D -> E, left, STATE_2
            CreatureType.D : (CreatureType.I, +1, 1, False),
            # E -> E, left, STATE_2
            CreatureType.E : (CreatureType.E, -1, 1, False),
            # I -> E, left, STATE_1
            CreatureType.I : (CreatureType.E, -1, 0, False),
            # R -> B, right, STATE_1
            CreatureType.R : (CreatureType.B, +1, 0, False),

            # O -> R, left, STATE_2
            CreatureType.O : (CreatureType.F, -1, 1, False),
            # A -> H, left, STATE_2
            CreatureType.A : (CreatureType.H, -1, 1, False),
            # B -> S, right, STATE_2
            CreatureType.B : (CreatureType.S, +1, 1, False),
            # H -> D, right, STATE_2
            CreatureType.H : (CreatureType.D, +1, 1, False),
            # R -> Q, HALT
            CreatureType.F : (CreatureType.Q, 0, 1, True)
            }

    instructions_table = InstructionTable(2, [STATE_1, STATE_2])
    init_tape = Tape([CreatureType.S, CreatureType.D, CreatureType.D,
        CreatureType.D, CreatureType.D, CreatureType.D, CreatureType.M,
        CreatureType.D, CreatureType.D, CreatureType.D, CreatureType.E,
        CreatureType.E])

    res_tape = Tape([CreatureType.S, CreatureType.D, CreatureType.D,
                     CreatureType.D, CreatureType.Q])

    head_start = 0

    substraction = TuringMachine(instructions_table, init_tape, head_start)
    substraction.run()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Expected one argument to define the operation type: \"addition\" or \"substraction\"")
    op = sys.argv[1]
    if op == "substraction":
        substraction()
    elif op == "addition":
        add()
    else:
        raise ValueError("Parameters are \"addition\" or \"substraction\"")
