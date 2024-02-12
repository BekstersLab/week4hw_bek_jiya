# Exercise - Write a line of code to create a file handle to open and append to a file called pelican.txt
handle = open('sample_files/pelican.txt', 'a')
# Exercise - append the following line to the file using the write method of the file handle:
handle.write("A wonderful bird is the pelican,\n")

# Exercise - Append the following second line using the write method:
handle.write("His bill holds more than his bellican.\n")

# Exercise - Create a list that contains the following lines:
lines = ["He can take in his beak, \n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

# Exercise - Append this list to the file using the writelines method.
handle.writelines(lines)
# Why are the "\n" required?
# writelines doesn't add line terminators to the end of each line, they need to be included in the list already

# Exercise - Run the script and confirm a new file called pelican.txt was created and that it contains the limerick as expected:
