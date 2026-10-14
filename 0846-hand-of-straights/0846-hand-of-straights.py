class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # deny if length of hand can not be divided by group size equally - > we can use a modulus opertion to confrim

        # do we want to sort? or process via a hashmap we could do a longest conqeuventive sub arrary thing.
        # but then how do we remove it from da index - > lets do hashmap

        # hash map works but in the f

        cards = {}

        n = len(hand)

        if n % groupSize != 0:
            return False
        
        for card in hand:
            cards[card] = cards.get(card, 0) + 1 

        
        
        for card in sorted(cards):
            if cards[card] > 0: 
                card_num = cards[card]
                counter = 1
                while counter < groupSize:
                    if card + counter in cards:
                        if cards[card + counter] < card_num:
                            return False 
                        cards[card + counter] -= card_num
                        counter += 1
                    else:
                        return False
                cards[card] -= 1
        return True

        




