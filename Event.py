from collections import deque
from Participant import Participant


class Event:
    def __init__(self, name):
        self.name = name
        self.participants = deque()
        self.finished_participants = []

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

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self):
        participant_to_remove = self.participants.popleft()
        self.finished_participants.append(participant_to_remove)
        return participant_to_remove

    def all_times_entered(self):
        for participant in self.participants:
            if not participant.times:
                return False
        return True

    def get_remaining_participants(self):
        remaining_participant_names = ''
        for participant in self.participants:
            if not participant.times:
                remaining_participant_names += f'{participant.name}\n'
        return remaining_participant_names if remaining_participant_names else 'No participants remaining'

    def calc_all_averages(self):
        for participant in self.participants:
            participant.calc_average()
        while self.participants:
            self.remove_participant()

    def sort_participants(self):
        n = len(self.finished_participants)

        for i in range(n):
            for j in range(0, n-i-1):
                if self.finished_participants[j].average > self.finished_participants[j + 1].average:
                    self.finished_participants[j], self.finished_participants[j + 1] = self.finished_participants[j + 1], self.finished_participants[j]

    def __str__(self):
        return f'Event Name: {self._name}\nParticipants: {[participant.name for participant in self.participants]}'

    def __repr__(self):
        return f'Event(name={self._name}, participants={[participant.name for participant in self.participants]})'
