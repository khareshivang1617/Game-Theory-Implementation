import pulp as p


def main():

    fileName = input("Enter the input file name : ")
    File = open(fileName, 'r')
    content = File.readlines()
    
    line0 = content[0]
    m_str, n_str = line0.split(" ")

    m = int(m_str)
    n = int(n_str)

    print(f"{m},{n}")

    a=[]
    for line in content:
        if line!=content[0]:
            row=list(map(int,line.split(" ")))
            a.append(row)


    print("Values of the array : \n")

    print (a)

    saddle_exists=False
    
    print("\n\nThe saddle points are : ")

    for i in range(m):
        
        row_min=a[i][0]
        corr_min_col_ind=[0]#it will contain the list of all min column indices for the corresponding i
        
        for j in range(1,n):
            
            if row_min > a[i][j]:
                row_min=a[i][j]
                corr_min_col_ind=[j]
            
            elif row_min == a[i][j]:
                corr_min_col_ind.append(j)

        for j in corr_min_col_ind: #these were the min in their row, now also checking them if they're max in the corr column
            col_max=True

            for k in range(m):
                if a[k][j]>a[i][j]:#if any other value in the corr column has the maxima
                    col_max=False

            if col_max:
                print(f"[{i},{j}] : {a[i][j]}")
                saddle_exists=True
        

    if saddle_exists==False:
        print("No saddle point exists")


    print("\n\nSolving LPs to find MSNEs... (In case of infinite MSNEs my program will output just one!)")

    ###########player 1##############################
    Lp_player1 = p.LpProblem('Problem1', p.LpMaximize)

    x=[]#the list containing the LP variables for Player 1
    for i in range(m):
        x.append(p.LpVariable(f"x{i}", lowBound=0))

    z = p.LpVariable("z")
    Lp_player1+=z#the variable to maximize

    for j in range(n):
        array_sum=0
        for i in range(m):
            array_sum+=a[i][j]*x[i]
        
        Lp_player1 += z-array_sum<=0

    sum_prob=0

    for i in range(m):
        sum_prob+=x[i]

    Lp_player1 += sum_prob==1

    #print(Lp_player1)
    status = Lp_player1.solve()
    #print(p.LpStatus[status])

    print("MSNE prob distribution for player 1 : ", end=" ")
    for i in range(m-1):
        print(f"{p.value(x[i])}", end=", ")
    print(f"{p.value(x[m-1])} ", end="; ")

    print(f"Expected utility : {p.value(Lp_player1.objective)}")


    ###########player 2##############################
    Lp_player2 = p.LpProblem('Problem2', p.LpMinimize)

    y=[]#the list containing the LP variables for Player 1
    for j in range(n):
        y.append(p.LpVariable(f"y{j}", lowBound=0))

    w = p.LpVariable("w")
    Lp_player2+=w#the variable to maximize

    for i in range(m):
        array_sum=0
        for j in range(n):
            array_sum+=a[i][j]*y[j]
        
        Lp_player2 += w-array_sum>=0

    sum_prob=0

    for j in range(n):
        sum_prob+=y[j]

    Lp_player2 += sum_prob==1

    #print(Lp_player2)
    status = Lp_player2.solve()
    #print(p.LpStatus[status])

    print("MSNE prob distribution for player 2 : ", end=" ")
    for j in range(n-1):
        print(f"{p.value(y[j])}", end=", ")
    print(f"{p.value(y[n-1])} ", end="; ")

    print(f"Expected utility : {(-1)*p.value(Lp_player2.objective)}\n\n")

main()