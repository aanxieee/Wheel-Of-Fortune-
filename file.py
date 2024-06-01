import random 
# 'RANDOM' MODULE is used to introduce an element of chance, mimicking the randomness of spinning the wheel and selecting a phrase
class WheelOfFortune:
    def __init__(self):  #     Class Initialization - Initializes the game with a list of phrases and wheel values; Randomly selects a phrase and sets up the initial game state.
        self.phrases = [
            "HELLO WORLD", 
            "PYTHON PROGRAMMING", 
            "WHEEL OF FORTUNE", 
            "I LIKE GAMING",
            "CODE BY AANYA"
        ]
        self.wheel_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, "BANKRUPT", "LOSE A TURN"]
        self.current_phrase = random.choice(self.phrases)
        self.guessed_letters = set()
        self.correct_letters = set(char for char in self.current_phrase if char.isalpha())
        self.player_score = 0
        self.turns = 0

    def spin_wheel(self): #Spin the Wheel : Randomly selects a value from the wheel values.

        return random.choice(self.wheel_values)

    def guess_letter(self, letter): #Guess Letter (guess_letter method):Checks if the guessed letter is in the phrase and updates the set of guessed letters.

        if letter in self.current_phrase and letter not in self.guessed_letters:
            self.guessed_letters.add(letter)
            return True
        else:
            self.guessed_letters.add(letter)
            return False

    def display_phrase(self): #Display Phrase (display_phrase method):Constructs and returns the current state of the phrase with guessed letters revealed and unknown letters as underscores.
       
        displayed_phrase = ""
        for char in self.current_phrase:
            if char in self.guessed_letters:
                displayed_phrase += char
            elif char == " ":
                displayed_phrase += " "
            else:
                displayed_phrase += "_"
        return displayed_phrase

    def play_game(self): #Play Game (play_game method):Manages the game loop, allowing the player to spin the wheel, guess letters, or guess the phrase ; Handles scoring, turns, and game end conditions.

        print("Welcome to Wheel of Fortune!")
        while self.correct_letters != self.guessed_letters:
            print(f"Phrase: {self.display_phrase()}")
            print(f"Guessed letters: {' '.join(self.guessed_letters)}")
            print(f"Score: {self.player_score}")
            print(f"Turns: {self.turns}")

            action = input("Would you like to (s)pin the wheel or (g)uess the phrase? ").lower()
            if action == 's':
                self.turns += 1
                wheel_result = self.spin_wheel()
                print(f"The wheel landed on: {wheel_result}")
                if wheel_result == "BANKRUPT":
                    self.player_score = 0
                    print("You went bankrupt! Your score is reset to 0.")
                elif wheel_result == "LOSE A TURN":
                    print("You lost a turn!")
                else:
                    letter = input("Guess a letter: ").upper()
                    if self.guess_letter(letter):
                        print(f"Correct! The letter {letter} is in the phrase.")
                        self.player_score += wheel_result
                    else:
                        print(f"Sorry, the letter {letter} is not in the phrase.")
            elif action == 'g':
                guess = input("Guess the phrase: ").upper()
                if guess == self.current_phrase:
                    print(f"Congratulations! You guessed the phrase: {self.current_phrase}")
                    self.player_score += 1000  # Bonus for guessing the entire phrase
                    break
                else:
                    print("Sorry, that's not the correct phrase.")

        print(f"Game over! Your final score is: {self.player_score}")
        print(f"The phrase was: {self.current_phrase}")

if __name__ == "__main__": # # This block runs the game if the script is executed directly, but not if it's imported as a module.
    game = WheelOfFortune()
    game.play_game()
