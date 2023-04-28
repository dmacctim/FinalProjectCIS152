# ***************************************************************
# Name : Final Project CIS 152
# Author: Tim Ancona
# Created : 4/2/2023
# Course: CIS 152 - Data Structures
# Version: 1.0
# OS: Windows 11
# IDE: Pycharm 2022.3.1
# Copyright : This is my own original work
# based on specifications issued by our instructor
# Description : This program is used for Rubik's Cubing
#               competitions. An event exists for each type of
#               cube, and participants can be added to the events.
#               Their times can be entered, and after all
#               participants have competed, a winner can be
#               determined for each event.
#            Input: participants and their times
#            Output: winners of each event
# Academic Honesty: I attest that this is my original work.
# I have not used unauthorized source code, either modified or
# unmodified. I have not given other fellow student(s) access
# to my program.
# ***************************************************************
from App import App


if __name__ == '__main__':
    app = App()
    app.main_window.mainloop()
