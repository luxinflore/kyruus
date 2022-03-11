# kyruus
Coding Challenge for Kyruus Team Orko

### Requirements to Execute ###
Python 3

### Program Scope ###
Input: Unsorted CSV file 
			--> sample_csv_input.csv
CLI arguments: python3 <program to execute> <csv input file> <column to sort>  
			--> python3 csv_sorting_program.py sample_csv_input.csv City
Output: Sorted CSV file (descending string order)
			--> sorted_csv_output.csv

The program scope takes the input of a .csv file type and outputs a sorted version of that .csv in descending string 
order based on the column specified. String order is defined as the number of characters in a given string value. The 
sorrting of data in the selected column needs to maintain the extended columns associated with said column. In other 
words, the sorting of one column needs to consider all columns so that sorting is coordinated in a comprehensive and 
congruent fashion.

### Sample Input ###
Based on the details provided in the "Team Orko Take-Home Exercise" assignment, a sample input is created called 
"sample_csv_input.csv". It has the following content, as provided in the assignment:

City,State,Motto,Mayor
Portland,Oregon,The City That Works,Ted Wheeler
Boston,Massachusetts,It’s All Here,Michelle Wu
New Orleans,Louisiana,City of Yes,LaToya Cantrell

### Edge Cases ###
Some commonalities discerned in this sample input include:
1. There are 4 columns
2. There are 3 rows after the header row
3. Based on the column titles, it logically follows that each column's data may contain strings with space characters
4. The "City", "State", and "Mayor" columns will likely have 1-2 string values potentially seperated by a space
5. The "Motto" column may have 3-4 string values separated by a space and/or an apostrophe

Some edge cases might include:
1. Checking whether the column selected is found in the headers of the sample input
2. Checking whether there are 1 or more rows/cells below the selected column header
3. Checking whether the string value found in the cells below the selected column have a space or an apostrophe

### Program Logic ###
Set CLI parsing using sys.argv where index 0 is the csv input & index 1 is the column to sort by
Read in the CSV input file
The first line of the CSV input file has 4 headers delimited by commas
Check if the CLI arg specifying the column header to sort by is a match to 1 of the string values in this first line
If it is not a match to any of them, provide error output at command line & terminate program
If it is a match to one of the strings, go to next line
On next line (2nd line) in the csv input, set the selected column's value as a key in a new dictionary
Set the dictionary key's value as the remainder of that line (the comma-delimited strings before & after the chosen key)
Continue doing this key-value assignment into the dictionary for the remaining lines in the csv file
Sort the dictionary by its key lengths (or default dict sorting)
Once there is a sorted dictionary in memory, then we output the values from it in the same order
