var readline = require('readline');

var playerOne = ['x', 'x', 'x', 'x', 'x'];
var playerTwo = ['o', 'o', 'o', 'o', 'o'];
var board = [ [null, null, null],
              [null, null, null],
              [null, null, null],
            ];

var rl = readline.createInterface(process.stdin, process.stdout);
rl.setPrompt('playerOneX> ');
rl.prompt();
rl.on('line', function(line) {
    if (line === "x") {
      playerOne.pop()
      rl.setPrompt('playerTwoO> ');
    } else if (line === "o") {
      playerTwo.pop()
      rl.setPrompt('playerOneX> ');
    } 

    if (!playerOne.length && !playerTwo.length) {
      rl.close();
    } else {
      rl.prompt();
    }
}).on('close',function(){
    process.exit(0);
});
