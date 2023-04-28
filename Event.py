# ***************************************************************
# Name : Event Class
# Author: Tim Ancona
# Created : 4/2/2023
# Course: CIS 152 - Data Structures
# Version: 1.0
# OS: Windows 11
# IDE: Pycharm 2022.3.1
# Copyright : This is my own original work
# based on specifications issued by our instructor
# Description : This is the class for the cubing events.
#            Input: none
#            Output: none
# Academic Honesty: I attest that this is my original work.
# I have not used unauthorized source code, either modified or
# unmodified. I have not given other fellow student(s) access
# to my program.
# ***************************************************************
from collections import deque


class Event:
    def __init__(self, name):
        self.name = name  # the name of the event
        self.participants = deque()  # queue for participants
        self.finished_participants = []  # list of finished participants after their averages have been calculated

    # properties for class
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value):
        self._participants = value

    @property
    def finished_participants(self):
        return self._finished_participants

    @finished_participants.setter
    def finished_participants(self, value):
        self._finished_participants = value

    # adds a participant to the queue
    def add_participant(self, participant):
        self.participants.append(participant)

    # removes a participant from the queue, places them in the finished participants list
    def remove_participant(self):
        participant_to_remove = self.participants.popleft()
        self.finished_participants.append(participant_to_remove)
        return participant_to_remove

    # returns true if all participants have their times entered, false if not
    def all_times_entered(self):
        for participant in self.participants:
            if not participant.times:
                return False
        return True

    # returns a list of all remaining participants (who don't have times entered)
    # returns a message indicating none are remaining otherwise
    def get_remaining_participants(self):
        remaining_participant_names = ''
        for participant in self.participants:
            if not participant.times:
                remaining_participant_names += f'{participant.name}\n'
        return remaining_participant_names if remaining_participant_names else 'No participants remaining'

    # calculates the averages of all the participants and removes each one from the queue
    def calc_all_averages(self):
        for participant in self.participants:
            participant.calc_average()
        while self.participants:
            self.remove_participant()

    # sorts the participants by their average time
    def sort_participants(self):
        n = len(self.finished_participants)

        for i in range(n):
            for j in range(0, n-i-1):
                if self.finished_participants[j + 1].average == 'DNF':
                    continue
                if self.finished_participants[j].average == 'DNF' or self.finished_participants[j].average > self.finished_participants[j + 1].average:
                    self.finished_participants[j], self.finished_participants[j + 1] = self.finished_participants[j + 1], self.finished_participants[j]

    # display methods for class
    def __str__(self):
        return f'Event Name: {self._name}\nParticipants: {[participant.name for participant in self.participants]}'

    def __repr__(self):
        return f'Event(name={self._name}, participants={[participant.name for participant in self.participants]})'
