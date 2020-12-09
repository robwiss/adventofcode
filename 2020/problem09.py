
my_input = [int(x) for x in open('problem09_input')]
sample_input = [int(x) for x in open('problem09_sample')]
active_input = my_input

# 5 for sample, 25 for input
preamble_length = 25

def part_one():
    # check each number to see if it's the sum of the previous 'preamble_length'
    # numbers before it
    for i, x in enumerate(active_input[preamble_length:]):
        # search the previous 5 numbers to see if any pairs add up to x, runs in O(n!)
        found = False
        for j in range(i, i + preamble_length):
            for k in range(j + 1, i + preamble_length):
                if active_input[j] + active_input[k] == x:
                    found = True
                    break
            if found:
                break
        if not found:
            return x

def part_two():
    sum_to_find = part_one()
    for i in range(len(active_input)):
        curr = active_input[i]
        j = i + 1
        while j < len(active_input) and curr < sum_to_find:
            curr = curr + active_input[j]
            if curr == sum_to_find:
                mx = max(active_input[i:j+1])
                mn = min(active_input[i:j+1])
                print(mn + mx)
            j = j + 1

if __name__ == '__main__':
    print('part one:')
    print(part_one())
    print('part two:')
    part_two()
