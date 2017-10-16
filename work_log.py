import os

from tasks import Tasks
from searches import Searches


class Main():
    def __init__(self, homescreen="", searchscreen=""):
        self.homescreen = homescreen
        self.searchscreen = searchscreen

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


m = Main()
t = Tasks()
s = Searches()

m.LogLoop()
