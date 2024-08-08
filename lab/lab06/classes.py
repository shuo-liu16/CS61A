# Magic the Lambda-ing!

import random

class Card:
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        """
        Create a Card object with a name, attack,
        and defense.
        >>> staff_member = Card('staff', 400, 300)
        >>> staff_member.name
        'staff'
        >>> staff_member.attack
        400
        >>> staff_member.defense
        300
        >>> other_staff = Card('other', 300, 500)
        >>> other_staff.attack
        300
        >>> other_staff.defense
        500
        """
        "*** YOUR CODE HERE ***"

    def power(self, opponent_card):
        """
        Calculate power as:
        (player card's attack) - (opponent card's defense)
        >>> staff_member = Card('staff', 400, 300)
        >>> other_staff = Card('other', 300, 500)
        >>> staff_member.power(other_staff)
        -100
        >>> other_staff.power(staff_member)
        0
        >>> third_card = Card('third', 200, 400)
        >>> staff_member.power(third_card)
        0
        >>> third_card.power(staff_member)
        -100
        """
        "*** YOUR CODE HERE ***"


    def effect(self, opponent_card, player, opponent):
        """
        Cards have no default effect.
        """
        return

    def __repr__(self):
        """
        Returns a string which is a readable version of
        a card, in the form:
        <cardname>: <cardtype>, [<attack>, <defense>]
        """
        return '{}: {}, [{}, {}]'.format(self.name, self.cardtype, self.attack, self.defense)

    def copy(self):
        """
        Returns a copy of this card.
        """
        return Card(self.name, self.attack, self.defense)

class Player:
    def __init__(self, deck, name):
        """Initialize a Player object.
        A Player starts the game by drawing 5 cards from their deck. Each turn,
        a Player draws another card from the deck and chooses one to play.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> len(test_deck.cards)
        1
        >>> len(test_player.hand)
        5
        """
        self.deck = deck
        self.name = name
        "*** YOUR CODE HERE ***"

    def draw(self):
        """Draw a card from the player's deck and add it to their hand.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> test_player.draw()
        >>> len(test_deck.cards)
        0
        >>> len(test_player.hand)
        6
        """
        assert not self.deck.is_empty(), 'Deck is empty!'
        "*** YOUR CODE HERE ***"

    def play(self, index):
        """Remove and return a card from the player's hand at the given INDEX.
        >>> from cards import *
        >>> test_player = Player(standard_deck, 'tester')
        >>> ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
        >>> tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
        >>> test_player.hand = [ta1, ta2, tutor1, tutor2]
        >>> test_player.play(0) is ta1
        True
        >>> test_player.play(2) is tutor2
        True
        >>> len(test_player.hand)
        2
        """
        "*** YOUR CODE HERE ***"


    def display_hand(self):
        """
        Display the player's current hand to the user.
        """
        print('Your hand:')
        for card_index, displayed_card in zip(range(len(self.hand)),[str(card) for card in self.hand]):
            indent = ' '*(5 - len(str(card_index)))
            print(card_index, indent + displayed_card)

    def play_random(self):
        """
        Play a random card from hand.
        """
        return self.play(random.randrange(len(self.hand)))

######################
# Optional Questions #
######################

class AICard(Card):
    cardtype = 'AI'

    def effect(self, opponent_card, player, opponent):
        """
        Add the top two cards of your deck to your hand via drawing.
        Once you have finished writing your code for this problem,
        set implemented to True so that the text is printed when
        playing an AICard.

        >>> from cards import *
        >>> player1, player2 = Player(standard_deck.copy(), 'p1'), Player(standard_deck.copy(), 'p2')
        >>> opponent_card = Card("other", 500, 500)
        >>> test_card = AICard("AI Card", 500, 500)
        >>> initial_deck_length = len(player1.deck.cards)
        >>> initial_hand_size = len(player1.hand)
        >>> test_card.effect(opponent_card, player1, player2)
        AI Card allows me to draw two cards!
        >>> initial_hand_size == len(player1.hand) - 2
        True
        >>> initial_deck_length == len(player1.deck.cards) + 2
        True
        """
        "*** YOUR CODE HERE ***"
        implemented = False
        # You should add your implementation above this.
        if implemented:
            print(f"{self.name} allows me to draw two cards!")

    def copy(self):
        """
        Create a copy of this card.
        """
        return AICard(self.name, self.attack, self.defense)

class TutorCard(Card):
    cardtype = 'Tutor'

    def effect(self, opponent_card, player, opponent):
        """
        Add a copy of the first card in your hand
        to your hand, at the cost of losing the current
        round. If there are no cards in hand, this card does
        not add any cards, but still loses the round.  To
        implement the second part of this effect, a Tutor
        card's power should be less than all non-Tutor cards.

        >>> from cards import *
        >>> player1, player2 = Player(standard_deck.copy(), 'p1'), Player(standard_deck.copy(), 'p2')
        >>> opponent_card = Card("other", 500, 500)
        >>> test_card = TutorCard("Tutor Card", 10000, 10000)
        >>> player1.hand = [Card("card1", 0, 100), Card("card2", 100, 0)]
        >>> test_card.effect(opponent_card, player1, player2)
        Tutor Card allows me to add a copy of a card to my hand!
        >>> print(player1.hand)
        [card1: Staff, [0, 100], card2: Staff, [100, 0], card1: Staff, [0, 100]]
        >>> player1.hand[0] is player1.hand[2] # must add a copy!
        False
        >>> player1.hand = []
        >>> test_card.effect(opponent_card, player1, player2)
        >>> print(player1.hand) # must not add a card if not available
        []
        >>> test_card.power(opponent_card) < opponent_card.power(test_card)
        True
        """
        "*** YOUR CODE HERE ***"
        added = False
        # You should add your implementation above this.
        if added:
            print(f"{self.name} allows me to add a copy of a card to my hand!")

    "*** YOUR CODE HERE ***"


    def copy(self):
        """
        Create a copy of this card.
        """
        return TutorCard(self.name, self.attack, self.defense)

class TACard(Card):
    cardtype = 'TA'

    def effect(self, opponent_card, player, opponent, arg=None):
        """
        Discard the card with the highest `power` in your hand,
        and add the discarded card's attack and defense
        to this card's own respective stats.

        >>> from cards import *
        >>> player1, player2 = Player(standard_deck.copy(), 'p1'), Player(standard_deck.copy(), 'p2')
        >>> opponent_card = Card("other", 500, 500)
        >>> test_card = TACard("TA Card", 500, 500)
        >>> player1.hand = []
        >>> test_card.effect(opponent_card, player1, player2) # if no cards in hand, no effect.
        >>> print(test_card.attack, test_card.defense)
        500 500
        >>> player1.hand = [Card("card1", 0, 100), TutorCard("tutor", 10000, 10000), Card("card3", 100, 0)]
        >>> test_card.effect(opponent_card, player1, player2) # must use card's power method.
        TA Card discards card3 from my hand to increase its own power!
        >>> print(player1.hand)
        [card1: Staff, [0, 100], tutor: Tutor, [10000, 10000]]
        >>> print(test_card.attack, test_card.defense)
        600 500
        """
        "*** YOUR CODE HERE ***"
        best_card = None
        # You should add your implementation above this.
        if best_card:
            print(f"{self.name} discards {best_card.name} from my hand to increase its own power!")


    def copy(self):
        """
        Create a copy of this card.
        """
        return TACard(self.name, self.attack, self.defense)

class InstructorCard(Card):
    cardtype = 'Instructor'

    def effect(self, opponent_card, player, opponent, arg=None):
        """
        Survives multiple rounds, as long as it has a non-negative
        attack or defense at the end of a round. At the beginning of the round,
        its attack and defense are permanently reduced by 1000 each.
        If this card would survive, it is added back to the hand.

        >>> from cards import *
        >>> player1, player2 = Player(standard_deck.copy(), 'p1'), Player(standard_deck.copy(), 'p2')
        >>> opponent_card = Card("other", 500, 500)
        >>> test_card = InstructorCard("Instructor Card", 1000, 1000)
        >>> player1.hand = [Card("card1", 0, 100)]
        >>> test_card.effect(opponent_card, player1, player2)
        Instructor Card returns to my hand!
        >>> print(player1.hand) # survives with non-negative attack
        [card1: Staff, [0, 100], Instructor Card: Instructor, [0, 0]]
        >>> player1.hand = [Card("card1", 0, 100)]
        >>> test_card.effect(opponent_card, player1, player2)
        >>> print(player1.hand)
        [card1: Staff, [0, 100]]
        >>> print(test_card.attack, test_card.defense)
        -1000 -1000
        """
        "*** YOUR CODE HERE ***"
        re_add = False
        # You should add your implementation above this.
        if re_add:
            print(f"{self.name} returns to my hand!")

    def copy(self):
        return InstructorCard(self.name, self.attack, self.defense)


########################################
# Do not edit anything below this line #
########################################

class Deck:
    def __init__(self, cards):
        """
        With a list of cards as input, create a deck.
        This deck should keep track of the cards it contains, and
        we should be able to draw from the deck, taking a random
        card out of it.
        """
        self.cards = cards

    def draw(self):
        """
        Pick a random card from the deck and remove it from the deck.
        """
        assert self.cards, 'The deck is empty!'
        rand_index = random.randrange(len(self.cards))
        return self.cards.pop(rand_index)

    def is_empty(self):
        return len(self.cards) == 0

    def copy(self):
        """
        Create a copy of this deck.
        """
        return Deck([card.copy() for card in self.cards])

class Game:
    win_score = 8

    def __init__(self, player1, player2):
        """
        Initialize a game of Magic: the Lambda-ing.
        """
        self.player1, self.player2 = player1, player2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, p1_card, p2_card):
        """
        After each player picks a card, play them against
        each other.
        """
        p1_card.effect(p2_card, self.player1, self.player2)
        p2_card.effect(p1_card, self.player2, self.player1)
        p1_power = p1_card.power(p2_card)
        p2_power = p2_card.power(p1_card)
        if p1_power > p2_power:
            # Player 1 wins the round.
            self.p1_score += 1
            result = 'won'
        elif p2_power > p1_power:
            # Player 2 wins the round.
            self.p2_score += 1
            result = 'lost'
        else:
            # This round is a draw.
            result = 'tied'
        # Display results to user.
        print('You {} this round!'.format(result))
        print('{}\'s card: {}; Power: {}'.format(self.player1.name, p1_card, p1_power))
        print('Opponent\'s card: {}; Power: {}'.format(p2_card, p2_power))

    def game_won(self):
        """
        Check if the game is won and, if so,
        which player won.
        """
        if self.p1_score < self.win_score and self.p2_score < self.win_score:
            return 0
        return 1 if self.p1_score > self.p2_score else 2

    def display_scores(self):
        """
        Display players' scores to the user.
        """
        print('{}\'s score: {}'.format(self.player1.name, self.p1_score))
        print('Opponent\'s score: {}'.format(self.p2_score))