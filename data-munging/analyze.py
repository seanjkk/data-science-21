# Place code below to do the analysis part of the assignment.

import csv

# Importing CSV file
csvfile = open('clean_data.csv', 'r')

reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')

# Creating header
print(":::::Average Fahrenheit Anomolies by Decade:::::")

# Creating counter to skip first row
row_counter = 0

# Creating empty list to store the J-D values in the decade
jan_to_dec_list = []

# Creating empty list to store the average temperature anomoly for each decade
average_list = []

# Creating empty list to store year values to print at the end
decades_list = []

for i in reader:

    # Skipping first row
    row_counter += 1

    if row_counter == 1:
        continue

    # Storing year value
    year = i[0]

    # Storing the first year of each decade for printing purposes 
    if jan_to_dec_list == []:
        start_year = year

    # If the year is NOT the last of the decade
    if year[-1] != "9":

        # Converting J-D value to float and appending to list
        jan_to_dec = float(i[13])
        jan_to_dec_list.append(jan_to_dec)

    # If the year is the last of the decade (ending in 9)
    if year[-1] == "9":

        # Converting J-D value to float and appending to list
        jan_to_dec = float(i[13])
        jan_to_dec_list.append(jan_to_dec)

        # Calculating the average and appending to the list for averages, with 1 decimal point
        average_list.append(format(sum(jan_to_dec_list) / len(jan_to_dec_list), ".1f"))

        # Storing the last year of each decade for printing purposes
        end_year = year

        # Appending the starting and ending years of each decade to a list
        decades_list.append(start_year + " - " + end_year)

        # Emptying the J-D values from the list for the next decade
        jan_to_dec_list = []

# Creating counter for the list of decades
decade_counter = 0

for j in average_list:

    # Printing the average temperature anomoly
    print("The average temperature anomoly in fahrenheit for " + decades_list[decade_counter] + " is " + j)

    decade_counter += 1





