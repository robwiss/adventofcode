import re
from typing import List

sample_input = [x for x in open('problem08_sample')]
my_input = [x for x in open('problem08_input')]

class Instruction:
    @staticmethod
    def from_input_line(line):
        retval = Instruction()
        retval.opcode, retval.sign, retval.value = re.match(r'^(nop|jmp|acc) (\+|-)(\d+)$', line).groups()
        retval.value = int(retval.value)
        retval.signed_value = int('{}{}'.format(retval.sign, retval.value))
        return retval
    
    def __str__(self):
        return '{} {}{}'.format(self.opcode, self.sign, self.value)

    def __repr__(self):
        return str(self)
    
class Computer:
    def __init__(self, instructions):
        self.instructions: List[Instruction] = instructions
        self.reset()
        self._debug_print: bool = False
    
    @property
    def debug_print(self):
        return self._debug_print
    
    @debug_print.setter
    def debug_print(self, value):
        self._debug_print = value
    
    @property
    def pc(self):
        return self._pc
    
    @property
    def acc(self):
        return self._acc

    @property
    def terminated(self):
        return self._pc == len(self.instructions)

    def step(self):
        '''execute the current instruction and increment the program counter'''
        if self.terminated:
            return
        instruction = self.instructions[self._pc]
        old_pc = self._pc
        if instruction.opcode == 'jmp':
            self._pc = self._pc + instruction.signed_value
        elif instruction.opcode == 'acc':
            self._acc = self._acc + instruction.signed_value
            self._pc = self._pc + 1
        elif instruction.opcode == 'nop':
            self._pc = self._pc + 1

        if self._debug_print:
            print('{} | pc: {} acc: {}'.format(
                self.instructions[old_pc],
                self._pc,
                self._acc))
    
    def nexti(self):
        return self.instructions[self._pc]
    
    def reset(self):
        self._pc = 0
        self._acc = 0

    def run(self, execution_hook=lambda x: None):
        while not self.terminated:
            execution_hook(self)
            self.step()

instructions = [Instruction.from_input_line(line) for line in my_input]
computer = Computer(instructions)

class InfiniteLoop(Exception):
    pass

class TestInfLoop:
    def __init__(self):
        self.pc_visited = set()
    
    def get_hook(self):
        def hook(computer):
            if computer.pc in self.pc_visited:
                raise InfiniteLoop
            self.pc_visited.add(computer.pc)
        return hook

class PcTraceInfLoop:
    def __init__(self):
        self.pc_trace = []
    
    def get_hook(self):
        testinfloop_h = TestInfLoop().get_hook()
        def hook(computer):
            self.pc_trace.append(computer.pc)
        def and_(computer):
            hook(computer)
            testinfloop_h(computer)
        return and_

def part_one():
    computer.reset()
    try:
        computer.run(TestInfLoop().get_hook())
    except InfiniteLoop:
        pass
    print(computer.acc)

def part_two():
    computer.reset()
    # record all instructions the program encounters before it hits the inifinite loop
    h = PcTraceInfLoop()
    try:
        computer.run(h.get_hook())
    except InfiniteLoop:
        pass
    # loop backwards through instructions, swapping nop and jmp and seeing if the program
    # terminates when run
    def swap_jmpnop(instruction: Instruction):
        if instruction.opcode == 'jmp':
            instruction.opcode = 'nop'
        elif instruction.opcode == 'nop':
            instruction.opcode = 'jmp'

    for pc in reversed(h.pc_trace):
        if computer.instructions[pc].opcode in ['jmp', 'nop']:
            # swap jmp <-> nop then see if the program terminates
            swap_jmpnop(computer.instructions[pc])
            computer.reset()
            h2 = PcTraceInfLoop()
            try:
                computer.run(h2.get_hook())
            except InfiniteLoop:
                # program didn't terminate, swap back since only one instruction can change
                swap_jmpnop(computer.instructions[pc])
                continue
            print(computer.acc)
            return

if __name__ == '__main__':
    print('part one:')
    part_one()
    print('part two:')
    part_two()
