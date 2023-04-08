class Participant:
    def __init__(self, name, participant_id):
        self.name = name
        self.participant_id = participant_id
        self.scores = []
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
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, value):
        self._scores = value

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, value):
        self._average = value

    def add_score(self, score):
        self.scores.append(score)

    def calc_average(self):
        self.average = sum(self.scores) / len(self.scores)

    def __str__(self):
        return f'Participant Name: {self.name}\nID: {self.participant_id}\nScores: {self.scores}\nAverage Score: {self.average}'

    def __repr__(self):
        return f'Participant(name={self.name}, id={self.participant_id}, scores={self.scores}, average={self.average})'
