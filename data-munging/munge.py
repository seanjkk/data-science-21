# Place code below to do the munging part of this assignment.

import csv

f = open("raw_data.txt", "r")

raw_data = f.read()

# Splitting the data by new line
data = raw_data.split("\n")

# Deleting unwanted notes at the top
del data[0:7]

# Popping the first row to add back later
first_line = data.pop(0)

# Removing empty strings from list
for i in data:
    if not i:
        data.remove(i)

# Creating empty list to append to
munged_list = []

# Splitting each term in the list by whitespace, then checking if the first term is numeric and appending to empty list
for j in data:
    k = j.split()
    if k[0].isnumeric():
        munged_list.append(k)

# Creating empty list to identify items to remove
remove_list = []

for l in munged_list:

    # Removing the repetitive year column at the end of each item
    del l[-1]

    l_length = len(l)
    counter = 0
    
    # Appending the items with *'s to the remove list
    while counter < len(l):
        if "*" in l[counter]:
            remove_list.append(l)
            break
        counter += 1

# Removing the items with *'s
for m in remove_list:
    if m in munged_list:
        munged_list.remove(m)

# Creating empty list for fahrenheit values
fahrenheit_list = []

for n in munged_list:

    temperatures = []

    # Popping the year value into a variable as it does not need fahrenheit conversion
    year = n.pop(0)

    # Multiplying each value by 0.018 formatted to one decimal and adding to temporary temperatures list
    for o in n:
        temperatures.append(format(int(o) * 0.018, ".1f"))

    # Inserting the year into the first position
    temperatures.insert(0, year)

    # Appending to the fahrenheit list
    fahrenheit_list.append(temperatures)

# Munging the first line
first_line = first_line.split()
del first_line[-1]

# Inserting the first line to the first position
fahrenheit_list.insert(0, first_line)

f.close()

# Converting to CSV

csvfile = open("clean_data.csv", "w", newline='')

writer = csv.writer(csvfile)

writer.writerows(fahrenheit_list)