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

function printBoard(board) {
  for (var i = 0; i < board.length; i++) {
    console.log(board[i]);
  }
}

rl.setPrompt(currentPlayer + ' ');
printBoard(board);
rl.prompt();
rl.on('line', function(line) {
    var x = line.split(' ')[0].toString();
    var y = line.split(' ')[1].toString();

    if (!board[x][y] ) {
      board[x][y] = players[currentPlayer].pop()
      currentPlayer = currentPlayer == 'playerOne' ? Object.keys(players)[1] : Object.keys(players)[0] 
    }
    
    rl.setPrompt(currentPlayer + ' ');

    if (!players.playerOne.length && !players.playerTwo.length) {
      printBoard(board);
      rl.close();
    } else {
      printBoard(board);
      rl.prompt();
    }
}).on('close',function(){
    process.exit(0);
});
