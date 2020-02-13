
def uno(hand, pile):
    for i in range(len(hand)):
        cards = hand[i]
        print(cards[-1])
        print(pile[-1])

    if cards[:-2] in pile[:-2] or cards[-1] == pile[-1]:
        return True
    else:
        return False

