# Raspberry Pi Stacker LED Game
Simple LED game for the Raspberry Pi.


## About
The game is similar to arcade game; Stacker, but with some changes here and there.


## The Game

The game includes just a few simple items to function:

- A button to press when the middle LED is lit. (More on that later)

- 3 LEDs to the side of the game which keep track of the number of lives still left by the user. 

- 5 LEDs for the actual game (however, more can be added if desired). 


The 5 Game LEDs flash one at a time, starting from left-to-right, until it has flashed all the way to right-most LED. Once it has reached the right-most LED, the LEDs starting flashing, again, one by one all the way to the left. This is repeated indefinately, or until the user presses the button. The rate at which the LEDs change increases as the user accumelates more points.


##### When to Press the Button

The button has to be pressed by the player when the middle LED is lit. If the player manages to do this, then they get a point and the rate at which the LEDs change from one to the next increases. 

If the player presses the button when the middle LED is not lit, then they lose a life. If the player still has lives, then they get to try again at the same level they were last at. If they run out of lives, then the game ends and the player can press the same button used for the game to start over.


Simple!








