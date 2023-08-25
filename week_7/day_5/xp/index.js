// Define winning combinations
const winCombos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2]
  ];
  
  // Initialize game variables
  let playerSymbol = "";
  let computerSymbol = "";
  let currentPlayer = "";
  let currentDifficulty = "";
  let gameBoard = ["", "", "", "", "", "", "", "", ""];
  
  // Get DOM elements
  const boxes = document.querySelectorAll('.box');
  const chooseXButton = document.getElementById('chooseX');
  const chooseOButton = document.getElementById('chooseO');
  const restartButton = document.getElementById('restart');
  
  // Event listeners for buttons
  chooseXButton.addEventListener('click', () => {
    playerSymbol = "X";
    computerSymbol = "O";
    currentPlayer = playerSymbol;
    currentDifficulty = "hard"; // or "hard" for hard level
    enableBoxes();
    computerMove();
  });
  
  chooseOButton.addEventListener('click', () => {
    playerSymbol = "O";
    computerSymbol = "X";
    currentPlayer = playerSymbol;
    currentDifficulty = "hard"; // or "hard" for hard level
    enableBoxes();
    computerMove();
  });
  
  restartButton.addEventListener('click', restartGame);
  
  // Event listeners for boxes
  boxes.forEach(box => {
    box.addEventListener('click', () => makeMove(box.id));
  });
  
  // Enable player's move
  function enableBoxes() {
    boxes.forEach(box => {
      box.style.pointerEvents = "auto";
    });
    chooseXButton.disabled = true;
    chooseOButton.disabled = true;
  }
  
  // Disable player's move during computer's turn
  function disableBoxes() {
    boxes.forEach(box => {
      box.style.pointerEvents = "none";
    });
  }
  
  // Handle player's move
  // Handle player's move
  function makeMove(boxId) {
    if (gameBoard[boxId] === "" && currentPlayer === playerSymbol) {
      gameBoard[boxId] = playerSymbol;
      document.getElementById(boxId).textContent = playerSymbol;
      currentPlayer = computerSymbol;
      disableBoxes();
      checkGameStatus();
  
      // Check if the game hasn't been won yet
      if (checkWinner() === null) {
        computerMove();
      }
    }
  }
  
    
    function computerMove() {
      if (currentPlayer === computerSymbol) {
        if (currentDifficulty === "easy") {
          computerMoveEasy();
        } else if (currentDifficulty === "hard") {
          computerMoveHard();
        }
      }
    }
    
    function computerMoveEasy() {
      const emptyBoxes = gameBoard.reduce((acc, val, index) => {
        if (val === "") {
          acc.push(index);
        }
        return acc;
      }, []);
    
      const randomIndex = Math.floor(Math.random() * emptyBoxes.length);
      const selectedBox = emptyBoxes[randomIndex];
    
      gameBoard[selectedBox] = computerSymbol;
      document.getElementById(selectedBox.toString()).textContent = computerSymbol;
    
      currentPlayer = playerSymbol;
      enableBoxes();
      checkGameStatus();
    }
    
    function computerMoveHard() {
      let bestScore = -Infinity;
      let bestMove;
    
      for (let i = 0; i < 9; i++) {
        if (gameBoard[i] === "") {
          gameBoard[i] = computerSymbol;
          let score = minimax(gameBoard, 0, false);
          gameBoard[i] = "";
          if (score > bestScore) {
            bestScore = score;
            bestMove = i;
          }
        }
      }
    
      gameBoard[bestMove] = computerSymbol;
      document.getElementById(bestMove.toString()).textContent = computerSymbol;
    
      currentPlayer = playerSymbol;
      enableBoxes();
      checkGameStatus();
    }
    
    function minimax(board, depth, isMaximizing) {
      const scores = {
        X: -1,
        O: 1,
        tie: 0
      };
    
      const winner = checkWinner();
      if (winner !== null) {
        return scores[winner];
      }
    
      if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < 9; i++) {
          if (board[i] === "") {
            board[i] = computerSymbol;
            let score = minimax(board, depth + 1, false);
            board[i] = "";
            bestScore = Math.max(score, bestScore);
          }
        }
        return bestScore;
      } else {
        let bestScore = Infinity;
        for (let i = 0; i < 9; i++) {
          if (board[i] === "") {
            board[i] = playerSymbol;
            let score = minimax(board, depth + 1, true);
            board[i] = "";
            bestScore = Math.min(score, bestScore);
          }
        }
        return bestScore;
      }
    }
    
    function checkGameStatus() {
      const winner = checkWinner();
    
      if (winner === playerSymbol) {
        displayResult("Player wins!");
      } else if (winner === computerSymbol) {
        displayResult("Computer wins!");
      } else if (gameBoard.every(box => box !== "") && winner === null) {
        displayResult("Tie game");
      }
    }
    
    
    function checkWinner() {
      for (const combo of winCombos) {
        const [a, b, c] = combo;
        if (gameBoard[a] !== "" && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
          return gameBoard[a];
        }
      }
      return null;
    }
    
    function displayResult(result) {
      document.getElementById('restart').style.display = "block";
      disableBoxes();
      alert(result);
    }
    
    function restartGame() {
      gameBoard = ["", "", "", "", "", "", "", "", ""];
      boxes.forEach(box => {
        box.textContent = "";
      });
      currentPlayer = playerSymbol;
      currentDifficulty = "";
      chooseXButton.disabled = false;
      chooseOButton.disabled = false;
      restartButton.style.display = "none";
    }
    