# ----------- #
#   Imports   #
# ----------- #
import pdb
import sys

# ------------- #
#   Functions   #
# ------------- #
def get_index_of_column(column, header_list):
    '''
    Get index of selected column.
    '''
    index_of_header = 0
    for word in header_list:
        word = word
        if column == word:
            index_of_header = header_list.index(word)
            break
    return index_of_header


def get_key_value_assignments(line, f, index_of_header):

    header_dict = {}

    while line:
        line = f.readline().strip()
        split_line = line.split(",")

        # Check if the index of the selected column matches the index in
        # each of the remaining lines. If it matches, assign the element at
        # that matching index as a new key in the dictionary "header_dict",
        # and then get all elements before and after that one, make it one
        # congruent string value, and assign it as the value to the key.
        for word in split_line:
            index_in_line = split_line.index(word)
            if index_of_header == index_in_line:
                #header_dict[word] = ''
                elem_before_index = split_line[:index_in_line]
                #print("The elements before the index are {}".format(elem_before_index))
                elem_after_index = split_line[index_in_line + 1:]
                #print("The elements after the index are {}".format(elem_after_index))
                all_values = elem_before_index + elem_after_index 
                if len(all_values) != 0:
                    header_dict[word] = all_values
    return header_dict


def get_sorted_dict(header_dict):
    sorted_dict = {}
    for k in sorted(header_dict, key=len, reverse=True):
        sorted_dict[k] = header_dict[k]
    return sorted_dict


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
        
        # Read the first line of headers & set it as list split by commas
        line = f.readline().strip()
        split_line = line.split(",")

        print(split_line)

        # Create a dictionary
        #header_dict = {}

        # Get the index of the selected column
        index_of_header = get_index_of_column(column, split_line)
        
        # Create a dictionary & fill it with keys & values from iterating over the next lines
        header_dict = get_key_value_assignments(line, f, index_of_header)
   
        # Create a dictionary sorted in descending order by key string length
        sorted_dict = get_sorted_dict(header_dict)
    
        # Flatten the sorted dictionary for printing at the command line
        for k,v in sorted_dict.items():
            values = ",".join(v)
            print("{},{}".format(k,values))

        # Write the sorted dictionary to a csv output file
        file_out = "sorted_csv_output.csv"
        with open(file_out, 'w') as f_out:
            f_out.write(line + "\n")
            for k,v in sorted_dict.items():
                f_out.write(f"{k},{','.join(v)}\n")

if __name__ == '__main__':
    main()
