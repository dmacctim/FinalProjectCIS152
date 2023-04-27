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

    def __str__(self):
        return f'Participant Name: {self.name}\nID: {self.participant_id}\nTimes: {self.times}\nAverage Time: {self.average}'

    def __repr__(self):
        return f'Participant(name={self.name}, id={self.participant_id}, times={self.times}, average={self.average})'
