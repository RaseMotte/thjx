from magic_game import CreatureType

class InstructionTable:
    def __init__(self, n_states, instructions_table):
        assert(n_states == len(instructions_table))
        self.table = instructions_table

    def __call__(self, state, symbol):
        return self.table[state][symbol]

class Cell:
    def __init__(self, symbol):
        self.symbol = symbol

    def read(self):
        #print("READ %s" % self.symbol)
        return self.symbol

    def write(self, new_symbol):
        #print("WRITE %s" % new_symbol)
        self.symbol = new_symbol#.replace(new_symbol)

    def __str__(self):
        return self.symbol.name

class Tape:
    def __init__(self, symbol_list):
        self.cells = [Cell(symbol) for symbol in symbol_list]

    def read(self, head):
        return self.cells[head].read()

    def write(self, head, new_symbol):
        self.cells[head].write(new_symbol)

    def __str__(self):
        s = ""
        for cell in self.cells:
            s = "%s %s" % (s, cell)
        return s

    def __len__(self):
        return len(self.cells)


class TuringMachine:
    def __init__(self, instruction_table, tape, head):
        self.instruction_table = instruction_table
        self.tape = tape
        self.head = head
        self.cur_state = 0


    def execute(self, symbol):
        # Seek for the ability to trigger
        action = self.instruction_table(self.cur_state, symbol)
        return action


    def run(self):
        halt = False
        while not halt:
            print("Tape : [%s]" % self.tape)
            # Cast infest
            symbol = self.tape.read(self.head)
            # Trigger Rotlung or Necromancia ability
            new_symbol, move_direction, next_state, new_halt = self.execute(symbol)
            print("State: q%d, Head : %d, Symbol : %s" % (self.cur_state + 1,\
                    self.head, symbol.name))
            print("New symbol %s, Move : %s, Next State : q%d, Halt : %s" % \
                    (new_symbol.name, move_direction, next_state, new_halt))
            # Create the new token
            self.tape.write(self.head, new_symbol)
            # If created by the necromancian, poped untapp, causes the turn to
            # end, thus, we change state. Else not.
            self.cur_state = next_state
            # Cast cleansing beam
            self.head += move_direction
            halt = new_halt
            print()
            if self.head < 0 or self.head > len(self.tape):
                raise ValueError("Invalid head position : %d" % (self.head))
        print("Final tape : [%s] " % self.tape)


