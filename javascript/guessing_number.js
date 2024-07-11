const math = require("mathjs"); // Importing math module
const prompt = require("prompt-sync")(); // Accessing prompt method in program file
let random_number = math.floor(math.random() * 100); // This is used to generate number between 1-100
let user_number; // This variable is used to store the user entered number
let guess = 0; // Initializing total number of guesses
// Using do-while loop
do {
  user_number = Number.parseInt(prompt(`Enter number: `)); // Prompting the user to enter a number
  guess += 1; // Incrementing the guesses
  // Checks the number of guesses
  // If the guess == 5, all the guesses are used and game will terminates
  if (guess == 5) {
    console.log(
      `You Lost\nAll lifes are finished\nCorrect Number is: ${random_number}`,
    );
    break;
  }
  // If guess != 5 then program will continues and askes for furthur input
  else {
    console.log(`Total Life left: ${5 - guess}`); // total number of guess alloted 5
    if (random_number == user_number) {
      // this conditional statement is used to praise the user that the entered number is correct
      console.log("You win!");
    } else {
      // if the entered number is not correct then in that case it will continue the iteration
      if (user_number > random_number) {
        // tells the user that entered number is higher then the actual number
        console.log("Guess lower number!");
        continue;
      } else {
        console.log("Guess higher number!"); // tells the user that entered number is lower then the actual number
        continue;
      }
    }
  }

  // Checks the user input
} while (user_number != random_number);
