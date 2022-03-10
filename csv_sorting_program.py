# ----------- #
#   Imports   #
# ----------- #
import sys

# ------------- #
#   Functions   #
# ------------- #

# -------- #
#   Main   #
# -------- #

def main():
    
    program = sys.argv[0] 
    file_in = sys.argv[1]
    column = sys.argv[2]

    # Check that 2 arguments were given at the command line
    if len(sys.argv) < 3:
        print("Error: not enough arguments provided at the command line.")
        sys.exit()

    # Check that the 1st argument is the program to execute & the 2nd, the column

    # Open the input file, being the 1st argument provided at the command line
    with open(file_in) as f:
        line = f.readline()
        count = 1
        while line:
            print("Line #{}: {}".format(count, line.strip()))
            line = f.readline()
            count += 1


if __name__ == '__main__':
    main()
