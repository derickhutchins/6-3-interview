
import unittest
import random

class Racko(object):

	def deal(self):
		cards = range(1, 51)

		for card in range(10):
			yield cards.pop(random.randint(0, len(cards) - 1))


class RackoTests(unittest.TestCase):

	def setUp(self):
		self.game = Racko()
		self.cards = list(self.game.deal())

	def test_10_cards_are_dealt(self):
		self.assertEqual(10, len(self.cards))

	def test_does_not_contain_any_duplicate_cards(self):
		self.assertEqual(10, len(set(self.cards)))

	def test_is_not_a_range(self):
		self.assertNotEqual(range(10), self.cards)

	def test_cards_are_all_ints(self):
		for card in self.cards:
			self.assertIsInstance(card, int)

	def test_does_not_return_cards_over_50(self):
		for i in range(10):
			cards = list(self.game.deal())
			self.assertTrue(max(cards) < 51)
			self.assertTrue(min(cards) > 0)

	def test_huh(self):
		self.fail(self.cards)


if __name__ == '__main__':
	unittest.main()