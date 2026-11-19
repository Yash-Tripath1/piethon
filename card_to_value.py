'''
Card to Value Tuple
Problem statement

Write a function card_to_value_tuple(card) that accepts a playing card as a string and converts it into a numeric tuple.

For example:
card_to_value_tuple('10D')# (3, 10)



The returned tuple must contain:

(suit_value, rank_value)

Suit mapping
Suit	Value
S (Spades)	1
H (Hearts)	2
D (Diamonds)	3
C (Clubs)	4

Rank mapping
Rank	Value
A	1
2–10	Their integer values
J	11
Q	12
K	13

Important: The rank can have variable length. For example, A has one character, whereas 10 has two. The final character always represents the suit.
'''

def card_to_value_tuple(card):
    suit=card[-1]
    rank=card[:-1]

    suits={
        "S": 1,
        "H": 2,
        "D": 3,
        "C": 4    
    }
    ranks = {
        "A": 1,
        "J": 11,
        "Q": 12,
        "K": 13
    }
    # Get suit value
    suit_value = suits[suit]

        # Get rank value
    if rank in ranks:
        rank_value = ranks[rank]
    else:
        rank_value = int(rank)

    return (suit_value, rank_value)

# Testing the function
print(card_to_value_tuple("10D"))
print(card_to_value_tuple("QH"))
print(card_to_value_tuple("AS"))
print(card_to_value_tuple("7C"))
    