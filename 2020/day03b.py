
# walk throw grid list using appropriate stepping
# modify each row that need an X or 0
# output the array at the end

class grid:
    """
    static class
    provides access to grid of trees.
    
    important public properties:

    is_tree(right, down)
    total_rows
    """
    def init():
        file_descriptor = open("day03_input.txt")
        grid.data = [ line.strip() for line in file_descriptor.readlines() ]
        grid._width = len(grid.data[0])
        grid.total_rows = len(grid.data)
        # grid.total_rows = 5

    def transform_right(right):
        return right % grid._width


    def _get_square(right, down):
        """
        private

        return the value or content of a square.  
        This will be "#" or "."
        """

        row = grid.data[down]
        return row[grid.transform_right(right)]
    

    def is_tree(right, down):
        """
        Did the toboggan encounter a tree?
        """
        square = grid._get_square(right, down)
        return square == "#"



# for x in range(0,50):
#    print(grid.get_square(x, 1), end="")

def process_slope(grid, right_steps, down_steps):

    y = down_steps
    x = right_steps
    tree_count = 0

    while(y < grid.total_rows):
        
        if grid.is_tree(x, y):
            tree_count += 1

        x += right_steps
        y += down_steps
          
    return tree_count

def process_all_slopes(stepping):
    
    print()
    
    multiplied = 1
    slope_number = 0

    for right, down in stepping:
        slope_number += 1

        trees = process_slope(grid, right, down)
        multiplied *= trees

        print("Slope %d encountered %d trees" % (slope_number, trees))

    print("\nAll slopes multiplied together: %d\n\n" % multiplied)
 
# ----------------------

grid.init()

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

process_all_slopes(slopes)



    

