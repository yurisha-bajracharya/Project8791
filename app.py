# This contains the basic code that you will need to view the game on the snadbox.
# You will provide all the moves of all the bots in the sandbox.
# The sandbox is for testing purposes only so, the API data format can change
# when quelifiers begin.
# The sandbox is provided so that you can get familiar with buliding bots before
#  the event actually begings.

# To seutp: `pip install flask, flask_cors`
# To run: python app.py

import json
import Cards
from Logic import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/bid", methods=["POST"])
def bid():
    """
    Bid is called at the starting phase of the game in callbreak.
    You will be provided with the following data:
    {
        "matchId": "M1",
        "playerId": "P3",
        "cards": ["1S", "TS", "8S", "7S", "6S", "4S", "3S", "9H", "6H", "5H", "1C", "1D", "JD"],
        "context": {
            "round": 1,
            "players": {
            "P3": {
                "totalPoints": 0,
                "bid": 0
            },
            "P0": {
                "totalPoints": 0,
                "bid": 3
            },
            "P2": {
                "totalPoints": 0,
                "bid": 3
            },
            "P1": {
                "totalPoints": 0,
                "bid": 3
            }
            }
        }
    }

    This is all the data that you will require for the bidding phase.
    """

    body = request.get_json()
    # print(json.dumps(body, indent=2))

    ####################################
    bid = 0
    count_spades = 0
    count_clubs = 0
    count_diamonds = 0
    count_hearts = 0
    player = ""
    cards = body["cards"]
    player = body["playerId"]
    for i in cards:
        if i in Cards.winners:
            bid += 1
        if 'S' in cards:
            count_spades += 1
        if 'H' in cards:
            count_hearts += 1
        if 'C' in cards:
            count_clubs += 1
        if 'D' in cards:
            count_diamonds += 1
    ####################################
    if count_clubs >= 3:
        bid -= 1
    if count_hearts >= 3:
        bid -= 1
    if count_diamonds >= 3:
        bid -= 1
    if count_diamonds <= 2 or count_clubs <= 2 or count_hearts <= 2:
        if count_spades >= 5:
            bid += 1
    if bid <= 0:
        bid = 1
    print(player + ': ' + str(bid))
    # return should have a single field value which should be an int reprsenting the bid value
    return jsonify({"value": 3})


@app.route("/play", methods=["POST"])
def play():
    """
    Play is called at every hand of the game where the user should throw a card.
    Request data format:
    {
        "matchId": "M1",
        "playerId": "P1",
        "cards": [ "QS", "9S", "2S", "KH", "JH", "4H", "JC", "9C", "7C", "6C", "8D", "6D", "3D"],
        "played": [
            "2H/0",
            "8H/0"
        ],
        "history": [
            [1, ["TS/0", "KS/0", "1S/0", "5S/0"], 3],
            [3, ["QS/0", "6S/0", "TH/0", "2S/0"], 3],
        ],
        "players": ["P0", "P1", "P2", "P3"]
    }
    The `played` field contins all the cards played this turn in order.
    'history` field contains an ordered list of cards played from first hand.
    Format: `start idx, [cards in clockwise order of player ids], winner idx`
        `start idx` is index of player that threw card first
        `winner idx` is index of player who won this hand
    `players`: list of ids in clockwise order (always same for a game)
    """
    body = request.get_json()
    # print(json.dumps(body, indent=2))

    ####################################
    cards = body['cards']  # list of cards in hand
    played = body['played']  # list of cards played this turn
    history = body['history']  # list of cards played from first hand
    players = body['playerId']  # list of player ids in clockwise order
    """
    print('CARDS: ' + str(cards))
    print('HISTORY: ' + str(history))
    print('PLAYED: ' + str(played))
    ####################################
    """
    logic(played, cards, history)
    # return should have a single field value
    # which should be an int reprsenting the index of the card to play
    # e.g> {"value": body.cards.index("QS")}
    # to play the card "QS"
    return jsonify({"value": 0})


# do not change this port; the sandbox server hits this port on localhost
app.run(port=7000)
