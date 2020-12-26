
# Advent of code day 6
# https://adventofcode.com/2020/day/6


class Groups:
    """ 
    It was proving very difficult to write a clean for loop without having to repeat
    code.  This little class contains a very simple interface that uses sets to 
    eleminate duplicate answers and keep track of totals.
    """
    def __init__(self):
        self.sum = 0
        self._group = set()
    
    def calculate_sum(self):
        self.sum += len(self._group)

    def next_group(self):
        self.calculate_sum()
        self._group = set()

    def append(self, answers):
        self._group.update(answers)

    def get_total_answers(self):
        self.calculate_sum()
        return self.sum


groups = Groups()

with open("2020/day06_input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            groups.next_group()
        else:
            groups.append(line)

print("\n%i people answered yes\n" % groups.get_total_answers())

