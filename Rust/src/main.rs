fn simple_game() {
    //include the random number generator
    use rand::prelude::*;
    let mut rng = rand::thread_rng();

    //get the users first guess
    let mut user_guess = read_terminal("\nwhat is your guess? (r, p, s, no): ");

    //mesages for when a user:
    let user_wins = "Only onece, you ded next round";
    let user_lose = "hehe, I win, you die, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom, your mom";
    let tie = "we tied......I have no words. AGAIN!";

    //main game loop
    while user_guess != "no" {
        //the computers guess
        let computer_guess:i32 = rng.gen_range(0..=2);

        //if the user guesses rock
        if user_guess == "r" {
            if  computer_guess == 0 {
                println!("{}",tie)
            } else if computer_guess == 2 {
                println!("{}",user_wins)
            } else if computer_guess == 1 {
                println!("{}",user_lose)
            }
        }

        //if the user guesses paper
        else if user_guess == "p" {
            if  computer_guess == 1 {
                println!("{}",tie)
            } else if computer_guess == 0 {
                println!("{}",user_wins)
            } else if computer_guess == 2 {
                println!("{}",user_lose)
            }
        }

        //if the user guesses scissors
        else if user_guess == "s" {
            if  computer_guess == 2 {
                println!("{}",tie)
            } else if computer_guess == 1 {
                println!("{}",user_wins)
            } else if computer_guess == 0 {
                println!("{}",user_lose)
            }
        }

        //if not one of the options       
        else {
            println!("not an answer, retry\n")
        };

        //get the users guess
        user_guess = read_terminal("\nwhat is your guess? (r, p, s, no): ");
    }
}

fn read_terminal(prompt: &str) -> String {
    //import the module
    use text_io::read;

    //print the prompt
    print!("{}", prompt);

    //read from the thing
    let output: String = read!("{}");

    //return the value
    return output

}

fn main() {
    simple_game();
}
