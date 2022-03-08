import Cards


def cards_assigner(cards):
    clubs = []
    hearts = []
    diamonds = []
    spades = []
    ace_clubs = []
    ace_hearts = []
    ace_diamonds = []
    ace_spades = []
    face_clubs = []
    face_hearts = []
    face_diamonds = []
    face_spades = []
    sample = cards
    # Sort the cards in ascending order
    # and return the sorted list
    for a in sample:
        if a[1] == 'C':
            if a == '1C':
                ace_clubs.append(a)
            elif a == 'JC' or a == 'QC' or a == 'KC':
                face_clubs.append(a)
            else:
                clubs.append(a)
        elif a[1] == 'H':
            if '1H' in a:
                ace_hearts.append(a)
            elif 'JH' in a or 'QH' in a or 'KH' in a:
                face_hearts.append(a)
            else:
                hearts.append(a)
        elif a[1] == 'D':
            if '1D' in a:
                ace_diamonds.append(a)
            elif 'JD' in a or 'QD' in a or 'KD' in a:
                face_diamonds.append(a)
            else:
                diamonds.append(a)
        elif a[1] == 'S':
            if '1S' in a:
                ace_spades.append(a)
            elif 'JS' in a or 'QS' in a or 'KS' in a:
                face_spades.append(a)
            else:
                spades.append(a)
    clubs = ace_clubs + face_clubs + sorted(clubs)
    hearts = ace_hearts + face_hearts + sorted(hearts)
    diamonds = ace_diamonds + face_diamonds + sorted(diamonds)
    spades = ace_spades + face_spades + sorted(spades)
    dictionary = {'clubs': clubs, 'hearts': hearts, 'diamonds': diamonds, 'spades': spades}
    return dictionary


def card_sort(cards):
    clubs = cards_assigner(cards)['clubs']
    spades = cards_assigner(cards)['spades']
    diamonds = cards_assigner(cards)['diamonds']
    hearts = cards_assigner(cards)['hearts']
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
    list1.reverse()
    for i in list1:
        list2 = list2 + dictionary[i]
    return spades + list2


def get_played_cards(card_name):
    return card_name[0:2]


def logic(played, cards, history):
    spades = []
    clubs = []
    diamonds = []
    hearts = []
    total_cards = cards_assigner(cards)
    spades = total_cards['spades']
    clubs = total_cards['clubs']
    diamonds = total_cards['diamonds']
    hearts = total_cards['hearts']
    playables = []
    overall_history = []
    cards_arranged = card_sort(cards)
    for dash in history:
        overall_history += dash[1]
    history_sorted = card_sort(overall_history)
    if played == []:
        if history == []:
            if '1S' in cards and 'KS' in cards and 'QS' in cards:
                play = '1S'
            else:
                play = card_sort(cards)[0]
        elif history != []:
            """
            In this case tho, we need to have a list of the cards that have been played throughout the game.
            """
            pass
    elif played != []:
        if history == []:
            """
            In this case tho, we need to have a list of the cards that have been played throughout the game.
            """
            pass
        elif history != []:
            played_cards = list(map(get_played_cards, played))
            play_sorted = card_sort(played_cards)
            total_played = card_sort(overall_history + played_cards)
            sign_of_the_card = played_cards[0][1]
            for c in cards:
                if c[1] == sign_of_the_card:
                    playables.append(c)
            if len(playables) < 1:
                if spades != []:
                    playable = [spades[-1]]
                else:
                    try:
                        playables = list(i for i in cards if Cards.value[i] <= 5)
                    except:
                        playables = list(cards_arranged[-1])
