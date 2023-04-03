#variables
firstname = "Jordan"
lastname = "Wicks"

print(firstname, lastname)


#list
fullname = [firstname, lastname]
print(*fullname)



#dictionary
name = {
    "first": firstname,
    "last": lastname
}

print(name["first"])
print(name["last"])


#display all values of a large dictionary
for values in name.values():
   print(values)

#unsure how to display values on single line