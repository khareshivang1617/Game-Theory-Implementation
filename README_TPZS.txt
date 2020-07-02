- Please make sure that the library 'pulp are already installed'
- To install pulp : "pip install pulp"
- Make an input file (the format is given below)
- Run the program and pass the input file name.
- To Run : "python 2player0sumgame.py"

Input Format : 
-make any input file (say input.txt)
-first line, enter m and n (no. of strategies of both the players)
-next m lines contains the n row utility inputs of matrix.

For Example : 
  | L | M | N
-------------
T | 1 | 2 | 3
B | 4 | 5 | 6


The above game's details can be simply entered as...

2 3
1 2 3
4 5 6

(first line is 2X3 matrix, and rest are utilities)


NOTE : I have considered strategies by index (didn't considered to input the strategy names!), all strategies will be by index.
     : All Indices start from zero!
     : In case if there exists infinite MSNE in TPZS, my code outputs only one of them, because its the multiple PSNE case. 