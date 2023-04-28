# ***************************************************************
# Name : Participant Class
# Author: Tim Ancona
# Created : 4/2/2023
# Course: CIS 152 - Data Structures
# Version: 1.0
# OS: Windows 11
# IDE: Pycharm 2022.3.1
# Copyright : This is my own original work
# based on specifications issued by our instructor
# Description : This is the class for the event participants.
#            Input: none
#            Output: none
# Academic Honesty: I attest that this is my original work.
# I have not used unauthorized source code, either modified or
# unmodified. I have not given other fellow student(s) access
# to my program.
# ***************************************************************
class Participant:
    def __init__(self, name, participant_id):
        self.name = name  # name of the participant
        self.participant_id = participant_id  # ID number of the participant
        self.times = []  # a list of the times for the participant
        self.average = None  # the average time for the participant

    # properties for class
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value

    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, value):
        self._times = value

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, value):
        self._average = value

    # adds a time for the participant
    def add_time(self, time):
        self.times.append(time)

    # calculates the average time for the participant, factoring in whether they have any 'DNF' times
    def calc_average(self):
        if self.times.count('DNF') > 1:
            self.average = 'DNF'
        elif self.times.count('DNF') == 1:
            times_for_calc = self.times
            times_for_calc.remove('DNF')
            times_for_calc.remove(min(times_for_calc))
            self.average = sum(times_for_calc) / len(times_for_calc)
        else:
            times_for_calc = self.times.copy()
            times_for_calc.remove(min(self.times))
            times_for_calc.remove(max(times_for_calc))
            self.average = sum(times_for_calc) / len(times_for_calc)

    # display methods for class
    def __str__(self):
        return f'Participant Name: {self.name}\nID: {self.participant_id}\nTimes: {self.times}\nAverage Time: {self.average}'

    def __repr__(self):
        return f'Participant(name={self.name}, id={self.participant_id}, times={self.times}, average={self.average})'
