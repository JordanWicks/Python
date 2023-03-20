Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

blength = '_'*len(Belgium)
print(blength)

rbelgium = Belgium.replace(',', ':')
print(rbelgium)

fields = Belgium.split(",")
population = (int(fields[1])+int(fields[3]))

#wrong population = (int(Belgium[8:16])+int(Belgium[26:32]))
print(population)




