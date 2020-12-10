import networkx as nx
from toolz import itertoolz

my_input = [int(x) for x in open('problem10_input')]
sample_input = [int(x) for x in open('problem10_sample')]
active_input = sorted(my_input + [0]) # add 0 for the charging device
active_input = active_input + [active_input[-1] + 3] # add an entry for the device to be charged

def part_one():
    result = {1: 0, 2: 0, 3: 0}
    for x,y in itertoolz.sliding_window(2, active_input):
        result[y - x] = result[y - x] + 1
    print(result[1] * result[3])

def part_two():
    d = {}
    for i, x in enumerate(active_input):
        d[x] = []
        while i+1 < len(active_input) and active_input[i+1] - x < 4:
            d[x].append(active_input[i+1])
            i = i + 1
    G = nx.DiGraph(d)

    stack = [0]
    answers = {active_input[-1]: 1}
    while len(stack) > 0:
        val = stack[-1]
        if val in answers: # already have this one
            stack.pop()
        # if there are answers for all of the children, record the answer
        # if not, add the children to the stack
        if all([x in answers for x in G[val].keys()]):
            answers[val] = sum([answers[x] for x in list(G[val].keys())])
        else:
            stack.extend(list(G[val].keys()))
    print(answers[0])

if __name__ == '__main__':
    print('part one:')
    print(part_one())
    print('part two:')
    part_two()
