from classes import *

standard_cards = [
	TACard('Rachel, Bringer of Boba', 1200, 2200),
	TutorCard('RichRocks', 2200, 1100),
	TutorCard('Apoλλo, Answerer of Ed', 2400, 1000),
	TutorCard('Ratthew, King of the Rats', 2000, 1000),
	TutorCard('Hans, Compiler of Chaos', 1800, 1500),
	TACard('Cyrus, Cereal Consumer', 1500, 1500),
	TutorCard('jade, jabbering jester', 2299, 1001),
	TutorCard('Arnold, Description Here', 1600, 1600),
	TutorCard('Sophia, Soda Slayer', 1700, 1600),
	AICard('El Shroomster the Lamb, duh!', 1000, 2300),
	TACard('Abby, Queen of Geese', 1800, 1600),
	TutorCard('The λce', 1200, 2000),
	AICard('Amber, Aetherweaver', 2300, 1000),
	TACard('The Ace', 1100, 2100),
	AICard('Bashwat, Brains of the Balawat', 1500, 1800),
	AICard('Henry, Huggable Hipster', 1499, 1501),
	AICard('The Smasher', 1100, 2200),
	TutorCard('Ronald, Recursor of Recursion', 1000, 2300),
	TutorCard('Albs, Ahri Ace', 1700, 1100),
	TACard('Kevin, Random Schmoe Who Is Incredibly Powerful For Some Reason', 2100, 1300),
	TACard('λaryn, λord of λambdas', 1700, 1600),
	AICard('Alexander the Not So Great', 1900, 1500),
	AICard('λnto\'s λI ', 2000, 1000),
	TACard('Kotryna, Chaotic Neutral', 1500, 1600),
	TutorCard('Darlnim, Darklord', 1000, 2300),
	AICard('Jade, Lucky Fool', 1600, 1800),
	AICard('Anshu, Chieftain of Recursion', 2100, 1000),
	AICard('Rudy, Squirrel Whisperer', 1500, 1600),
	TACard('Christina, Stick Breaker', 1900, 1100),
	AICard('Adhvaith Thurvas, Caffeine-Powered Adverserial AI', 1500, 1500),
	TACard('Bryce, Fuzzy Fire Flinger', 1300, 2100),
	AICard('Zattack', 1200, 2000),
	InstructorCard('DeNero, Antihero', 6650, 6650),
	InstructorCard('Rao, Chaotic Wanderer', 0, 10000)
]

standard_deck = Deck(standard_cards)
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()