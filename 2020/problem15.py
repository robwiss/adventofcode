
my_input = [x for x in open('problem15_input')]
active_input = [int(x) for x in my_input[0].strip().split(',')]

class ElfGameIterator:
    def __init__(self, elfgame):
        self._e = elfgame
    
    def __next__(self):
#        print(self._e._turn, self._e._turns)
        if self._e._turns == self._e._turn:
            raise StopIteration
        to_speak = 0
        if self._e._last_spoken in self._e._turn_spoken:
            to_speak = self._e._turn - self._e._turn_spoken[self._e._last_spoken]

#        print(self._e._turn, self._e._last_spoken, to_speak, self._e._turn_spoken)
        
        self._e._turn_spoken[self._e._last_spoken] = self._e._turn
        self._e._turn = self._e._turn + 1
        self._e._last_spoken = to_speak
        return to_speak

# initialize with numbers, (position, value, last turn spoken)
# get the next number
class ElfGame:
    def __init__(self, numbers, turns=None):
        self._last_spoken = numbers[-1]
        self._turn_spoken = {}
        for i, x in enumerate(numbers[:-1]):
            self._turn_spoken[x] = i + 1
        self._turn = len(numbers)
        self._turns = turns
    
    def __iter__(self):
        return ElfGameIterator(self)
    
assert([x for x in ElfGame([0,3,6], 10)] == [0, 3, 3, 1, 0, 4, 0])
e = iter(ElfGame([1,3,2], 2020))
while True:
    try:
        i = next(e)
    except StopIteration:
        break
assert(i == 1)
e = iter(ElfGame([2,1,3], 2020))
while True:
    try:
        i = next(e)
    except StopIteration:
        break
assert(i == 10)
e = iter(ElfGame([1,2,3], 2020))
while True:
    try:
        i = next(e)
    except StopIteration:
        break
assert(i == 27)
e = iter(ElfGame([2,3,1], 2020))
while True:
    try:
        i = next(e)
    except StopIteration:
        break
assert(i == 78)
e = iter(ElfGame([3,2,1], 2020))
while True:
    try:
        i = next(e)
    except StopIteration:
        break
assert(i == 438)
e = iter(ElfGame([3,1,2], 2020))
while True:
    try:
        i = next(e)
    except StopIteration:
        break
assert(i == 1836)

def part_one():
    e = iter(ElfGame(active_input, 2020))
    while True:
        try:
            i = next(e)
        except StopIteration:
            break
    print(i)

def part_two():
    e = iter(ElfGame(active_input, 30000000))
    while True:
        try:
            i = next(e)
        except StopIteration:
            break
    print(i)

if __name__ == '__main__':
    print('part one')
    part_one()
    print('part two')
    part_two()
