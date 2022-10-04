# write your Python code here according to the instructions

## import the csv module
import csv


def get_csv_data(filepath):
    """
    Opens the file at filepath, reads the data using the csv module's DictReader, 
    converts that data to a regular list containing a dictionary for each row of data in the CSV file
    and returns that list.

    :param filepath: The file path of the CSV data file to open
    :returns: A list of dictionaries, where each dictionary represents one row from the file
    """
    f = open(filepath, 'r')

    data = list(csv.DictReader(f))

    f.close()

    return data

def remove_rows_with_null_valued_fields(data):
    """
    Removes any rows with one or more fields set to 'NULL' (string format) from the data set.

    :param data: The data, as a list of dictionaries
    :returns: The modified data, as a list of dictionaries
    """
    # Creating new list to hold rows to remove
    remove_list = []

    # If dict value contains "NULL", append row to remove_list
    for i in data:
        if "NULL" in i.values():
            remove_list.append(i)
    
    # If row in remove_list is in data, remove the row
    for j in remove_list:
        if j in data:
            data.remove(j)

    return data

def remove_rows_with_invalid_handles(data):
    """
    Removes any rows that have handles containing special (non-alphanumeric) characters such as ('$', '*', etc.). 
    Handles can only have alphabets or numbers.

    :param data: The data, as a list of dictionaries
    :returns: The modified data, as a list of dictionaries
    """

    # Creating new list to hold rows to remove
    remove_list = []

    row_counter = 0

    # If 'handle' value is NOT alpha/numeric, append row to remove_list
    for k in data:

        row_counter += 1

        if row_counter == 1:
            continue

        if k['handle'].isalnum() == False:
            remove_list.append(k)
    
    # If row in remove_list is in data, remove the row
    for j in remove_list:
        if j in data:
            data.remove(j)

    return data

def remove_rows_over_affinity_id_level(data, affinity_type, threshold):
    """
    Removes any rows with a value in a given affinity category id field greater than to the supplied threshold.

    :param data: The data, as a list of dictionaries
    :param affinity_type: The type of affinity category id of interest...
    :param threshold: The maximum acceptable id value for this affinity type... records with lower values will be removed.
    :returns: The modified data, as a list of dictionaries
    """
    
    # Creating new list to hold rows to remove
    remove_list = []

    row_counter = 0

    # If value for the affinity_type is greater than threshold value, append row to remove_list
    for l in data:

        row_counter += 1

        if row_counter == 1:
            continue

        if int(l[affinity_type]) > threshold:
            remove_list.append(l)
    
    # If row in remove_list is in data, remove the row
    for j in remove_list:
        if j in data:
            data.remove(j)

    return data

def replace_email_domain(data, old_domain, new_domain):
    """
    Updates any rows where the 'email' ends in the old domain.  Updates to the new domain.

    :param data: The data, as a list of dictionaries
    :param old_domain: The old domain to remove, e.g. '@dmoz.org'
    :param new_domain: The new domain to replace the old_domain with, e.g. '@dmoz.com'
    :returns: The modified data, as a list of dictionaries
    """

    for m in data:

        # If statement for when the old_domain is in the 'email' value
        if old_domain in m['email']:

            # Splitting original email by '@', so that it creates a list with first value as email username and second value as the rest of the domain
            email_split = m['email'].split('@')

            # Creating new email by getting the original email username and adding the new_domain
            new_email = email_split[0] + new_domain

            # Updating the new email value in the dictionary
            m['email'] = new_email

    return data

def save_csv_data(data, filepath):
    """
    Saves the data into the specified file.  Include the field headers as the first row.

    :param data: The data, as a list of dictionaries
    :param filepath: The file path of the CSV data file to save to
    """

    i = data[0]
    
    fieldnames = i.keys()

    # Writer using DictWriter
    writer = csv.DictWriter(open(filepath, 'w', newline=''), fieldnames)
    writer.writeheader()
    writer.writerows(data)


def get_average_and_median_affinity_id(data, affinity_type):
    """
    Calculates the average and median number of the affinity category id of all records in the data set.

    :param data: The data, as a list of dictionaries
    :param affinity_type: The type of affinity category id of interest...
    :returns: The average and median number of affinity id for the given affinity_type (both are of type float) in the order << average, median >>
    """
    #Creating list for affinity values
    affinity_list = []

    # Skipping first row
    row_counter = 0

    # Appending affinity values to affinity_list
    for i in data:

        row_counter += 1

        if row_counter == 1:
            continue

        affinity_value = int(i[affinity_type])

        affinity_list.append(affinity_value)

    # Calculating average
    avg = sum(affinity_list)/len(affinity_list)

    avg = float(avg)

    # Calculating median

    # If length of affinity values is divisible by 2, find the average of two most middle values
    if len(affinity_list) % 2:
        big_index = int(len(affinity_list)/2)
        small_index = int(big_index - 1)

        median = (affinity_list[big_index] + affinity_list[small_index]) / 2
    
    # If not divisible by 2, find the middle value
    else:
        mid_index = (len(affinity_list) / 2) - 0.5
        mid_index = int(mid_index)

        median = affinity_list[mid_index]

    median = float(median)

    return avg, median

    


#################################################
## Do not modify the code below this line      ##
## except to comment out any function calls    ##
## that you do not wish to test at the moment  ##
#################################################

def main():
    ## use the functions defined above to complete munging of the data file

    # get the data from the file
    data = get_csv_data('data/users.csv')

    # munge it
    data = remove_rows_with_null_valued_fields(data)
    data = remove_rows_with_invalid_handles(data)
    data = remove_rows_over_affinity_id_level(data, 'tech_gadget_affinity_category_id', 10)
    data = replace_email_domain(data, '@amazon.de', '@amazon.com')
    print(data)
    # save to the new csv file
    save_csv_data(data, 'data/users_clean.csv')

    # print the average and median affinity level for real food
    avg, median = get_average_and_median_affinity_id(data, 'tech_gadget_affinity_category_id')
    print('The average affinity id for tech gadget is: {}.'.format(avg))
    print('The median affinity id for tech gadget is: {}.'.format(median))

if __name__ == "__main__":
    main()
