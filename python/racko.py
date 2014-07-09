
import unittest
import random

class Racko(object):
	#Automatically plays a terrible game of Racko.

	def __init__(self):
    		self.cards = range(1, 51)
    		random.shuffle(self.cards)
    		self.hand = list(self.deal())
    		self.discard = []

	def deal(self):

		for card in range(10):
			yield self.cards.pop(random.randint(0, len(self.cards) - 1))

	def draw_card(self, pile):
		#Returns card value if cards are still in the deck. If not returns -1.
		if(len(pile) > 0):
			return pile.pop(0)
		else:
			return -1

	def place_card(self, card, hand):
		#Tries placing card in hand. Returns index of card replaced if successful. Otherwise returns -1.
		index = 0

		while index < len(hand):
			if index == 0:
				if card < hand[index]:
					return index
			else:
				if hand[index] < hand[index-1] or card < hand[index]:
					return index
			index += 1

		return -1

	def discard_card(self, card):
		self.discard.insert(0, card)

	def replace_card(self, index, newCard):
		oldCard = self.hand[index]
		self.hand[index] = newCard
		self.discard_card(oldCard)

	def hand_in_ascending_order(self, hand):
		for i in xrange(len(hand) -1):
			if hand[i] > hand[i + 1]:
				return False
		return True

	def play(self):
		#Setup discard pile
		self.discard_card(self.draw_card(self.cards))

		#Main Game Loop
		racko = False
		turns = 0

		while racko == False:

			card = self.discard[0]
			index = self.place_card(card, self.hand)
			#If spot found for discard pile card
			if index != -1:
				self.replace_card(index, card)
				self.discard.pop()
			#Otherwise draw a card from deck and try placing it
			else:
				card = self.draw_card(self.cards)
				index = self.place_card(card, self.hand)
				#Able to place card
				if index != -1:
					self.replace_card(index, card)
				#Place drawn card into discard
				else:
					self.discard_card(card)

			turns += 1
			print "\nTurn: {0} {1}".format(turns, self.hand)
			racko = self.hand_in_ascending_order(self.hand)
			
		print "\nRacko in {0} turns. {1}".format(turns, self.hand)
		return self.hand

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

	def test_hand_is_ascending(self):
		asc = range(10)
		self.assertTrue(self.game.hand_in_ascending_order(asc))

	def test_non_ascending_hand(self):
		badHand = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
		self.assertFalse(self.game.hand_in_ascending_order(badHand))

	def test_cards_are_all_ints(self):
		for card in self.cards:
			self.assertIsInstance(card, int)

	def test_does_not_return_cards_over_50(self):
		for i in range(10):
			self.assertTrue(max(self.cards) < 51)
			self.assertTrue(min(self.cards) > 0)

	def test_play(self):
		rackoHand = self.game.play()
		self.assertTrue(self.game.hand_in_ascending_order(rackoHand))

	def test_huh(self):
		self.fail(self.cards)

if __name__ == '__main__':
	unittest.main()
