        #QUESTION 1
        #opens or creates a new file with the 'append' function
        #assigned to a variable, so we can close
pelican_file = open('pelican.txt', mode='a')

        #create variable to assign to write function
output = open('pelican.txt', 'w')

        #input variable .write to add to append to file
output.write("A wonderful bird is the pelican\n"
             "His bill holds more than his belican\n")

        #create variable and add list, then add variable to output.writelines to add to file
        #using \n to each value so that its on a new line
lines = ["He can take in his beak,\n",
         "Enough food for a week,\n",
         "But i'm damned if I see how the helican.\n"]

output.writelines(lines)

        #close file
pelican_file.close()