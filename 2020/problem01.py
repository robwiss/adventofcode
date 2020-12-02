# pre-parsed input
input = [int(x) for x in open('problem01_input')]
# sort the input so it can be binary searched
sorted_entries = sorted(input)

import math
import itertools

def binary_search(arr, comparator, low=0, high=None):
    """
    comparator is a function that returns less than zero for when the algorithm should search to the left,
    zero for a match, and greater than zero when the algorithm should search to the right.
    """
    if high is None:
        high = len(arr) - 1

    # check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if comparator(arr[mid]) == 0:
            return mid
        
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif comparator(arr[mid]) < 0:
            return binary_search(arr, comparator, low, mid - 1)

        # Else the element can only be present in the right subarray
        else:
            return binary_search(arr, comparator, mid + 1, high)
    else:
        # comparator not true for array
        return -1

# set silent to true for profiling
def part_one(silent=False):
    '''
    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
    
    For example, suppose your expense report contained the following:
    
    1721
    979
    366
    299
    675
    1456
    
    In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
    
    Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
    '''
    # for each entry in sorted_entries need to find if there is an element in sorted_entries where entry + element = 2020 
    # approach:
    #   for each entry in sorted_entries:
    #     binary search through the list and search for an element where entry + element = 2020. If entry + element < 2020 go right, if entry + element > 2020, go left.
    found = None
    for entry in sorted_entries:
        other_entries = sorted_entries[:]
        other_entries.remove(entry) # don't use dupe values to find the sum
        index = binary_search(other_entries, lambda x : 2020 - (x + entry))
        if index != -1:
            found = other_entries[index]
            break
    if not silent and found is not None:
        print("{} + {} = {}\n{} * {} = {}".format(entry, found, entry+found, entry, found, entry*found))

# prep data for part two

# get all pairs
entry_pairs = itertools.combinations(sorted_entries, 2)

# set silent to true for profiling
def part_two(silent=False):
    '''
    The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

    Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

    In your expense report, what is the product of the three entries that sum to 2020?
    '''

    # need to find if there is an entry in entry_pairs and an element in sorted_entries where entry[0] + entry[1] + element = 2020 
    # approach:
    #   for each entry in entry_pairs:
    #     binary search through sorted_entries and search for and element where entry[0] + entry[1] + element = 2020. If sum is < 2020 go right, if sum is > 2020, go left.
    z = None # z will be the value that makes a sum of 2020 with the current entry pair
    for x, y in entry_pairs:
        other_entries = sorted_entries[:]
        other_entries.remove(x) # don't use dupe values to find the sum
        other_entries.remove(y)
        index = binary_search(other_entries, lambda z : 2020 - (x + y + z))
        if index != -1:
            z = other_entries[index]
            break
    
    if not silent and z is not None:
        sum = x + y + z
        product = x * y * z
        print("{x} + {y} + {z} = {sum}\n{x} * {y} * {z} = {product}".format(x=x, y=y, z=z, sum=sum, product=product))

if __name__ == '__main__':
    print("part one:")
    part_one()
    print("part two:")
    part_two()
