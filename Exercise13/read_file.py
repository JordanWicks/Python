# QUESTION 2
# Slurps entire contents of file
print(open('pelican.txt').read())
# Confused on part 3,4. Data type is string??

# reads from 'pelican.txt' and splits into list
# use len() to attain number of items in the list
pelican_list = open('pelican.txt').read().splitlines()
print("Number of lines in file:", end="")
print(len(pelican_list))
print()  # <<< utilised for line break in console, how else could i do this?

#loop function to print contents of file
for line in open('pelican.txt'):
    print(line, end='')


