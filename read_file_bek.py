# 1 - Create a new python file in the project called read_file.py

# 2 - Use the open and read methods to slurp the entire contents of your pelican.txt file
# open file in read mode
with open('sample_files/pelican.txt', 'r') as file:
    # read file contents into a single string
    contents = file.read()
# slurping means the entire file is read into memory as a single string.
# 'with' statement automatically handles the closing of the file after its lines are read - good practice!

# 3 - Display the type of the returned data and print the contents of the returned data.
print(type(contents))  # <class 'str'>
print(contents)  # prints over 5 lines due to newline (/n) to mark each new line

# 4 - What data type is the output?
# String

# 5 - Now, write some code that will read the pelican.txt file into a list...
# open file in read mode
with open('sample_files/pelican.txt', 'r') as file:
    # read all lines in file into a list
    # lines = file.readlines()
    # strip() method removes newline character (\n) from each line
    lines = [line.strip() for line in file.readlines()]

# print the list
print(lines)

# ... and then output the number of items within the list.
# there are 5 items (strings) in the list
print(len(lines))

# 6 - Now use a loop to iterate over and print the contents of the file...
# ... Be sure not to include any blank lines in the output.

# open file in read mode
with open('sample_files/pelican.txt', 'r') as file:
    # iterate over each line in the file
    for line in file:
        # end='' prevents adding extra newline
        print(line, end='')