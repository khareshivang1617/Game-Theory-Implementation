from itertools import combinations
import pulp as p

def checkMSNE(supp1, supp2, u, m, n):
    #1st check for all strategies in supp1, supp2 finally has a solution or not...
    z1=[] 
    for s1 in supp1:
        z1.append(p.LpVariable(f"z1({s1})", lowBound = 0))

    z2=[] 
    for s2 in supp2:
        z2.append(p.LpVariable(f"z2({s2})", lowBound = 0))

    c = p.LpVariable("c")

    #################################################
    Lp_prob1 = p.LpProblem('Problem', p.LpMinimize)
    Lp_prob1+=0

    for s1 in supp1:
        u1=0
        for i in range(len(z2)):
            u1+=z2[i]*u[s1][supp2[i]][0]
        Lp_prob1 += u1==c#max and equal case...

    for s1 in range(m):
        if s1 not in supp1:#all the strategies which don't belong to the support...
            u1=0
            for i in range(len(z2)):
                u1+=z2[i]*u[s1][supp2[i]][0]
            Lp_prob1 += c>=u1#greater than all non support strategies case...

    sum_of_z2=0
    for z in z2:
        sum_of_z2 += z
    Lp_prob1 += sum_of_z2==1#sum of all prob in z2 is 1

    #print(Lp_prob1)
    status1 = Lp_prob1.solve()
    
    
    #################################################
    Lp_prob2 = p.LpProblem('Problem', p.LpMinimize)
    Lp_prob2+=0

    for s2 in supp2:
        u2=0
        for i in range(len(z1)):
            u2+=z1[i]*u[supp1[i]][s2][1]
        Lp_prob2 += u2==c#max and equal case...

    for s2 in range(n):
        if s2 not in supp2:#all the strategies which don't belong to the support...
            u2=0
            for i in range(len(z1)):
                u2+=z1[i]*u[supp1[i]][s2][1]
            Lp_prob2 += c>=u2#greater than all non support strategies case...

    sum_of_z1=0
    for z in z1:
        sum_of_z1 += z
    Lp_prob2 += sum_of_z1==1#sum of all prob in z2 is 1

    #print(Lp_prob2)
    status2 = Lp_prob2.solve()
    #print(p.LpStatus[status1])
    #print(p.LpStatus[status2])

    if p.LpStatus[status1]=="Optimal" and p.LpStatus[status2]=="Optimal":
        print(f"MSNE Exists : ", end=" ")
        print(f"P1 : ", end=" ")
        for z in z1:
           print(f"{z} = {p.value(z)} ",end=" ")
        #print(f"z1(rest) = 0", end=" ")
        print(f"; P2 : ", end=" ")
        for z in z2:
            print(f"{z} = {p.value(z)} ", end=" ")
        #print(f"z2(rest) = 0", end=" ")
        print()
        
    
    else:
        print("No MSNE Exists")
    #print("-----------------")

def main():

    fileName = input("Enter the input file name : ")
    File = open(fileName, 'r')
    content = File.readlines()
    
    line0 = content[0]
    m_str, n_str = line0.split(" ")

    m = int(m_str)
    n = int(n_str)

    #print(f"{m},{n}")

    u=[]
    for line in content:
        if line!=content[0]:
            line_list=list(line.split(" "))
            row=[[int(line_list[2*j]),int(line_list[2*j+1])] for j in range(n)]
            u.append(row)
        
    
    #u = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    #u = [[[1, -1], [2, -2]], [[3, -3], [4, -4]]]


    s1 = [i for i in range(m)]#strategies of player 1 (by index only)
    s2 = [j for j in range(n)]#strategies of player 1 (by index only)

    #u = [[list(map(int, input(f"(Enter the 2 utilities of both players seperated by spaces) u[{s1[i]},{s2[j]}] : ").split())) for i in range(m)] for j in range(n)]
    
    print(f"No. of strategies of player 0 : {m}\nNo. of strategies of player 1 : {n}")

    print("\n\nUtility matrix is : ")
    print(u)
    print("\n\n*****************************************\n")

    for size1 in range(1,m+1):
        for size2 in range(1,n+1):

            comb1 = combinations(s1,size1)

            for supp1 in comb1:
                comb2 = combinations(s2,size2)
                for supp2 in comb2:
                    print(f"checking for the support : {list(supp1)} X {list(supp2)}")
                    checkMSNE(supp1,supp2,u,m,n)
                    print("\n*****************************************\n")

















main()