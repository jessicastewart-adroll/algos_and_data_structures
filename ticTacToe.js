var readline = require('readline');

function computeWinner(board, player) {
  for (var i = 0; i < board[0].length; i++) {
    var rows = search(board, player, i, 0);
    var columns = search(board, player, 0, i);
    var values = [];
    for (var direction in rows) {
      if (rows[direction] == board.length || columns[direction] == board.length) {
        return true;
      }
    }
  }
  return false;
}

function search(board, player, row, column, counts) {
  if (!counts) {
    var counts = {
      horizontal: 0,
      vertical: 0,
      forward: 0,
      backward: 0
    };
  }
  if (row < 0 || column < 0 || row >= board.length || column >= board.length) {
    return counts;
  }

  if (board[row][column] != player) {
    return counts;
  }

  counts.horizontal = 1 + search(board, player, row+1, column, counts).horizontal;
  counts.vertical = 1 + search(board, player, row, column+1).vertical;
  counts.forward = 1 + search(board, player, row+1, column+1).forward;
  counts.backward = 1 + search(board, player, row-1, column+1).backward;
  return counts;
}

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
      board[x][y] = players[currentPlayer].pop();
      if (currentPlayer == 'playerOne') {
        if (computeWinner(board, 'x')) {
          console.log('X wins!');
          printBoard(board);
          rl.close();
        }  else {
        currentPlayer = Object.keys(players)[1] 
        }
      }
      else {
        if (computeWinner(board, 'o')) {
          console.log('O wins!');
          printBoard(board);
          rl.close();
        } else {
        currentPlayer = Object.keys(players)[0] 
        }
      }
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
