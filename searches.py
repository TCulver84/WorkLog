import os
import csv
import datetime
import re


class Searches():
    """Contains all applicable methods and variables
     applicable to searching the .CSV file"""

    def __init__(self, search_value='', search_column=''):
        self.search_value = search_value
        self.search_column = search_column

    def list_values(self):
        """Shows the user the availible values to search
         based on selected search type"""
        csv_file = csv.reader(open('data.csv', "r"))
        data_elements = ''
        self.search_value = list(self.search_value)
        # Changed from empty list to variable
        firstline = True  # Skip header line in .CSV file
        for row in csv_file:
            if firstline:
                firstline = False
                continue
            else:
                data_elements = list(
                    row[column] for column in [int(self.search_column)])
                self.search_value.append(data_elements[0])
                print(data_elements[0])

    def print_results(self, search_value):
        """Shows the user multiple output rows based
         on a provided search value"""
        os.system('clear')
        print("HERE'S YOUR DATA!!!")
        csv_file = csv.reader(open('data.csv', "r"))
        returned_values = []
        for row in csv_file:
            for field in row:
                if field == search_value:  # Match field to search value
                    if row not in returned_values:  # Prevent Dupes
                        returned_values.append(row)
        titles = ['DATE', 'TITLE', 'TIME', 'NOTES']
        for x in returned_values:  # Make list readable
            dictionary = dict(zip(titles, x))  # Convert to dict
            for key, value in dictionary.items():
                print(key + ':', value)
            print('\n')

    def date_search(self):
        """Method to search .CSV file by date column"""
        while True:
            os.system('clear')
            print("Dates Availible to Search:")
            self.search_column = 0
            self.list_values()
            search_date = input('\nPlease Use DD/MM/YYYY: ')
            try:
                datetime.datetime.strptime(search_date, '%d/%m/%Y')
                if search_date not in self.search_value:
                    print("Not an Availible Selection!")
                    input("Press ENTER to Try Again!")
                    continue
                else:
                    self.print_results(search_date)
                    input("\nPress ENTER to Return to the Main Menu")
                    break
            except ValueError:
                print("ValueError: Please Use DD/MM/YYYY.")
                input("Press ENTER to Try Again")
                continue
            else:
                break

    def time_search(self):
        """Method to search .CSV file by time column"""
        while True:
            os.system('clear')
            print("Times Availible to Search:")
            self.search_column = 2
            self.list_values()
            search_time = str(input('\nPlease Use a Whole Number: '))
            if search_time not in self.search_value:
                input("Not an Availible Selection! Press ENTER to Try Again!")
                continue
            else:
                self.print_results(search_time)
                input("\nPress ENTER to Return to Main Menu")
                break

    def string_search(self):
        """Method to search .CSV file by string
         in task names and notes"""
        while True:
            os.system('clear')
            print("Strings Availible to Search:")
            self.search_column = 1
            self.list_values()
            self.search_column = 3
            self.list_values()
            search_string = str(input('\nPlease Use CaSe sEnSiTiVe Text: '))
            if search_string not in self.search_value:
                print("Not an Availible Selection!")
                input("Press ENTER to Try Again!")
                continue
            else:
                self.print_results(search_string)
                input("\nPress ENTER to Return to Main Menu")
                break

    def regex_search(self):
        """Method to search .CSV file by regex patterns
         in task names and notes"""
        while True:
            file = open("data.csv")
            data = file.read()
            file.close()
            os.system('clear')
            print("Select whatever regex or value you wish to search for:")
            print("For example: \d would return Unicode digits from 0 to 9")
            regex_string = input('\nPlease enter a regex or value: ')
            regex_results = (re.findall(regex_string, data))
            regex_results_list = (list(set(regex_results)))
            with open('data.csv', 'rt') as f:
                reader = csv.reader(f)
                returned_values = []
                for row in reader:
                    for field in row:
                        for item in regex_results_list:
                            if item in field:  # Match field to search value
                                if row not in returned_values:  # Prevent Dupes
                                    returned_values.append(row)
            print('\nYou found {} instances of this criterion and {} values!'
                  .format(len(regex_results), len(returned_values)))
            next_step = input('Would you like to see the results? (y/n): ')
            if next_step.lower() == 'n':
                continue
            elif next_step.lower() == 'y':
                os.system('clear')
                print("HERE'S YOUR DATA!!!")
                titles = ['DATE', 'TITLE', 'TIME', 'NOTES']
                for x in returned_values:  # Make list readable
                    dictionary = dict(zip(titles, x))  # Convert to dict
                    for key, value in dictionary.items():
                        print(key + ':', value)
                    print('\n')
                input("\nPress ENTER to Return to Main Menu")
                break
            else:
                continue
