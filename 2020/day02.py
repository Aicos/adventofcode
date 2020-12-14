
import re

def check_password(input):

    # carrage return affects output
    input = input.strip()

    # sample
    # input = "66-19 g: gggggggggggggggggggg"

    parts = re.findall(r"^(\d{1,4})-(\d{1,4}) ([a-z]): ([a-z]+)$", input)[0]

    lower = int(parts[0])
    higher = int(parts[1])
    search_char = parts[2]
    password = parts[3]

    occurances = password.count(search_char)

    if occurances >= lower and occurances <= higher:
        print("%s is valid" % input)
        return True
    else:
        print("%s is not valid" % input)
        return False

f = open("day02_input.txt")

valid_passwords = 0

for line in f.readlines():
    if check_password(line):
        valid_passwords += 1

print("%s valid passwords." % valid_passwords)
