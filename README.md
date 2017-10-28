Synopsis
In order to prepare better timesheets for your company, you've been asked to develop a terminal application for logging what work someone did on a certain day. The script should ask for a task name, how much time was spent on the task, and any general notes about the task. Record each of these items into a row of a CSV file along with a date.

Provide a way for a user to find all of the tasks that were done on a certain date or that match a search string (either as a regular expression or a plain text search). Print a report of this information to the screen, including the date, title of task, time spent, and general notes.


Code Example

The code library contains 1 application that refers to multiple classes for entering and searching for data within a .CSV file.

The application itself is comprised of a homescreen and a search screen below:

    def HomeScreen(self):
        """Displays all availlible options for
         interfacing with the terminal application"""
        while True:
            os.system('clear')
            print("WORK LOG")
            print("What Would You Like to Do?")
            print("a) Add New Entry")
            print("b) Search in Existing Entries")
            print("c) Quit Program")
            self.homescreen = input("\n>>> ").lower()
            if self.homescreen not in ["a", "b", "c"]:
                continue
            else:
                return self.homescreen
                break

    def SearchScreen(self):
        """Displays all availible options for
         searching the CSV file"""
        while True:
            os.system('clear')
            print("What Parameter Do You Want to Search?")
            print("a) Exact Date")
            print("b) Time Spent (Rounded Minutes)")
            print("c) Title or Notes Assocated with Task")
            print("d) Regex Pattern")
            print("e) Return to Menu")
            self.searchscreen = input("\n>>> ").lower()
            if self.searchscreen not in ["a", "b", "c", "d", "e"]:
                continue
            else:
                return self.searchscreen
                break

The application is then run through the following while loop.

    def LogLoop(self):
        """Runs the application log loop"""
        while True:
            homescreen = m.HomeScreen()
            if homescreen == 'a':
                t.input_date()
                t.input_title()
                t.input_time()
                t.input_notes()
                t.write_to_file()
                continue
            elif homescreen == 'b':
                searchscreen = m.SearchScreen()
                if searchscreen == 'a':
                    s.date_search()
                    continue
                elif searchscreen == 'b':
                    s.time_search()
                    continue
                elif searchscreen == 'c':
                    s.string_search()
                    continue
                elif searchscreen == 'd':
                    s.regex_search()
                    continue
                if searchscreen == 'e':
                    homescreen
                else:
                    continue
            elif homescreen == 'c':
                os.system('clear')
                print("Thanks for Using the Work Log Program!")
                print("Come Again Soon!\n")
                break
            else:
                break

The tasks class is meant for data entry with a method for each type of data entry (i.e. date)

    def input_date(self):
        """Prompts user to add a date to the .CSV file"""
        try:
            os.system('clear')
            print("Exact Date of the task")
            task_date = input('Please use DD/MM/YYYY: ')
            datetime.datetime.strptime(task_date, '%d/%m/%Y')
        except ValueError:
            print("ValueError: Incorrect data format. Please use DD/MM/YYYY")
            input("Press ENTER to try again")
            self.input_date()
        else:
            self.csv_row.append(task_date)

The searches class is meant for and retrieval of data from the .CSV (i.e date)

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

**Critical to the success of the searches class are two methods**

1 - The List Values Method which spans any instance of the class which shows the values within a column in the .CSV file.

    def list_values(self):
        """Shows the user the availible values to search
         based on selected search type"""
        csv_file = csv.reader(open('data.csv', "r"))
        data_elements = ''
        self.search_value = []
        for row in csv_file:
            data_elements = list(
                row[column] for column in [int(self.search_column)])
            self.search_value.append(data_elements[0])
            print(data_elements[0])

2 - The print results method that finds the data within the .CSV and returns the list record value as a dictionary which can easily be converted into plain text.

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


Motivation

The motivation for this project was to be able to log data to a .CSV file and then be able to search the contents via multiple data types and search conditions using object oriented programming as well regular expressions and date time data validation.

Installation

To install the project download all files to a location of your choosing on your computer, log into the terminal (on a MAC) and instantiate the program from the directory where you stored the files as follows:

python3 -i work_log.py


Tests

To test this application choose the option to enter data and then search that data set using the multiple options availible to the user. Verify that you are able to find your data set (and others) The program will give you the option to continue or exit thereafter.


Contributors

This project was inspired by the teachers at teamtreehouse.com and was developed by Taylor. This code as been tested by flake8 PEP8 standards and passes the programmatic testing of all files associated with this application.


License

Opensource for your enjoyment!