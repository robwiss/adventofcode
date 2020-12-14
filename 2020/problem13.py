
my_input = [x for x in open('problem13_input')]
sample_input = [x for x in open('problem13_sample')]
active_input = my_input

def part_one():
    time = int(active_input[0])
    buses = [int(x) for x in filter(lambda x: x != 'x', active_input[1].split(','))]
    mod = [time % bus for bus in buses]
    try:
        i = mod.index(0)
        print(buses[i])
        return
    except ValueError:
        pass
    diff = [bus - mod for bus,mod in zip(buses, mod)]
    min_value = min(diff)
    print(buses[diff.index(min_value)] * min_value)

def part_two():
# t % 7 = 0             
# (t + 1) % 13 = 0     t % 13 = 13 - 1
# (t + 4) % 59 = 0     t % 59 = 59 - 4
# (t + 6) % 31 = 0     t % 31 = 31 - 6
# (t + 7) % 19 = 0     t % 19 = 19 - 7
    integers = [int(x) if x != 'x' else x for x in active_input[1].split(',')]
    conditions = list(filter(lambda x: x is not None, [(x, (x - i) % x) if x != 'x' else None for i, x in enumerate(integers)]))
    n = 0
    lcm = 1
    for i in range(len(conditions)-1):
        curr_c = conditions[i]
        next_c = conditions[i+1]
        lcm = lcm * curr_c[0]
        while n % next_c[0] != next_c[1]:
            n = n + lcm
    print(n)

if __name__ == '__main__':
    print('part one')
    part_one()
    print('part two')
    part_two()
