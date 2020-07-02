- Make sure that the library 'numpy' is installed.
- To install numpy : "pip install numpy"
- Since storing the utility values in a file for n dimensional array is a complicated thing. Therefore I've preferred to input the n player game via the terminal.
- Once the game details are entered, it will show all the details about the game.

Input Format : 
For example, to input the following game...
  |  c  |  d
--------------
a | 1,2 | 0,0
b | 0,0 | 2,1


>>>The input at terminal will look like following : 

############################################ RUNNING AT TERMINAL #############################################

No. of players : 2
No. of strategies of player 0 : 2
enter the strategy set of player 0 (please enter 2 strategies seperated by space): a b
No. of strategies of player 1 : 2
enter the strategy set of player 1 (please enter 2 strategies seperated by space): c d
utilities at strategies ['a', 'c'] (Enter 2 values as utilities of all 2 players seperated by spaces): 1 2
utilities at strategies ['a', 'd'] (Enter 2 values as utilities of all 2 players seperated by spaces): 0 0
utilities at strategies ['b', 'c'] (Enter 2 values as utilities of all 2 players seperated by spaces): 0 0
utilities at strategies ['b', 'd'] (Enter 2 values as utilities of all 2 players seperated by spaces): 2 1

############################################ RUNNING AT TERMINAL #############################################
