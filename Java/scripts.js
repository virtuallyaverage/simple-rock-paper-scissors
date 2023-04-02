
function selection(userSelection) {
	//get the computers guess
	var computerGuess = Math.floor(Math.random() * 3);
	var computerGuessName = 'empty';

	//get the text value for each
	if (computerGuess == 0) {
		computerGuessName = 'rock';
	} else if (computerGuess == 1) {
		computerGuessName = 'paper';
	} else if (computerGuess == 2) {
		computerGuessName = 'scissors';
	}

	//initialize the variable
	var winner = 'undecided';


	// if user chooses rock
	if (userSelection == 'rock') {
		if (computerGuess == 0) {
			winner = 'tie';
		} else if (computerGuess == 2) {
			winner = 'user';
		} else if (computerGuess == 1) {
			winner = 'computer';
		}
	}

	// if user chooses rock
	if (userSelection == 'paper') {
		if (computerGuess == 1) {
			winner = 'tie';
		} else if (computerGuess == 0) {
			winner = 'user';
		} else if (computerGuess == 2) {
			winner = 'computer';
		}
	}

	// if user chooses rock
	if (userSelection == 'scissors') {
		if (computerGuess == 2) {
			winner = 'tie';
		} else if (computerGuess == 1) {
			winner = 'user';
		} else if (computerGuess == 0) {
			winner = 'computer';
		}
	}

	//update the values
	var PreviousGuessPage = document.getElementById("computerGuess");
	PreviousGuessPage.textContent = computerGuessName;
	var whoWon = document.getElementById("winner_text");
	whoWon.textContent = winner;

	//get what recorded values are currently
	var winBox = document.getElementById("wins");
	var winCount = parseInt(winBox.textContent);
	var tieBox = document.getElementById("ties");
	var tieCount = parseInt(tieBox.textContent);
	var lossBox = document.getElementById("loss");
	var lossCount = parseInt(lossBox.textContent)

	//increment values
	if (winner == 'tie') {
		tieCount = tieCount + 1;
	} else if (winner == 'user') {
		winCount = winCount + 1;
	} else if (winner == 'computer') {
		lossCount = lossCount + 1;
	}

	//reupload the values
	winBox.textContent = winCount;
	tieBox.textContent = tieCount;
	lossBox.textContent = lossCount;
}



