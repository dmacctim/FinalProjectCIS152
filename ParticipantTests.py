import unittest
from Participant import Participant


class MyTestCase(unittest.TestCase):
    # test that a participant can be created
    def test_create_participant(self):
        # ARRANGE
        my_participant = Participant('Bilbo Baggins', 1234)
        # ACT
        actual = isinstance(my_participant, Participant)
        # ASSERT
        self.assertTrue(actual)

    # test that a participant can have their times entered
    def test_input_times(self):
        # ARRANGE
        my_participant = Participant('Bilbo Baggins', 1234)
        times = (5.00, 10.00, 15.00, 20.00, 25.00)
        expected = list(times)
        # ACT
        [my_participant.add_time(time) for time in times]
        actual = my_participant.times
        # ASSERT
        self.assertEqual(expected, actual)

    # test that a participant can have 'DNF' entered into their times
    def test_can_enter_DNF_as_time(self):
        # ARRANGE
        my_participant = Participant('Bilbo Baggins', 1234)
        times = (5.00, 10.00, 15.00, 'DNF', 25.00)
        expected = list(times)
        # ACT
        [my_participant.add_time(time) for time in times]
        actual = my_participant.times
        # ASSERT
        self.assertEqual(expected, actual)

    # test that a participant's average can be calculated
    def test_calc_average(self):
        # ARRANGE
        my_participant = Participant('Bilbo Baggins', 1234)
        times = (5.00, 10.00, 15.00, 20.00, 25.00)
        expected = 15.00
        # ACT
        [my_participant.add_time(time) for time in times]
        my_participant.calc_average()
        actual = my_participant.average
        # ASSERT
        self.assertEqual(expected, actual)

    # test that an average can still be calculated with one 'DNF' time
    def test_calc_average_with_one_DNF(self):
        # ARRANGE
        my_participant = Participant('Bilbo Baggins', 1234)
        times = (5.00, 10.00, 15.00, 'DNF', 20.00)
        expected = 15.00
        # ACT
        [my_participant.add_time(time) for time in times]
        my_participant.calc_average()
        actual = my_participant.average
        # ASSERT
        self.assertEqual(expected, actual)

    # test that an average will be calculated as 'DNF' if there is more than one 'DNF' time
    def test_calc_average_with_more_than_one_DNF(self):
        # ARRANGE
        my_participant = Participant('Bilbo Baggins', 1234)
        times = (5.00, 10.00, 15.00, 'DNF', 'DNF')
        expected = 'DNF'
        # ACT
        [my_participant.add_time(time) for time in times]
        my_participant.calc_average()
        actual = my_participant.average
        # ASSERT
        self.assertEqual(expected, actual)

    # test printing a participant
    def test_print_participant(self):
        # ARRANGE
        my_participant = Participant('Bilbo Baggins', 1234)
        times = (5.00, 10.00, 15.00, 20.00, 25.00)
        [my_participant.add_time(time) for time in times]
        my_participant.calc_average()
        expected = 'Participant Name: Bilbo Baggins\nID: 1234\nTimes: [5.0, 10.0, 15.0, 20.0, 25.0]\nAverage Time: 15.0'
        # ACT
        actual = str(my_participant)
        # ASSERT
        self.assertEqual(expected, actual)
