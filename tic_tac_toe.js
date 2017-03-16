var readline = require('readline');

var players = {
  playerOne: ['x', 'x', 'x', 'x', 'x'],
  playerTwo: ['o', 'o', 'o', 'o']
};
var board = [ [null, null, null],
              [null, null, null],
              [null, null, null],
            ];

var rl = readline.createInterface(process.stdin, process.stdout);
var currentPlayer = Object.keys(players)[0];

rl.setPrompt(currentPlayer + ' ');
console.log(board);
rl.prompt();
rl.on('line', function(line) {
    if (!line.split(' ').length == 2) {
      console.log('Bad input');
      rl.prompt();
      return
    }

    var x = line.split(' ')[0].toString();
    var y = line.split(' ')[1].toString();
    if (!x || !y || x<0 || y<0 || x>=board.length || y>=board[0].length) {
      console.log('Bad input');
      rl.prompt();
    }

    board[x][y] = players[currentPlayer].pop()

    currentPlayer = currentPlayer == 'playerOne' ? Object.keys(players)[1] : Object.keys(players)[0] 
    rl.setPrompt(currentPlayer + ' ');

    if (!players.playerOne.length && !players.playerTwo.length) {
      rl.close();
    } else {
      console.log(board);
      rl.prompt();
    }
}).on('close',function(){
    process.exit(0);
});
