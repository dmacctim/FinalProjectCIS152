from queue import Queue


class Event:
    def __init__(self, name):
        self.name = name
        self.participants = Queue()

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

    def add_participant(self, participant):
        self.participants.enqueue(participant)

    def remove_participant(self, participant):
        self.participants.dequeue(participant)

    def __str__(self):
        return f'Event Name: {self._name}\nParticipants: {self._participants}'

    def __repr__(self):
        return f'Event(name={self._name}, participants={self._participants})'
