import unittest


class Timer(object):

    def __init__(self, exercises):
        self.data = exercises
        self.start_point = 0

    def get_current_exercises(self):

        if len(self.data) == self.start_point + 1:
            self.start_point = 0
            return [self.data[-1], self.data[0]]

        result = self.data[self.start_point:self.start_point + 2]
        self.start_point += 1
        return result


class TimerTests(unittest.TestCase):

    def test_gets_first_2_exercises(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'])
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())

    def test_gets_next_2_exercises(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'])
        timer.get_current_exercises()
        self.assertEqual(['Pull Ups', 'Burpees'], timer.get_current_exercises())

    def test_does_not_go_past_length(self):
        timer = Timer(['Push Ups', 'Pull Ups'])
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())
        self.assertEqual(['Pull Ups', 'Push Ups'], timer.get_current_exercises())

    def test_resets_start_point_when_rollover(self):
        timer = Timer(['Push Ups', 'Pull Ups'])
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())
        self.assertEqual(['Pull Ups', 'Push Ups'], timer.get_current_exercises())
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())

    def test_resets_start_point_when_rollover(self):
        timer = Timer(['Push Ups', 'Pull Ups', 'Burpees'])
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())
        self.assertEqual(['Pull Ups', 'Burpees'], timer.get_current_exercises())
        self.assertEqual(['Burpees', 'Push Ups'], timer.get_current_exercises())
        self.assertEqual(['Push Ups', 'Pull Ups'], timer.get_current_exercises())
