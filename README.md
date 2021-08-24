# Raspberry Pi Stacker LED Game
Simple LED game for the Raspberry Pi.


## About
The game is similar to the arcade game Stacker, but with some changes. 

There's no visual stacking, the stacking is more so done with points. 

There are also lives in the game instead of either missing the stack completely, landing the block partly or landing it right in the middle. 


## The Game

### Items

The game includes just a few simple items to function:

- A button to press when the middle LED is lit. (More on that later)

- 3 LEDs to the side of the game which keep track of the number of lives left. (We'll call these the Lives LEDs)

- 5 LEDs for the actual game (however, more can be added if desired, but there has to be an *odd* amount!). (We'll call these the Game LEDs)

### Functionality

#### Flashing LEDs

The Game LEDs flash one at a time, starting from left-to-right, until it has flashed all the way to right-most LED. Once it has reached the right-most LED, the LEDs start flashing again one by one all the way to the left. This is repeated indefinitely, or until the user presses the button. The rate at which the LEDs change increases as the user accumulates more points.

#### When to Press the Button

The button has to be pressed by the player when the middle LED is lit (in this case, when LED #3 out 5 is lit). If the player manages to do this, then they get a point and the rate at which the LEDs switch from one to the next increases. If the player presses the button when the middle LED is not lit, then they lose a life.

#### Lives

The player will start with 3 lives, hence the 3 Lives LEDs. These decrease as the player loses lives, and if the player has 0 lives left, then the game is over. If the player presses the button at the wrong time and still has 1 or more lives left, then they get to try again at the same level they were last at.

#### Starting Over

The player can press the same button used for the game to start over. This will reset their lives counter, their score, as well as the rate of change of the game LEDs.



That's it!




