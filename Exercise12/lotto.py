import random

#help('random')

#random.sample picks unique characters from a given population in list form, for a given amount
nums = random.sample(range(1, 50), 6)
#assign the sorted numbers to a variable
snums = sorted(nums, key=int)
#display
print("The winning numbers are:", snums)
