from typing import List
import itertools
import pdb

my_input = [x for x in open('problem11_input')]
sample_input = [x for x in open('problem11_sample')]
active_input = [[y for y in row.strip()] for row in my_input]

class SeatLayout:
    def __init__(self, layout_grid: List[List[str]]):
        self._layout_grid = layout_grid
    
    def num_occupied_adjacent(self, x: int, y: int) -> int:
        to_check_x = [x]
        if x - 1 >= 0:
            to_check_x.append(x - 1)
        if x + 1 < len(self._layout_grid):
            to_check_x.append(x + 1)
        to_check_y = [y]
        if y - 1 >= 0:
            to_check_y.append(y - 1)
        if y + 1 < len(self._layout_grid[x]):
            to_check_y.append(y + 1)
        to_check = []
        for i in to_check_x:
            for j in to_check_y:
                if i != x or j != y:
                    to_check.append((i, j))

        return sum([self._layout_grid[coord[0]][coord[1]] == '#' for coord in to_check])
    
    def iterate(self):
        new_layout = []
        for x, row in enumerate(self._layout_grid):
            new_row = []
            for y, seat in enumerate(row):
                if seat == '.': # floor never changes
                    new_row.append(seat)
                    continue

                num_occupied_adjacent = self.num_occupied_adjacent(x, y)
                if seat == 'L' and num_occupied_adjacent == 0:
                    new_row.append('#')
                elif seat == '#' and num_occupied_adjacent > 3:
                    new_row.append('L')
                else:
                    new_row.append(seat)
            assert(len(new_row) == len(row))
            new_layout.append(new_row)
        
        return SeatLayout(new_layout)

    def __str__(self):
        return '\n'.join([''.join(row) for row in self._layout_grid])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other is None:
            return False
        return self._layout_grid == other._layout_grid

class SeatLayout2:
    def __init__(self, layout_grid: List[List[str]]):
        self._layout_grid = layout_grid
    
    def visible_in_direction(self, x: int, y: int, direction) -> bool:
        if direction == 'N':
            path = [self._layout_grid[i][y] for i in range(x - 1, -1, -1)]
        elif direction == 'S':
            path = [self._layout_grid[i][y] for i in range(x + 1, len(self._layout_grid))]
        elif direction == 'E':
            path = [self._layout_grid[x][j] for j in range(y + 1, len(self._layout_grid[x]))]
        elif direction == 'W':
            path = [self._layout_grid[x][j] for j in range(y - 1, -1, -1)]
        elif direction == 'NE':
            x_distance = len(range(x, -1, -1))
            y_distance = len(range(y, len(self._layout_grid[x])))
            distance = min(x_distance, y_distance)
            path = [self._layout_grid[x - i][y + i] for i in range(1, distance)]
        elif direction == 'NW':
            x_distance = len(range(x, -1, -1))
            y_distance = len(range(y, -1, -1))
            distance = min(x_distance, y_distance)
            path = [self._layout_grid[x - i][y - i] for i in range(1, distance)]
        elif direction == 'SE':
            x_distance = len(range(x, len(self._layout_grid)))
            y_distance = len(range(y, len(self._layout_grid[x])))
            distance = min(x_distance, y_distance)
            path = [self._layout_grid[x + i][y + i] for i in range(1, distance)]
        elif direction == 'SW':
            x_distance = len(range(x, len(self._layout_grid)))
            y_distance = len(range(y, -1, -1))
            distance = min(x_distance, y_distance)
            path = [self._layout_grid[x + i][y - i] for i in range(1, distance)]
        for c in path:
            if c == 'L':
                return False
            elif c == '#':
                return True
        return False
    
    def num_visible(self, x, y):
        return sum([self.visible_in_direction(x, y, direction) for direction in ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']])
    
    def iterate(self):
        new_layout = []
        for x, row in enumerate(self._layout_grid):
            new_row = []
            for y, seat in enumerate(row):
                if seat == '.': # floor never changes
                    new_row.append(seat)
                    continue

                occupied_seen = self.num_visible(x, y)
                if seat == 'L' and occupied_seen == 0:
                    new_row.append('#')
                elif seat == '#' and occupied_seen > 4:
                    new_row.append('L')
                else:
                    new_row.append(seat)
            assert(len(new_row) == len(row))
            new_layout.append(new_row)
        
        return SeatLayout2(new_layout)

    def __str__(self):
        return '\n'.join([''.join(row) for row in self._layout_grid])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other is None:
            return False
        return self._layout_grid == other._layout_grid

test1_input = [[y for y in row.strip()] for row in '''.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....'''.split('\n')]
test1_layout = SeatLayout2(test1_input)
assert(test1_layout.num_visible(4, 3) == 8)

test2_input = [[y for y in row.strip()] for row in '''.............
.L.L.#.#.#.#.
.............'''.split('\n')]
test2_layout = SeatLayout2(test2_input)
assert(test2_layout.num_visible(1, 1) == 0)

test3_input = [[y for y in row.strip()] for row in '''.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.'''.split('\n')]
test3_layout = SeatLayout2(test3_input)
assert(test3_layout.num_visible(3, 3) == 0)

test4_input = [[y for y in row.strip()] for row in '''#..#..#
.......
.......
#..L..#
.......
.......
#..#..#'''.split('\n')]
test4_layout = SeatLayout2(test4_input)
assert(test4_layout.num_visible(3, 3) == 8)


def part_one():
    last_layout = None
    layout = SeatLayout(active_input)
    while layout != last_layout:
        last_layout = layout
        layout = layout.iterate()
    
    print(sum([s == '#' for row in layout._layout_grid
                        for s in row]))

def part_two():
    last_layout = None
    layout = SeatLayout2(active_input)
    while layout != last_layout:
        last_layout = layout
        layout = layout.iterate()
    
    print(sum([s == '#' for row in layout._layout_grid
                        for s in row]))

if __name__ == '__main__':
    print('part one:')
    part_one()
    print('part two:')
    part_two()
