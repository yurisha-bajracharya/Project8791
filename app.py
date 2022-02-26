# This contains the basic code that you will need to view the game on the sandbox.
# You will provide all the moves of all the bots in the sandbox.
# The sandbox is for testing purposes only so, the API data format can change
# when qualifiers begin.
# The sandbox is provided so that you can get familiar with building bots before
#  the event actually begins.

# To setup: `pip install flask, flask_cors`
# To run: python app.py

import json
import Cards

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bid = 1
played_cards = []


@app.route("/bid", methods=["OPTIONS", "POST"])
def bid():
    """
    Bid is called at the starting phase of the game in call break.
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
    try:
        cards = body["cards"]
        for i in cards:
            if i in Cards.winners:
                bid += 1
            if 'S' in cards:
                count_spades += 1
            elif 'H' in cards:
                count_hearts += 1
            elif 'C' in cards:
                count_clubs += 1
            elif 'D' in cards:
                count_diamonds += 1
    except:
        pass
    #     Input your code here.        #
    ####################################
    if count_clubs >= 4:
        bid -= 1
    if count_hearts >= 4:
        bid -= 1
    if count_diamonds >= 4:
        bid -= 1
    if count_diamonds <= 2 or count_clubs <= 2 or count_hearts <= 2:
        if count_spades >= 5:
            bid += 1

    # return should have a single field value which should be an int representing the bid value
    return jsonify({"value": bid})


@app.route("/play", methods=["OPTIONS", "POST"])
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
        ]
    }
    The played field contains all the cards played this turn in order.
    """
    body = request.get_json()
    try:
        played_cards.append(body["played"][-1][0:2])
    except:
        pass
    # print(json.dumps(body))
    ####################################
    #     Input your code here.        #
    ####################################

    # return should have a single field value
    # which should be an int representing the index of the card to play
    # e.g> {"value": body.cards.index("QS")}
    # to play the card "QS"
    return jsonify({"value": 0})


# do not change this port; the sandbox server hits this port on localhost
app.run(port=7000)
print(played_cards)