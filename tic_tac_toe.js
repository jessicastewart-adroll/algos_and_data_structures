var readline = require('readline');

var players = {
  playerOne: ['x', 'x', 'x', 'x', 'x'],
  playerTwo: ['o', 'o', 'o', 'o']
};
var board = [ [null, null, null],
              [null, null, null],
              [null, null, null],
            ];

//var rl = readline.createInterface(process.stdin, process.stdout);
var currentPlayer = Object.keys(players)[0];

function printBoard(board) {
  for (var i = 0; i < board.length; i++) {
    console.log(board[i]);
  }
}

function compute_winner(board) {
  // horizontals
  for (var row = 0; row < board.length; row++) {
    var win = 0
    for (var column = 0; column < board[0].length; column++) {
      if (board[row][column] === 'x') {
        win += 1;
      }
    }
    console.log(row, column, win)
    if (win == board.length-1) {
      return true;
    }
  }

  // verticals
  for (var row = 0; row < board.length; row++) {
    var win = 0;
    for (var column = 0; column < board[0].length; column++) {
      if (board[column][row] == 'x') {
        win += 1;
      }
    }
    if (win == board.length-1) {
      return true;
    }
  }

  // forward diagonal
  var win = 0;
  for (var row = 0; row < board.length; row++) {
    if (board[row][row] == 'x') {
        win += 1;
    }
  }
  if (win == board.length-1) {
    return true;
  }

  // reverse diagonal
  var win = 0;
  for (var row = 0; row < board.length; row++) {
    var column = (board.length-1) - row;
    if (board[row][column] == 'x') {
      win += 1;
    }
  }
  if (win == board.length-1) {
    return true;
  }

  return false;
}

var test_horizontal = [ 
                   [00, 01, 02],
                   ['x', 'x', 'x'],
                   [20, 21, 22],
                ];

var test_veritcal = [ 
                   [00, 'x', 02],
                   [10, 'x', 12],
                   [20, 'x', 22],
                ];

var test_forward_diagonal = [ 
                   ['x', 01, 02],
                   [10, 'x', 12],
                   [20, 21, 'x'],
                ];

var test_backward_diagonal = [ 
                   [00, 01, 'x'],
                   [10, 'x', 12],
                   ['x', 21, 22],
                ];

console.log(compute_winner(test_horizontal));  
// console.log(compute_winner(test_veritcal));  
// console.log(compute_winner(test_forward_diagonal));  
// console.log(compute_winner(test_backward_diagonal));           

// rl.setPrompt(currentPlayer + ' ');
// printBoard(board);
// rl.prompt();
// rl.on('line', function(line) {
//     var x = line.split(' ')[0].toString();
//     var y = line.split(' ')[1].toString();

//     if (!board[x][y] ) {
//       board[x][y] = players[currentPlayer].pop()
//       currentPlayer = currentPlayer == 'playerOne' ? Object.keys(players)[1] : Object.keys(players)[0] 
//     }
    
//     rl.setPrompt(currentPlayer + ' ');

//     if (!players.playerOne.length && !players.playerTwo.length) {
//       printBoard(board);
//       rl.close();
//     } else {
//       printBoard(board);
//       rl.prompt();
//     }
// }).on('close',function(){
//     process.exit(0);
// });
/////////////////////////////////////////
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
