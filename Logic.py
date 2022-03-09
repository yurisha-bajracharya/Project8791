import Cards


def get_plays(sign, played):
    a = []
    for i in played:
        if sign in i:
            a.append(i)
    return a


def cards_assigner(cards):
    """
    This function assigns cards of different suits to different lists and adds them to a dictionary.
    """
    clubs = []
    hearts = []
    diamonds = []
    spades = []
    ace_clubs = []
    ace_hearts = []
    ace_diamonds = []
    ace_spades = []
    jack_clubs = []
    jack_hearts = []
    jack_diamonds = []
    jack_spades = []
    queen_clubs = []
    queen_hearts = []
    queen_diamonds = []
    queen_spades = []
    king_clubs = []
    king_hearts = []
    king_diamonds = []
    king_spades = []
    sample = cards
    # Sort the cards in ascending order
    # and return the sorted list
    for a in sample:
        if a[1] == 'C':
            if a == '1C':
                ace_clubs.append(a)
            elif a == 'JC':
                jack_clubs.append(a)
            elif a == 'QC':
                queen_clubs.append(a)
            elif a == 'KC':
                king_clubs.append(a)
            else:
                clubs.append(a)
        elif a[1] == 'H':
            if '1H' in a:
                ace_hearts.append(a)
            elif 'JH' in a:
                jack_hearts.append(a)
            elif 'QH' in a:
                queen_hearts.append(a)
            elif 'KH' in a:
                king_hearts.append(a)
            else:
                hearts.append(a)
        elif a[1] == 'D':
            if '1D' in a:
                ace_diamonds.append(a)
            elif 'JD' in a:
                jack_diamonds.append(a)
            elif 'QD' in a:
                queen_diamonds.append(a)
            elif 'KD' in a:
                king_diamonds.append(a)
            else:
                diamonds.append(a)
        elif a[1] == 'S':
            if '1S' in a:
                ace_spades.append(a)
            elif 'JS' in a:
                jack_spades.append(a)
            elif 'QS' in a:
                queen_spades.append(a)
            elif 'KS' in a:
                king_spades.append(a)
            else:
                spades.append(a)
    clubs = ace_clubs + king_clubs + queen_clubs + jack_clubs + list(reversed(sorted(clubs)))
    hearts = ace_hearts + king_hearts + queen_hearts + jack_hearts + list(reversed(sorted(hearts)))
    diamonds = ace_diamonds + king_diamonds + queen_diamonds + jack_diamonds + list(reversed(sorted(diamonds)))
    spades = ace_spades + king_spades + queen_spades + jack_spades + list(reversed(sorted(spades)))
    dictionary = {'clubs': clubs, 'hearts': hearts, 'diamonds': diamonds, 'spades': spades}
    return dictionary


def card_sort(cards):
    """
    This function sorts the cards in descending order.
    """
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


def get_cards(card_name):
    """
    This function returns suitable name of player's cards. Like, it takes '1S/0' and returns '1S'.
    """
    return card_name[0:2]


def logic(played, cards, history):
    # This is the main logic of the game.
    play = ''
    same = 0
    spades = []
    clubs = []
    remains = []
    diamonds = []
    sign_match = []
    hearts = []
    remaining_sorted = []
    sign_of_the_card = ''
    total_cards = cards_assigner(cards)
    spades = total_cards['spades']
    clubs = total_cards['clubs']
    diamonds = total_cards['diamonds']
    sign_remains = []
    hearts = total_cards['hearts']
    playable = []
    applicable_remains = []
    overall_history = []
    cards_arranged = card_sort(cards)
    total_played = []
    for dash in history:
        overall_history += dash[1]
    history_sorted = card_sort(overall_history)
    # When no players have played before you, i.e. your turn is in the first throw of any round.
    if played == []:
        # When it's the first round
        if history == []:
            if '1S' in cards and 'KS' in cards and 'QS' in cards:
                play = '1S'
            else:
                play = card_sort(cards)[0]
        # When it's not the first round
        elif history != []:
            """
            In this case tho, we need to have a list of the cards that have been played throughout the game.
            """
            pass
    # When other players have played before you
    elif played != []:
        # When it's the first round
        if history == []:
            """
            In this case tho, we need to have a list of the cards that have been played throughout the game.
            """
            pass
        # When it's not the first round
        elif history != []:
            played_cards = list(map(get_cards, played))  # Gets proper list of played card
            play_sorted = card_sort(played_cards)  # Sorts played cards
            total_played = card_sort(
                list(map(get_cards,
                         overall_history)) + played_cards)  # Gets overall history of cards that have been played
            sign_of_the_card = played_cards[0][1]  # Gets the sign of the card that has been played
            sign_match = get_plays(sign_of_the_card,
                                   play_sorted)  # Gets the list of played cards that have the same sign as the played card
            sign_match = card_sort(sign_match)  # Sorts the sign_match list
            remains = card_sort([z for z in Cards.cards if
                                 z not in total_played and z not in cards])  # Gets the list of cards that have not been played yet
            sign_remains = cards_assigner(
                remains)  # Gets a dictionary of the cards that have not been played yet with their respective signs
            applicable_remains = sign_remains[Cards.dict2[
                sign_of_the_card]]  # Gets the list of remaining cards that have the same sign as the played card
            print(applicable_remains)
            for c in cards:
                if c[1] == sign_of_the_card:
                    playable.append(c)  # Gets the list of cards that we have that have the same sign as the played card
            if len(playable) < 1:  # If we no longer have cards with same sign,
                if spades != []:  # And if we have spades,
                    playable = [spades[-1]]  # Spade of lowest value is played
                else:
                    playable = list(i for i in cards if
                                    Cards.value[i] <= 5)  # If we don't have spades, we play cards of value 5 or less
                    if playable == []:
                        playable = list(
                            cards_arranged[
                                -1])  # If we don't have cards of value 5 or less, we play the lowest card that we have
                same = 1
            if same == 0:
                playable = card_sort(playable)  # If we have cards with same sign, we sort them
                for i in playable:
                    if Cards.value[playable[0]] > Cards.value[sign_remains[Cards.dict2[sign_of_the_card]][0]] and len(
                            sign_remains[Cards.dict2[
                                sign_of_the_card]]) > 7:  # If we have highest valued card of any sign, and less than 7 of such signed card is played, we play the highest card we have
                        play = playable[0]
                    elif Cards.value[i] > Cards.value[sign_match[0]]:
                        # And play the card with exactly higher value than already played card with highest value
                        play = i
            else:
                play = playable[
                    -1]  # If we do not have cards with same sign, we play the lowest spade card or lowest other card
            if play == '':
                # If we don't have higher cards with same sign, we play the last card of the list, i.e. the lowest value card of same sign
                play = sign_match[-1]
