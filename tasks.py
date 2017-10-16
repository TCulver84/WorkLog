import os
import datetime


class Tasks:
    """Contains all applicable methods and variables
     applicable to data entry"""

    def __init__(self):
        self.csv_row = []

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

    def input_title(self):
        """Prompts user to add a title to the .CSV file"""
        os.system('clear')
        task_title = str(input('Title of the task: ')).title()
        self.csv_row.append(task_title)

    def input_time(self):
        """Prompts user to add a time to the .CSV file"""
        try:
            os.system('clear')
            task_time = input('Time spent (rounded minutes): ')
            int(task_time)
        except ValueError:
            print('ValueError: {} is not an integer'.format(task_time))
            input("Press ENTER to try again")
            self.input_time()
        else:
            self.csv_row.append(task_time)

    def input_notes(self):
        """Prompts user to add a note to the .CSV file"""
        os.system('clear')
        task_notes = input('Notes (Optional, you can leave this empty): ')
        self.csv_row.append(task_notes)

    def write_to_file(self):
        """Writes input selections to the .CSV file"""
        os.system('clear')
        input("The entry has been added. Press enter to return to the menu")
        with open('data.csv', 'a') as file:
            file.write('{}\n'.format(','.join(self.csv_row)))
            self.csv_row = []
