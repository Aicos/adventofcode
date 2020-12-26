
# Advent of code day 6 part 2
# https://adventofcode.com/2020/day/6


class Groups:
    """
    Rewrote this class with different logic but used the same interface.
    
    See comments for an explantion of how it works.
    """
    def __init__(self):
        self.sum = 0
        self._possible_questions = set()
        self.forms = []
    
    def _calculate_sum(self):

        # contents -
        # iterate through each of the forms customs forms in the group
            # iterate through each of the possible letters/chatacters
                # letter not found, eliminate it from questions

        # how ever many questions have not been eliminated that remain...
        # add that to the total sum (for all groups)

        questions = self._possible_questions.copy()

        # iterate through each of the forms customs forms in the group
        for form in self.forms:
            # iterate through each of the possible letters/chatacters
            for pq in self._possible_questions:
                if pq not in form and pq in questions:
                    # eleminate question from questions set
                    questions.remove(pq)

        # get the number of remaining questions
        # # and add to total sum for all groups
        self.sum += len(questions)

    def next_group(self):
        self._calculate_sum()
        self._possible_questions = set()
        self.forms = []
        
    def append(self, answers):

        # collect all possible questions from customs form
        # do that with sets to avoid duplicates

        # break up answers string so the set looks
        # something like this { "a", "b", "c" }

        for char in answers:
            self._possible_questions.add(char)
        
        self.forms.append(answers)
            
    def get_total_answers(self):
        self._calculate_sum()
        return self.sum

def sort_answers(answers):
    """ return alphabetically sorted characters """
    l = sorted(set(answers))
    return "".join(l)


# test input:

# abc
# abcd
# abcf
# 
# a
# a

groups = Groups()

with open("2020/day06_input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            groups.next_group()
        else:
            line = sort_answers(line)
            groups.append(line)

print("\n%i questions where everyone answered yes in all groups\n" % groups.get_total_answers())

