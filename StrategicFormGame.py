import numpy as numpy_array

##############################################################for taking utility input from users################################
def increment_curr_index(num_of_strategies, curr_index):
	n=len(num_of_strategies)
	curr_index[n-1]=curr_index[n-1]+1

	i=n-1
	while curr_index[i]==num_of_strategies[i] and i!=0:
		curr_index[i]=0
		curr_index[i-1]=curr_index[i-1]+1
		i=i-1

	#return curr_index

def take_utility_input(num_of_strategies, s, u, curr_index):
	n=len(num_of_strategies)
	
	if curr_index[0]==num_of_strategies[0]:
		return
	
	else:
		#print(f"enter the utility set for players for strategy profile {curr_index}")

		curr_index_tuple=tuple(curr_index)
		strategy_profile=[]

		for i in range(n):
			strategy_profile.append(s[i][curr_index[i]])

		u[curr_index_tuple]=list(map(int, input(f"utilities at strategies {strategy_profile} (Enter {n} values as utilities of all {n} players seperated by spaces): ").split()))#go to the location in the numpy array of utilities and insert the utility of all the players w.r.t. that profile
		#for i in range(n):
			#u[curr_index_tuple].append(int(input()))#go to the location in the numpy array of utilities and insert the utility of ith player for that particular profile played

		increment_curr_index(num_of_strategies,curr_index)
		take_utility_input(num_of_strategies, s, u, curr_index)
######################################################################################################################################################


###################################finding all SDS and WDS#########################################################################
def append_curr_index_except(i, curr_index, num_of_strategies):#appends the current indices but excludes the ith one...
	#assuming that the curr_index[i] was 0 so far...
	#print(f"before append {curr_index}")


	increment_curr_index(num_of_strategies, curr_index)

	if curr_index[i]==1:#which means this one is incremented...

		if i==0:
			curr_index[0]=-1

		else:
			curr_index[i]=0
			curr_index[i-1]=curr_index[i-1]+1
			j=i-1
			while curr_index[j]==num_of_strategies[j] and j!=0:
				curr_index[j]=0
				curr_index[j-1]=curr_index[j-1]+1
				j=j-1

			if curr_index[0]==num_of_strategies[0]:
				curr_index[0]=-1
	#print(f"after append {curr_index}")

###################################functions to find SDS###########################################
def SDS_given_others(i, curr_index, u, strategy_count): #permute over the ith of curr_indices and check the index giving best utility to player i

	#print(curr_index)
	max_index=0
	curr_index[i]=0
	curr_index_tuple=tuple(curr_index)
	max_utility=u[curr_index_tuple][i]

	for j in range (1, strategy_count):
		curr_index[i]=j
		curr_index_tuple=tuple(curr_index)
		
		if max_utility<u[curr_index_tuple][i]:
			max_utility=u[curr_index_tuple][i]
			max_index=j

		elif max_utility==u[curr_index_tuple][i]:
			max_index=-1

	curr_index[i]=0
	return max_index


def all_strongly_dominant_strategies(n, num_of_strategies, u):
	#for a particular player his/her SDS will be the one which is always his/her best stratgy for any other players
	index_of_SDS=[] #to store the index of the strategy of each player which is SDS	

	for i in range(n):
		#for each set of strategies of other players, it must give the ith player a max utility, and this strategy index must be common in all cases...
		#we need to permute over all the indices of curr index other than i
		curr_index=[]
		for x in range(n):
			curr_index.append(0)

		common_SDS_index=SDS_given_others(i,curr_index, u, num_of_strategies[i])#given the strategy set of other players in the curr_index, find the best strategy for ith player, and that too the strongly greater over all, else it will return -1
		append_curr_index_except(i, curr_index, num_of_strategies)#appends the curr_index except ith to change the strategy set of other players, once all permutations done it will always make curr_indezx[0]==-1 or something lyk that

		while curr_index[0]!=-1 and common_SDS_index!=-1:
			SDS_index=SDS_given_others(i,curr_index, u, num_of_strategies[i])#given the strategy set of other players in the curr_index, find the best strategy for ith player, and that too the strongly greater over all, else it will return -1
			append_curr_index_except(i,curr_index,num_of_strategies)#appends the curr_index except ith to change the strategy set of other players, once all permutations done it will always make curr_indezx[0]==-1 or something lyk that
			
			if common_SDS_index!=SDS_index:#that means that there doesn't exits any common best strategy for all cases...
				common_SDS_index=-1
				break

		index_of_SDS.append(common_SDS_index)

	return index_of_SDS

#####################################################################################################

###################################functions to find WDS############################################

def WDS_given_others(i, curr_index, u, strategy_count):#permute over the ith of curr_indices and check the index giving best utility to player i
	#print(curr_index)
	max_index=[0]
	curr_index[i]=0
	curr_index_tuple=tuple(curr_index)
	max_utility=u[curr_index_tuple][i]

	for j in range (1, strategy_count):
		curr_index[i]=j
		curr_index_tuple=tuple(curr_index)
		
		if max_utility<u[curr_index_tuple][i]:
			max_utility=u[curr_index_tuple][i]
			max_index=[j]

		elif max_utility==u[curr_index_tuple][i]:
			max_index.append(j)

	curr_index[i]=0
	return max_index

def all_weakly_dominant_strategies(n, num_of_strategies, u):
		#for a particular player his/her SDS will be the one which is always his/her best stratgy for any other players
	indices_of_WDS=[] #to store the index of the strategy of each player which is SDS

	for i in range(n):
		#for each set of strategies of other players, it must give the ith player a max utility, and this strategy index must be common in all cases...
		#we need to permute over all the indices of curr index other than i
		curr_index=[]
		for x in range(n):
			curr_index.append(0)

		common_WDS_indices=WDS_given_others(i,curr_index, u, num_of_strategies[i])#given the strategy set of other players in the curr_index, find the best strategy sets for ith player, that are weakly dominant
		append_curr_index_except(i, curr_index, num_of_strategies)#appends the curr_index except ith to change the strategy set of other players, once all permutations done it will always make curr_indezx[0]==-1 or something lyk that

		while curr_index[0]!=-1:
			WDS_indices=WDS_given_others(i,curr_index, u, num_of_strategies[i])#given the strategy set of other players in the curr_index, find the best strategy sets for ith player, that are weakly dominant
			append_curr_index_except(i,curr_index,num_of_strategies)#appends the curr_index except ith to change the strategy set of other players, once all permutations done it will always make curr_indezx[0]==-1 or something lyk that
			common_WDS_indices=[index for index in common_WDS_indices if index in WDS_indices]#finding the indices which are max and equal among all cases so far...

			if len(common_WDS_indices)==0: #i.e. the list becomes empty, which means there doesn't exists any strategy for ith player so far such that its the best case for all other players strategies
				 break#cuz there doesn't exist any WDS in this case...

		if len(common_WDS_indices)==num_of_strategies[i]:#the case where all the strategies are the best strategies, there doesn't exist any dominated strategy...
			common_WDS_indices=[]
		indices_of_WDS.append(common_WDS_indices)

	return indices_of_WDS

####################################################################################################

################################MAXMIN##############################################################

def maxmin_strategies(n, num_of_strategies, u, s):
	#first for each strategy of a player i, find a minimum utility he/she can have

	for i in range(n):
		#now we are at player i

		curr_index=[]
		for k in range(n):
			curr_index.append(0)

		maxmin_strategy_index=[0]#assuming it to be 0th index at first, and comparing accordingly
		min_value=u[tuple(curr_index)][i]#it will store min value for 0th index after the loop

		while curr_index[0]!=-1:
			#print("0000000000000000000000000000000000")
			if u[tuple(curr_index)][i]<min_value:
				min_value=u[tuple(curr_index)][i]
			append_curr_index_except(0, curr_index,num_of_strategies)		
		#now we have the min utility for 0th index

		maxmin_value=min_value#at first, assigning the minmax_value as the min_value for 0th index,, next we will compare with each and insert accordingly

		for j in range(1,num_of_strategies[i]):#for each strategy j of the ith player
			
			for k in range(n):
				curr_index[k]=0

			curr_index[i]=j#in the tuple assigning ith player(for which we are finding) the strategy j always
			min_value=u[tuple(curr_index)][i]
			curr_index[i]=0
			#append_curr_index_except(i,curr_index, num_of_strategies)

			while curr_index[0]!=-1:
				#print(f"***************************************{j}")
				curr_index[i]=j#keeping the strategy of ith player as j always
				if u[tuple(curr_index)][i]<min_value:
					min_value=u[tuple(curr_index)][i]
				curr_index[i]=0
				append_curr_index_except(i, curr_index, num_of_strategies)

			if maxmin_value<min_value: #which means that jth index is the best so far

				maxmin_strategy_index=[j]
				maxmin_value=min_value#that's how we find the maxmin
			
			elif maxmin_value==min_value: #the case where two maxmin strategy may exist
				maxmin_strategy_index.append(j)


		print(f"for player {i}, maxmin strategies are : ", end=" ")

		for index in maxmin_strategy_index:
			print(f"{s[i][index]} ", end=" ")

		print(f"\nCorr maxmin value : {maxmin_value}")

def minmax_strategies(n, num_of_strategies, u, s):

	for i in range(n):
		#we are at player i
		#for each strategy profile of other players, we need to find the maximum utility of player i

		curr_index=[]
		for k in range(n):
			curr_index.append(0)

		#finding max utility for the strategy profile [0,0,0...]

		max_value=u[tuple(curr_index)][i]
		
		for j in range (num_of_strategies[i]):
			curr_index[i]=j
			if u[tuple(curr_index)][i]>max_value:
				max_value=u[tuple(curr_index)][i]
			
		curr_index[i]=0
		minmax_value=max_value
		minmax_strategies=[curr_index.copy()]

		append_curr_index_except(i, curr_index, num_of_strategies)

		while curr_index[0]!=-1:

			#for this part we will find the max utility of player i corr to curr_index, then we will compare this...
			max_value=u[tuple(curr_index)][i]
			
			for j in range (num_of_strategies[i]):
				curr_index[i]=j
				if u[tuple(curr_index)][i]>max_value:
					max_value=u[tuple(curr_index)][i]#assigning new max for the current profile
		
			curr_index[i]=0

			if minmax_value>max_value:#we got a better minimization of max utilities
				minmax_value=max_value
				minmax_strategies=[curr_index.copy()]
				#print(f"1 minmax strategy update : {curr_index} : {minmax_strategies}")
			
			elif minmax_value==max_value:#the case when two minmax profile of other players co-exists
				#print(f"2 minmax strategy update : {curr_index}")
				minmax_strategies.append(curr_index.copy())

			append_curr_index_except(i, curr_index, num_of_strategies)
			#print(f"3 minmax strategy update : {minmax_strategies}")

		#print(f"4 minmax strategy update : {minmax_strategies}")
		print(f"for player {i}, the minmax strategy of other players is : ",end=" ")
		#print(minmax_strategies)
		for curr_index in minmax_strategies:
			#####print accordingly...
			#print(curr_index)
			for _i in range(n):
				if (_i!=i):
					print(f"s[{_i}]={s[_i][curr_index[_i]]}, ", end = " ")

			print("")
		print(f"corr minmax value is : {minmax_value}")



######################################PSNEs#####################################################
def check_PSNE(n, num_of_strategies, curr_index, u):
	#this function will check whether the curr_index is the best strategy also for rest of the players other than 0th player
	curr_index_temp=curr_index.copy()

	for i in range(1,n):
		max_utility_Pi=u[tuple(curr_index_temp)][i]
		for j in range(num_of_strategies[i]):
			curr_index_temp[i]=j#iterating for every strategy of player i
			if max_utility_Pi<u[tuple(curr_index_temp)][i]:#this means what we assumed as max utility for ith player, it wasn't actually
				return False#the curr_index is not the PSNE therefore..

	return True#true will be returned if all cases passed...

def PSNEs(n, num_of_strategies, u, s):
	curr_index=[]
	for i in range(n):
		curr_index.append(0)

	while (curr_index[0]!=-1):
		max_utility_P0=u[tuple(curr_index)][0]#setting the max_utility for player 0th at first according to the strategies of rest of the player
		max_index_P0=[0]
		for i in range(1, num_of_strategies[0]):
			curr_index[0]=i
			if max_utility_P0<u[tuple(curr_index)][0]:
				max_utility_P0=u[tuple(curr_index)][0]
				max_index_P0=[i]

			elif max_utility_P0==u[tuple(curr_index)][0]:
				max_index_P0.append(i)

		for index in max_index_P0:
			curr_index[0]=index#corr to rest players strategy this one's the best for player 0th
			if check_PSNE(n, num_of_strategies, curr_index, u):
				print(f"PSNE : [", end="")
				for i in range(n-1):
					print(f"{s[i][curr_index[i]]},",end="")
				print(f"{s[n-1][curr_index[n-1]]}",end="")
				print(f"] ; utilities={u[tuple(curr_index)]}")
		
		curr_index[0]=0
		append_curr_index_except(0,curr_index,num_of_strategies)#we have checked and now we are doing the same for another profile of rest players

##################################################################################################
def main():


#########################################################################################

	n=int(input("No. of players : "))#no. of dimensions in of the utility array
	s=[]#the array containing all the strategies of all the players
	num_of_strategies=[]#the array containing the number of strategies each player is having
	curr_index=[]#this represent the index of the strategy at current being played by each player in the game

	for i in range(n):
		
		size=int(input(f"No. of strategies of player {i} : "))
		num_of_strategies.append(size)#storing the no. of strategies of each player in a seperate list cuz they are the length of a particular dimension in the array
		curr_index.append(0)
		#strategy_set=[]#strategy set of ith player
		#for j in range(size):
			#strategy_set.append(input(f"{j} th move of player {i}: "))

		s.append(input(f"enter the strategy set of player {i} (please enter {num_of_strategies[i]} strategies seperated by space): ").split())

	u=numpy_array.empty(num_of_strategies, dtype=object)

	take_utility_input(num_of_strategies,s, u, curr_index)

	print("\n\nThe utility matrix is : \n")
	print(u)

	SDS_indices=all_strongly_dominant_strategies(n, num_of_strategies, u)#this will store the strongly dominant strategy of each of the n players
	#weakly_dominant_strategies=all_weakly_dominant_strategies()#this will store the strongly dominant strategy of each of the n players

	print(f"\n\nBy indices the strongly dominant strategies are : {SDS_indices}")

	#####SDS and SDSEs#############################################################
	SDSE_strategy_profile=[]
	#SDSE_indices=[]
	SDSE_exists=True

	for i in range(n):
		if SDS_indices[i]!=-1:
			print(f"SDS for player {i} is : {s[i][SDS_indices[i]]}")
			SDSE_strategy_profile.append(s[i][SDS_indices[i]])
			#SDSE_indices.append(SDS_indices)

		else:
			print(f"SDS for player {i} is : Doesn't exist")
			SDSE_exists=False



	if SDSE_exists:
		print(f"\n\nSDSE strategy profile set : {SDSE_strategy_profile}")
		print(f"corr utilities : {u[tuple(SDS_indices)]}")

	else:
		print("\n\nNo SDSE exists")
	

	#################################################################################

	########WDS and WDSEs############################################################

	WDS_indices=all_weakly_dominant_strategies(n, num_of_strategies,u)

	print(f"\n\nBy indices the weakly dominant strategies are : {WDS_indices}")

	WDSE_strategy_profile=[]
	#WDSE_indices=[]#just for converting it to tuple so as to display the utilities in the equilibria
	WDSE_exists=True

	for i in range(n):
		if len(WDS_indices[i])==0:
			print(f"WDS for player {i} is : Doesn't exists")
			WDSE_exists=False
		else:
			print(f"WDS for player {i} is : ", end=" ")
			#WDSE_indices.append(WDS_indices[i][0])

			WDSE_strategy_profile_at_i=[]
			for index in WDS_indices[i]:
				print(f"{s[i][index]} ",end=" ")
				WDSE_strategy_profile_at_i.append(s[i][index])

			WDSE_strategy_profile.append(WDSE_strategy_profile_at_i)

			print("")

	if WDSE_exists:
		print(f"\n\nWDSE strategy profile set : {WDSE_strategy_profile}")

		#print(f"corr utilities : {u[tuple(WDSE_indices)]}")

	else:
		print("\n\nNo WDSE exists")

	print("\n\n")

	PSNEs(n, num_of_strategies, u, s)

	print("\n\n")
	
	maxmin_strategies(n, num_of_strategies, u, s)
	
	print("\n\n")
	
	minmax_strategies(n, num_of_strategies, u, s)

	print("\n\n")
	#print("")
				
	#####################################################################################




main()