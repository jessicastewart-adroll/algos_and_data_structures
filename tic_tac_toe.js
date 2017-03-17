///////////////// dfs ////////////////////////
// misses backwards diagonal
function compute_winner(board, player) {
  for (var row = 0; row < board.length; row++) {
    for (var column = 0; column < board[0].length; column++) {
      var value = search(board, player, row, column)
      if (value == board.length) {
        return true;
      }
    }
  }
  return false;
}

function search(board, player, row, column) {
  if (row < 0 || column < 0 || row >= board.length || column >= board.length) {
    return 0;
  }

  if (board[row][column] != player) {
    return 0;
  }

  var count = 1
  count += search(board, player, row+1, column);
  count += search(board, player, row, column+1);
  count += search(board, player, row+1, column+1);

  return count;
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

var test_broken_one = [ 
                   [00, 01, 'x'],
                   [10, 'x', 12],
                   [20, 'x', 22],
                ];

var test_broken_two = [ 
                   [00, 01, 'x'],
                   [10, 'x', 'x'],
                   [20, 21, 22],
                ];

var test_broken_three = [ 
                   [00, 01, 'x'],
                   [10, 'x', 12],
                   [20, 21, 'x'],
                ];           

// console.log(compute_winner(test_horizontal, 'x'));  
// console.log(compute_winner(test_veritcal, 'x')); 
// console.log(compute_winner(test_forward_diagonal, 'x'));
console.log(compute_winner(test_backward_diagonal, 'x'));   
// console.log(compute_winner(test_broken_one, 'x'));
// console.log(compute_winner(test_broken_two, 'x')); 
// console.log(compute_winner(test_broken_three, 'x')); 

///////////////// prevent repetition -> n^3 ////////////////////////
function compute_winner(board, player) {
  // strights
  for (var row = 0; row < board.length; row++) {
    var horizontal = 0
    var vertical = 0
    for (var column = 0; column < board[0].length; column++) {
      if (board[row][column] == player) {
        horizontal += 1;
      }
      if (board[column][row] == player) {
        vertical += 1;
      }
    }
    if (horizontal == board.length || vertical == board.length) {
      return true;
    }
  }

  // diagonals
  var forward_diagonal = 0;
  var reverse_diagonal = 0;
  for (var row = 0; row < board.length; row++) {
    var column = (board.length-1) - row;
    if (board[row][row] == player) {
      forward_diagonal += 1;
    }
    if (board[row][column] == player) {
      reverse_diagonal += 1;
    }
  }
  if (forward_diagonal == board.length || reverse_diagonal == board.length) {
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

var test_broken_one = [ 
                   [00, 01, 'x'],
                   [10, 'x', 12],
                   [20, 'x', 22],
                ];

var test_broken_two = [ 
                   [00, 01, 'x'],
                   [10, 'x', 'x'],
                   [20, 21, 22],
                ];

var test_broken_three = [ 
                   [00, 01, 'x'],
                   [10, 'x', 12],
                   [20, 21, 'x'],
                ];           

console.log(compute_winner(test_horizontal, 'x'));  
console.log(compute_winner(test_veritcal, 'x')); 
console.log(compute_winner(test_forward_diagonal, 'x'));
console.log(compute_winner(test_backward_diagonal, 'x'));   
console.log(compute_winner(test_broken_one, 'x'));
console.log(compute_winner(test_broken_two, 'x')); 
console.log(compute_winner(test_broken_three, 'x')); 

///////////////// brute-force -> n^6 ////////////////////////
function compute_winner(board) {
  // horizontals
  for (var row = 0; row < board.length; row++) {
    var win = 0
    for (var column = 0; column < board[0].length; column++) {
      if (board[row][column] === 'x') {
        win += 1;
      }
    }
    if (win == board.length) {
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
    if (win == board.length) {
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
  if (win == board.length) {
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
  if (win == board.length) {
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

var test_broken_one = [ 
                   [00, 01, 'x'],
                   [10, 'x', 12],
                   [20, 'x', 22],
                ];

var test_broken_two = [ 
                   [00, 01, 'x'],
                   [10, 'x', 'x'],
                   [20, 21, 22],
                ];

var test_broken_three = [ 
                   [00, 01, 'x'],
                   [10, 'x', 12],
                   [20, 21, 'x'],
                ];           

console.log(compute_winner(test_horizontal));  
console.log(compute_winner(test_veritcal));  
console.log(compute_winner(test_forward_diagonal));  
console.log(compute_winner(test_backward_diagonal));   
console.log(compute_winner(test_broken_one));   
console.log(compute_winner(test_broken_two));   
console.log(compute_winner(test_broken_three)); 

///////////////// set-up ////////////////////////
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
