from collections import deque


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

    def __str__(self):
        return f'Event Name: {self._name}\nParticipants: {[participant.name for participant in self.participants]}'

    def __repr__(self):
        return f'Event(name={self._name}, participants={[participant.name for participant in self.participants]})'
