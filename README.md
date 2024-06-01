# Wheel-Of-Fortune-
A game coded in python , guess a phrase or spin the wheel 
The Wheel of Fortune game implemented in the provided Python code is a simplified text-based version of the popular TV game show "Wheel of Fortune."
The main objective is to guess the hidden phrase by suggesting letters one at a time or by guessing the entire phrase .
gameplay elements: phrase - a secret phrase that the player needs to guess ; wheel - letter or to encounter special events like 'BANKRUPT' or 'LOST A TURN'
; score- the players score accumulates based on the value of correctly guessed letters ; guessed letters - a record of letters the player has already guessed . 
#example gameplay 
1. The game selects the phrase "HELLO WORLD".
2. The player starts with a score of 0.
3. The player chooses to spin the wheel and lands on 200.
4. The player guesses the letter 'L'.
   - The letter 'L' is in the phrase, so the player earns 200 points for each 'L' (total 400 points).
   - The phrase now shows: "_ _ L L _ _ _ _ L _".
5. The player chooses to spin the wheel again and lands on "LOSE A TURN".
   - The player loses their turn.
6. The player spins the wheel again and lands on 300.
7. The player guesses the letter 'H'.
   - The letter 'H' is in the phrase, so the player earns 300 points.
   - The phrase now shows: "H _ L L _ _ _ _ L _".
8. The player chooses to guess the phrase and guesses "HELLO WORLD".
   - The guess is correct. The player earns a bonus of 1000 points and wins the game.
