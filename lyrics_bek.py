# import Counter from collections module to count objects eg word occurrence
from collections import Counter

print("-" * 8, "High & Dry - Radiohead", "-" * 8)

# print the file using best slurping method
with open('sample_files/HighAndDry.txt', 'r') as file:
    for line in file:
        print(line, end='')

print("\n")
print("-" * 8, "Word Count", "-" * 8)

# empty counter object
word_count = Counter()

with open('sample_files/HighAndDry.txt', 'r') as file:
    for line in file:
        # convert each line to lowercase and split into words
        words = line.lower().split()
        # update the counter with words from line
        word_count.update(words)

# display words in order of most common
print(word_count.most_common())

print("\n")
print("-" * 8, "Word Replacement", "-" * 8)

word_find = "high"
word_replace = "low"


with open('sample_files/HighAndDry.txt', 'r') as file:
        file_contents = file.read()

file_contents = file_contents.replace(word_find, word_replace)

new_file_path = 'sample_files/HighAndDry_modified.txt'

with open(new_file_path, 'w') as file:
    file.write(file_contents)

print(f"Replacement complete. Modified content saved to '{new_file_path}'.")