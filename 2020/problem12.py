import re

my_input = [x for x in open('problem12_input')]
sample_input = [x for x in open('problem12_sample')]
active_input = [re.match(r'(N|S|E|W|L|R|F)([0-9]+)', line).groups() for line in my_input]

class Ship:

    def __init__(self, heading):
        self.heading = heading # N is 0, E is 90, S is 180, W is 270
        self.x = 0
        self.y = 0

    def move(self, action):
        d = action[0]
        v = int(action[1])
        if d == 'L':
            self.heading = self.heading - v
            if self.heading < 0:
                self.heading = 360 - (abs(self.heading) % 360)
            # 0 - 90 = 270
            # 0 - 270 = 90
            # 0 - 450 = 270
            return
        elif d == 'R':
            self.heading = (self.heading + v) % 360
            return
        
        card_from_deg = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
        if d == 'F':
            d = card_from_deg[self.heading]

        if d == 'N':
            self.x = self.x + v
        elif d == 'S':
            self.x = self.x - v
        elif d == 'E':
            self.y = self.y + v
        elif d == 'W':
            self.y = self.y - v

def part_one():
    s = Ship(90)
    for action in active_input:
        s.move(action)
    print(abs(s.x) + abs(s.y))

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        return Coordinate(self.x * other, self.y * other)

class Ship2:

    def __init__(self, waypoint: Coordinate):
        self.pos = Coordinate(0, 0)
        self.waypoint = waypoint

    def move(self, action):
        d = action[0]
        v = int(action[1])
        if d == 'F':
            wp = self.waypoint * v
            self.pos = self.pos + wp
        elif d == 'N':
            self.waypoint = self.waypoint + Coordinate(v, 0)
        elif d == 'S':
            self.waypoint = self.waypoint + Coordinate(v * -1, 0)
        elif d == 'E':
            self.waypoint = self.waypoint + Coordinate(0, v)
        elif d == 'W':
            self.waypoint = self.waypoint + Coordinate(0, v * -1)
        elif d == 'L':
            assert(v < 360)
            # (4 N, 10 E) -> (10 N, -4 W)     x * -1 and swap
            for i in range(v // 90):
                self.waypoint = Coordinate(self.waypoint.y, self.waypoint.x * -1)
        elif d == 'R':
            assert(v < 360)
            # (4 N, 10 E) -> (-10 S, 4 E)     y * -1 and swap
            # (-10 S, 4 E) -> (-4 S, -10 W)   y * -1 and swap
            # (-4 S, -10 W) -> (10 N, -4 W)   y * -1 and swap
            for i in range(v // 90):
                self.waypoint = Coordinate(self.waypoint.y * -1, self.waypoint.x)

def part_two():
    s = Ship2(Coordinate(1, 10))
    for action in active_input:
        s.move(action)
    print(abs(s.pos.x) + abs(s.pos.y))

if __name__ == '__main__':
    print('part one:')
    part_one()
    print('part two:')
    part_two()
