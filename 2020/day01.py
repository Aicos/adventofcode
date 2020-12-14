
f = open("day1_input.txt", "r")
raw_data = f.read().splitlines()
data = [ int(num) for num in raw_data ]

# print(data)

def new_calc(list):
    list_length = len(list)
    for idx1 in range(0, list_length):
        num1 = list[idx1]
        for idx2 in range(idx1 + 1, list_length):
            num2 = list[idx2]
            # print("idx: %s,%s)  %s + %s" % (idx1, idx2, num1, num2))
            if (num1 + num2 == 2020):
                return num1 * num2

def old_calc(list):
    for idx1, num1 in enumerate(list):
        for idx2, num2 in enumerate(list):
            if (idx2 - idx1 > 0):
                # print("idx: %s,%s)  %s + %s" % (idx1, idx2, num1, num2))
                if (num1 + num2 == 2020):
                    return num1 * num2

print(old_calc(data))
print(new_calc(data))


