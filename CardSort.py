def card_sort(cards):
    clubs = []
    hearts = []
    diamonds = []
    spades = []
    new_deck = []
    # Sort the cards in ascending order
    # and return the sorted list
    for a in cards:
        if 'C' in a:
            clubs.append(a)
        elif 'H' in a:
            hearts.append(a)
        elif 'D' in a:
            diamonds.append(a)
        elif 'S' in a:
            spades.append(a)
    list2 = []

    c = str(len(clubs)) + 'C'
    h = str(len(hearts)) + 'H'
    d = str(len(diamonds)) + 'D'
    dictionary = {
        c: clubs,
        h: hearts,
        d: diamonds,
    }
    list1 = [c, h, d]
    list1.sort()
    for i in list1:
        list2 = list2 + dictionary[i]
    return list2 + spades
