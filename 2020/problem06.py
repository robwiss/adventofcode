import string
import functools

my_input = [x.strip() for x in open('problem06_input')]

all_questions = set(string.ascii_lowercase)

def parse_input_one(data):
    # groups are separated by newlines
    # add each letter to a set for the group until the newline
    parsed = []
    group = set()
    for line in data:
        if len(line) == 0:
            assert(all_questions.issuperset(group))
            parsed.append(group)
            group = set()
        for letter in line:
            group.add(letter)
    return parsed

def parse_input_two(data):
    # need to find the questions all members of a group answered yes for
    # if each group member's answers are marked as a set, the questions
    # all group members answered yes to is the intersection of all of those
    # sets
    parsed = []
    groups = []
    for line in data:
        if len(line) == 0:
            group = functools.reduce(lambda x, y: x.intersection(y), groups)
            parsed.append(group)
            groups = []
            continue
        groups.append(set(line))
    return parsed

def part_one():
    customs_forms = parse_input_one(my_input)
    print(sum([len(x) for x in customs_forms]))

def part_two():
    customs_forms = parse_input_two(my_input)
    print(sum([len(x) for x in customs_forms]))

if __name__ == '__main__':
    print('part one:')
    part_one()
    print('part two')
    part_two()
