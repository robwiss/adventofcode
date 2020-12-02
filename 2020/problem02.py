from typing import List, Dict, Tuple

def parse_input(input_lines : List[str]) -> List[Tuple[Dict, str]]:
    pw_list = []
    for line in input_lines:
        xy, letter, pw = line.split(' ') # tokenize input of form "4-5 h: hhhhh"
        x, y = xy.split('-') # get values x and y that were separated by a hyphen
        letter = letter[0] # strip the colon off of the letter

        policy = { 'x': int(x), 'y': int(y), 'letter': letter }
        pw_list.append((policy, pw)) # store the policy and the password in a list
    return pw_list

my_input = parse_input(open('problem02_input').readlines())

def part_one():
    '''
    Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

    The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.
    
    Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
    
    To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
    
    For example, suppose you have the following list:
    
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    
    Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
    
    In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
    
    How many passwords are valid according to their policies?
    '''

    # approach:
    #   for each password, make a histogram of all letters in the pw.
    #   check if the letter occurs the correct amount of times using the histogram
    numvalid: int = 0
    for policy, pw in my_input:
        l = policy['letter']
        pw_hist = {}
        # build histogram
        for c in pw:
            if c in pw_hist:
                pw_hist[c] = pw_hist[c] + 1
            else:
                pw_hist[c] = 1
        if l not in pw_hist: # skip this pw if the policy character doesn't appear in it
            continue
        n = pw_hist[l] # get num occurrences of policy character
        x = policy['x']
        y = policy['y']
        if n >= x and n <= y: # check if valid
            numvalid = numvalid + 1
    
    print('number of valid passwords: {}'.format(numvalid))

def part_two():
    '''
    While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

    The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
    
    Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
    
    Given the same example list from above:
    
        1-3 a: abcde is valid: position 1 contains a and position 3 does not.
        1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
        2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    
    How many passwords are valid according to the new interpretation of the policies?
    '''

    # approach:
    #   retrieve the characters important to the policy for each pw
    #   check if the important characters match the policy character
    #   xor the result to make sure one and only one spot matches

    numvalid: int = 0
    for policy, pw in my_input:
        l = policy['letter']
        pos1 = policy['x'] - 1 # account for one-indexed policy
        pos2 = policy['y'] - 1
        pos1_correct = pos1 < len(pw) and pw[pos1] == l # check if position matches
        pos2_correct = pos2 < len(pw) and pw[pos2] == l
        correct = pos1_correct ^ pos2_correct
        if correct:
            numvalid = numvalid + 1
    
    print('number of valid passwords: {}'.format(numvalid))

if __name__ == '__main__':
    print('part one:')
    part_one()
    print('part two:')
    part_two()