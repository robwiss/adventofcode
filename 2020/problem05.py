import operator

my_input = [x.strip() for x in open('problem05_input')]
# split it into the row part and the col part
boarding_passes = [(x[:7], x[7:]) for x in my_input]

def bsp_row_to_int_row(bsp_row):
    table = str.maketrans({'F': '0', 'B': '1'})
    bin_str = bsp_row.translate(table)
    return int(bin_str, 2)

def bsp_col_to_int_col(bsp_col):
    table = str.maketrans({'L': '0', 'R': '1'})
    bin_str = bsp_col.translate(table)
    return int(bin_str, 2)

seat_ids = [bsp_row_to_int_row(row) * 8 + bsp_col_to_int_col(col) for row, col in boarding_passes]
seat_ids = sorted(seat_ids)

def part_one():
    print(seat_ids[-1])

def part_two():
    last_seat_id = None
    for seat_id in seat_ids:
        if last_seat_id is not None:
            if seat_id != last_seat_id + 1:
                print(last_seat_id + 1)
        last_seat_id = seat_id

if __name__ == '__main__':
    print('part one:')
    part_one()
    print('part two:')
    part_two()