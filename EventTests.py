import unittest
from Event import Event
from Participant import Participant


class MyTestCase(unittest.TestCase):
    # test that an event can be created
    def test_create_event(self):
        # ARRANGE
        my_event = Event('3x3')
        # ACT
        actual = isinstance(my_event, Event)
        # ASSERT
        self.assertTrue(actual)

    # test that an event can have a participant added to it
    def test_add_participant(self):
        # ARRANGE
        my_event = Event('3x3')
        my_participant = Participant('Bilbo Baggins', 1234)
        expected = 1
        # ACT
        my_event.add_participant(my_participant)
        actual = len(my_event.participants)
        # ASSERT
        self.assertTrue(expected, actual)

    # test that a participant's name will be returned by get_remaining_participants()
    # if they don't have times entered
    def test_get_one_remaining_participant(self):
        # ARRANGE
        my_event = Event('3x3')
        my_participant = Participant('Bilbo Baggins', 1234)
        expected = 'Bilbo Baggins\n'
        # ACT
        my_event.add_participant(my_participant)
        actual = my_event.get_remaining_participants()
        # ASSERT
        self.assertTrue(expected, actual)

    # test that a participant's name will not be returned by get_remaining_participants()
    # if they do have times entered
    def test_get_remaining_participants_none_remaining(self):
        # ARRANGE
        my_event = Event('3x3')
        my_participant = Participant('Bilbo Baggins', 1234)
        expected = 'No participants remaining'
        # ACT
        [my_participant.add_time(5.0) for _ in range(5)]
        my_event.add_participant(my_participant)
        actual = my_event.get_remaining_participants()
        # ASSERT
        self.assertTrue(expected, actual)

    # test that averages can be calculated for all participants in an event
    def test_calc_all_averages(self):
        # ARRANGE
        my_event = Event('3x3')
        my_participants = [Participant('Bilbo Baggins', 1234), Participant('Frodo Baggins', 2345)]
        expected = 2
        # ACT
        [participant.add_time(5.0) for _ in range(5) for participant in my_participants]
        [my_event.add_participant(participant) for participant in my_participants]
        my_event.calc_all_averages()
        actual = len(my_event.finished_participants)
        # ASSERT
        self.assertTrue(expected, actual)

    # test that participants can be sorted by their average time
    def test_sort_participants(self):
        # ARRANGE
        my_event = Event('3x3')
        my_participants = [Participant('Bilbo Baggins', 1234),
                           Participant('Frodo Baggins', 2345),
                           Participant('Samwise Gamgee', 3456)]
        expected = my_participants[0]
        # ACT
        [participant.add_time(time) for _ in range(5) for time, participant in enumerate(my_participants[::-1], 1)]
        [my_event.add_participant(participant) for participant in my_participants]
        my_event.calc_all_averages()
        my_event.sort_participants()
        actual = my_event.finished_participants[0]
        # ASSERT
        self.assertTrue(expected, actual)

    # test printing an event
    def test_print_event(self):
        # ARRANGE
        my_event = Event('3x3')
        my_participants = [Participant('Bilbo Baggins', 1234),
                           Participant('Frodo Baggins', 2345),
                           Participant('Samwise Gamgee', 3456)]
        expected = f'Event Name: 3x3\nParticipants: {[participant.name for participant in my_participants]}'
        # ACT
        [my_event.add_participant(participant) for participant in my_participants]
        actual = str(my_event)
        # ASSERT
        self.assertEqual(expected, actual)
