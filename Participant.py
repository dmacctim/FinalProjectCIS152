class Participant:
    def __init__(self, name, participant_id):
        self.name = name
        self.participant_id = participant_id
        self.times = []
        self.average = None

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

    def add_time(self, time):
        self.times.append(time)

    def calc_average(self):
        self.average = sum(self.times) / len(self.times)

    def __str__(self):
        return f'Participant Name: {self.name}\nID: {self.participant_id}\nTimes: {self.times}\nAverage Time: {self.average}'

    def __repr__(self):
        return f'Participant(name={self.name}, id={self.participant_id}, times={self.times}, average={self.average})'
