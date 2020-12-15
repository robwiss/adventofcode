import re

my_input = [x for x in open('problem14_input')]
sample_input = [x for x in open('problem14_sample2')]
active_input = my_input

# X1XX turn it into 1011, flip the 1, X => 1
# 1011 & 0000 = 0000
# 0000 | 0100 = 0100

# 1011 & 0001 = 0001
# 0001 | 0100 = 0101

# first do the 1s, treat 0 as 0 and X as 0
# X10X turn it into 0100 then or it with the value
# 0100 | 0000 = 0100
# 0100 | 0110 = 0110
# 0100 | 0100 = 0100

# next do the 0s, 1 => 0, X => 0, 0 => 1
# X10X => 0010 then or it with the inverted value
# ~0100 = 1011
# ~0110 = 1001
# ~0100 = 1011
# 0010 | 1011 = 1011 invert back to 0100
# 0010 | 1001 = 1011                0100
# 0010 | 1011 = 1011                0100


def part_one():
    one_table = str.maketrans({'X': '0'})
    zero_table = str.maketrans({'X': '0', '1': '0', '0': '1'})
    instructions = []
    for line in active_input:
        k, v = line.strip().split(' = ')
        if k == 'mask':
            mask_1 = int(v.translate(one_table), 2)
            mask_0 = int(v.translate(zero_table), 2)
            instructions.append({'k': 'mask', 'v': (mask_1, mask_0)})
        else:
            index = int(re.match(r'mem\[([0-9]+)\]', k).group(1))
            val = int(v)
            instructions.append({'k': 'mem', 'v': (index, val)})

    memory = {}
    for instr in instructions:
        if instr['k'] == 'mask':
            mask_1, mask_0 = instr['v']
        elif instr['k'] == 'mem':
            index, val = instr['v']
            val = val | mask_1
            val = ~val | mask_0
            val = ~val
            memory[index] = val
    print(sum(memory.values()))

def part_two():
    # 0 op 0 = 0   op = or/and/xor
    # 0 op 1 = 1   op = or/xor
    # 1 op 1 = 1   op = or/and
    # 1 op 0 = 1   op = or
    # X means to or it with 1, to and it with 0
    base_table = str.maketrans({'X': '0'})
    instructions = []
    for line in active_input:
        k, v = line.strip().split(' = ')
        if k == 'mask':
            base_mask = int(v.translate(base_table), 2)
            # compute all of the wildcard masks
            masks = [(base_mask, 2**36 - 1)]
            i = v.find('X')
            if i == -1:
                continue
            while i != -1:
                exponent = len(v) - i - 1
                or_mask = 2**exponent
                and_mask = (2**36 - 1) & ~or_mask
                new_masks = []
                for old_or_mask, old_and_mask in masks:
                    new_masks.append((old_or_mask | or_mask, old_and_mask))
                    new_masks.append((old_or_mask, and_mask & old_and_mask))
                masks = new_masks
                i = v.find('X', i+1)
            assert(len(masks) == 2**v.count('X'))
            instructions.append({'k': 'mask', 'v': masks})
        else:
            index = int(re.match(r'mem\[([0-9]+)\]', k).group(1))
            val = int(v)
            instructions.append({'k': 'mem', 'v': (index, val)})

    memory = {}
    for instr in instructions:
        if instr['k'] == 'mask':
            masks = instr['v']
        else:
            index, val = instr['v']
            for or_mask, and_mask in masks:
                mask_index = (index | or_mask) & (and_mask if and_mask is not None else 1)
                memory[mask_index] = val
    print(sum(memory.values()))


if __name__ == '__main__':
    print('part one')
    part_one()
    print('part two')
    part_two()
