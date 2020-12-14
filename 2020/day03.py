

f = open("day03_input.txt")

grid = [ line.strip() for line in f.readlines() ]
width = len(grid[0])
total_rows = len(grid)

def process_row(row, width, x):
    x_transformed = x % width
    selected_square = row[x_transformed]
    return (selected_square, x_transformed)

# test to see repeating pattern
for c in range(0, 100):
    instr = ".#.#....###..#.#..............#"
    char = instr[c % width ]
    # print(char, end='')

x = 0
tree_count = 0

# go throw one row at a time
for y in range(1, total_rows):
    x += 3
    row = grid[y]
    square, x_transformed = process_row(row, width, x)

    if square == "#":
        trail = "X" # just for output
        tree_count += 1
    else:
        trail = "0" # just for output
    
    # output
    for idx in range(width):
        if x_transformed == idx:
            output = trail
        else:
            output = row[idx]
        print(output, end="")

    print()
        
print("\ntree count is " + str(tree_count))

