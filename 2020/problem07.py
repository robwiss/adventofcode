import networkx as nx

my_input = [x for x in open('problem07_input')]
sample_input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split('\n')

def parse_input(data):
    # sample input line:
    #   dull blue bags contain 2 dotted green bags, 1 dull brown bag, 3 striped tomato bags, 5 muted blue bags.
    d = {}
    for line in data:
        if len(line.strip()) == 0:
            continue
        contain = line.split('contain')
        outer_bag = contain[0][:contain[0].find(' bag')] # gets 'dull blue'
        contains = contain[1].strip(' .').split(', ') # gets ['2 dotted green bags', '1 dull brown bag', '3 striped tomato bags', '5 muted blue bags']
        contained_bags = {}
        for bag_desc in contains:
            bag_desc_tokens = bag_desc.split()[:-1] # gets ['2', 'dotted', 'green']
            if bag_desc_tokens[0] == 'no': # a bag can contain no bags
                continue
            num_bags = int(bag_desc_tokens[0]) # gets 2
            bag_name = ' '.join(bag_desc_tokens[1:]) # gets 'dotted green'
            contained_bags[bag_name] = {'weight': num_bags}
        d[outer_bag] = contained_bags
    return nx.DiGraph(d)

G = parse_input(my_input)
#G = parse_input(sample_input)

def part_one():
    RG = G.reverse()
    predecessors = sorted(nx.dfs_predecessors(RG, 'shiny gold'))
    print(predecessors)
    print(len(predecessors))

def part_two():
    def dfs_cost(node, indent = 0):
        cost = 0
        for n, weight in G[node].items():
            print('{}{} {}'.format(' ' * indent, weight['weight'], n))
            cost = cost + weight['weight'] + weight['weight'] * dfs_cost(n, indent + 2)
        return cost
    print(dfs_cost('shiny gold'))

if __name__ == '__main__':
    print('part one:')
    part_one()
    print('part two:')
    part_two()
