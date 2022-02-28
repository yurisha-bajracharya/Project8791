const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url) res.setHeader('Content-Type', 'application/json');
  res.setHeader('Access-Control-Allow-Origin', '*');

  let payload = '';
  req.on('data', chunk => {
    payload += chunk;
  });

  req.on('end', () => {
    let result = { error: 'Unknown request' };
    if (req.url.endsWith('bid')) {
      result = bid(payload);
    } else if (req.url.endsWith('play')) {
      result = play(payload);
    }

    res.write(JSON.stringify(result));
    res.end();
  });
});

function bid(payload) {
  /*
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
  */
  console.log('Returning bid', payload);

  /*
  ####################################
  #     Input your code here.        #
  ####################################
  */

  // return should have a single field value which should be an int reprsenting the bid value
  return {
    value: Math.floor(Math.random() * 4) + 2,
  };
}

function play(payload) {
  /*
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
        [3, ["QS/0", "6S/0", "TH/0", "2S/0"], 3],
        [1, ["TS/0", "KS/0", "1S/0", "5S/0"], 3],
      ],
      "players": ["P0", "P1", "P2", "P3"]
    }
  The `played` field contins all the cards played this turn in order.
    'history` field contains an ordered list of cards played from first hand.
    Format: `start idx, [cards in clockwise order of player ids], winner idx`
        `start idx` is index of player that threw card first
        `winner idx` is index of player who won this hand
    `players`: list of ids in clockwise order (always same for a game)
  */
  console.log('Returning play', payload);

  /*
  ####################################
  #     Input your code here.        #
  ####################################
  */

  //  return should have a single field value
  //  which should be an int reprsenting the index of the card to play
  //  e.g> {"value": payload.cards.indexOf("QS")}
  //  to play the card "QS"
  return {
    value: 0,
  };
}

server.listen(7000);
