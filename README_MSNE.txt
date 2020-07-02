- Please make sure that the libraries 'itertools' and 'pulp are already installed'
- To install pulp : "pip install pulp"
- Make an input file (the format is given below)
- Run the program and pass the input file name.
- To Run : "python MSNE.py"

Input Format : 
-make any input file (say input.txt)
-first line, enter m and n (no. of strategies of both the players)
-next m lines contains the n row utility inputs of both the players.
- be careful to leave exactly one space please!

For Example : 
  | L   | M
-------------
T | 1,0 | 1,2
B | 0,3 | 0,1


The above game's details can be simply entered as...

2 2
1 0 1 2
0 3 0 1

(first line is 2X2 matrix, and rest are utilities)


NOTE : I have considered strategies by index (didn't considered to input the strategy names!), all strategies will be by index.
     : All Indices start from zero!
     : For finding MSNE, I'm just displaying the prob distribution in case a support is found be MSNE cuz the strategies not belonging to the support were already condsidered to not be played, it can be PSNE also.
