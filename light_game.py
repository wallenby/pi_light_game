from gpiozero import Button, LED
from signal import pause
from numpy import array
import os
import time
import threading
import math

# - The LEDs on the GPIO and other values -
# gLED are the game LEDs (Red, yellow and green)
gLED = array([LED(24), LED(23), LED(22), LED(27), LED(17)])
# blueLED are the blue LEDs which represent the lives left
blueLED = array([LED(16), LED(20), LED(21)])
startTime = time.time()
running = False
gLEDchangeRate = 0.5
goalgLEDindex = 2
livesLeft = 3
score = 0
gameOver = False

# Where the blinking and switching of gLEDs happens
def timerThread():

    global gLED, startTime, running, currentgLED

    running = True

    startTime = time.time()

    # While the game is running
    while (running):
        
        # Moving left to right |----->
        for x in range(len(gLED)):
            
            # The time the LED was turned on
            tempTime = time.time()
         
            # While the button hasn't been pressed
            while (running):

                # Changing LED that is alluminated after the LED 
                # was turned on for the value of time of gLEDchangeRate
                if( (time.time() - tempTime) >= gLEDchangeRate):

                    if (x == 0):
                        gLED[x].on()
                        gLED[x+1].off()
                    else:
                        gLED[x-1].off()
                        gLED[x].on()
                        
                    break
                
        # Moving right to left <-----|
        for x in range(len(gLED) - 2, 0, -1):

            # The time the LED was turned on
            tempTime = time.time()

            # While the button hasn't been pressed
            while (running):

                # Changing LED that is alluminated after the LED 
                # was turned on for the value of time of gLEDchangeRate
                if((time.time() - tempTime) >= gLEDchangeRate):

                    gLED[x+1].off()
                    gLED[x].on()

                    break


# Pressing the button
def buttonPress():

    global gLED, running, currentgLED, score, thread, gLEDchangeRate, livesLeft, gameOver

    # If the game is running
    if (running):

        # Stopping the thread
        running = False

        # If the user scored
        if (gLED[goalgLEDindex].value == 1):

            print("HIT!")
            score = score + 1
            print("Score:", score, "\n")

            # Blinking the gLEDs 3 times
            for i in range(3):

                timeNow = time.time()
                while (True):
                    if((time.time() - timeNow) >= 0.20):
                        for x in range(len(gLED)):
                            gLED[x].on()
                        break

                timeNow = time.time()

                while (True):
                    if((time.time() - timeNow) >= 0.20):
                        for x in range(len(gLED)):
                            gLED[x].off()
                        break

                gLEDchangeRate = gLEDchangeRate * 0.9

        else:
            print("Miss :(")

            # Blinking the blue LEDs 3 times
            for i in range(3):

                timeNow = time.time()
                while (True):
                    if((time.time() - timeNow) >= 0.20):
                        for x in range(len(blueLED)):
                            blueLED[x].on()
                        break

                timeNow = time.time()

                while (True):
                    if((time.time() - timeNow) >= 0.20):
                        for x in range(len(blueLED)):
                            blueLED[x].off()
                        break

            livesLeft = livesLeft - 1
            print("Lives:", livesLeft, "\n")

                      # Blue LEDs score count
            if(livesLeft == 2):
                blueLED[0].off()
                blueLED[1].on()
                blueLED[2].on()

            elif (livesLeft == 1):
                blueLED[0].off()
                blueLED[1].off()
                blueLED[2].on()

            elif (livesLeft == 0):
                blueLED[0].off()
                blueLED[1].off()
                blueLED[2].off()
                print("\n~~~ GAME OVER ~~~")
                print("Final Sore:", score,  "\n")
                gameOver = True

            for x in range(len(gLED)):
                gLED[x].off()

                for x in range(len(gLED)):
                    gLED[x].off()

        if not (gameOver):
            # Running game thread again
            thread = threading.Thread(target=timerThread)
            thread.start()


    # If the game hasn't started yet, start it and reset values and lights
    else:
        print("\n~~~ GAME HAS STARTED ~~~")
        print("Lives:", livesLeft)
        print("Score:", score, "\n")
        thread = threading.Thread(target=timerThread)
        thread.start()
        livesLeft = 3
        score = 0
        gameOver = False
        gLEDchangeRate = 0.5
        for x in range(len(blueLED)):
            blueLED[x].on()


button = Button(2)  # 2 = button

button.when_pressed = buttonPress

pause()

print("End of Program.")