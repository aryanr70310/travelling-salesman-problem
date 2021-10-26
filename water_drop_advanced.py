############
############ ALTHOUGH I GIVE YOU THE 'BARE BONES' OF THIS PROGRAM WITH THE NAME
############ 'skeleton.py', YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR
############ THE PURPOSES OF THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT
############ THIS PROGRAM IS STILL CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES!
############

import os
import sys
import time
import random

############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############

input_file = "AISearchfile098.txt"

############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

the_particular_city_file_folder = "city-files"
print("../" + the_particular_city_file_folder + "/" + input_file)
if os.path.isfile("D:/Year 2 Projects/AI SEARCH/qcfb85/" + the_particular_city_file_folder + "/" + input_file):#line changed
#if os.path.isfile("../" + the_particular_city_file_folder + "/" + input_file):
    ord_range = [[32, 126]]
    #file_string = read_file_into_string("../" + the_particular_city_file_folder + "/" + input_file, ord_range)
    file_string = read_file_into_string("D:/Year 2 Projects/AI SEARCH/qcfb85/" + the_particular_city_file_folder + "/" + input_file, ord_range)#line changed
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the folder '" + the_particular_city_file_folder + "'.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############

############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME, E.G., 'abcd12'.
############

#code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs("../alg_codes_and_tariffs.txt")
code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs("D:/Year 2 Projects/AI SEARCH/qcfb85/alg_codes_and_tariffs.txt")#line changed

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR USER-NAME, E.G., "abcd12"
############

my_user_name = "qcfb85"

############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############

my_first_name = "Aryan"
my_last_name = "Rao"

############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############

algorithm_code = "WD"

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the agorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############

added_note = ""

############
############ NOW YOUR CODE SHOULD BEGIN.
############

"""Go to line 517 to start, the IWD algorithm and formula's used are based on and derived from this article:
   https://iajit.org/PDF/Vol.%2013,%20No.%206/6351.pdf,
   The Genetic algorithm I've implemented was inspired by this article:
   https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
   The breed function used is the exact same as used in the article"""

def avg_dist(avg):
    # calculates average distance of eb=ntire dist_matrix
    # this is used as a constant for some calculations
    for i in dist_matrix:
        for j in i:
            avg+=j
    return avg/num_cities**2

def gen_matrix(n,mat):
    # Used to create the soil matrix which contains soil between nodes(soil_mat[][])
    # n is the value to fill the matrix with, mat is the matrix to be returned
    mat=[num_cities*[n] for i in range(0,num_cities)]
    return mat

def min_dist(current_city,available_cities,mini):
    # calculates the smallest possible distance from current city to a random city
    # used in the g_soil() function to deal with negative values
    for i in range(0,len(available_cities)):
        if mini>soil_mat[current_city][available_cities[i]]:
            mini=soil_mat[current_city][available_cities[i]]

    return mini

def g_soil(val,mini):
    # function used to avoid negative values for generating probability distribution
    # val is the distance, mini is the minimum distance
    if mini>=0:
        return val
    else:
        return val-mini

def f_soil(val,mini):
    # returns probaility for water drop to choose city with soil=val
    return 1/(0.001+g_soil(val,mini))

def prob_calc(current_city,available_cities,prob_list):
    # generates a list of probabilities corresponding to the soil value from the current city to each available city
    # prob_list is the list of probabilties to be returned
    mini=min_dist(current_city,available_cities,99999999999) # minimum soil between nodes
    for i in range(0,len(available_cities)):
        prob_list.append(f_soil(soil_mat[current_city][available_cities[i]],mini)) # probabilities are generated
    prob_list=[item/sum(prob_list) for item in prob_list]
    return prob_list

def drops(visited,unvisited,a_tour_length,pos):
    # Executes every time a drop makes a cycle
    # visited and unvisited are lists storing what their name states and a_tour_length stores the tour_length
    # visited is returned when it contains a full tour and a_tour length and soil_iwd is also returned
    # vel_iwd stores the velocity of each drop and soil_iwd stores the soil stored in each droplet
    global soil_iwd,vel_iwd
    for i in range(0,num_cities-1):
        unvisited=list(set(unvisited)-set(visited))
        next_city=random.choices(unvisited,prob_calc(visited[i],unvisited,[]),k=1)[0]
        # random.choices is used to utilize a weighted probability with the help of prob_calc()

        a_tour_length+=dist_matrix[visited[i]][next_city]

        vel_iwd[pos]+=1000000/(0.01+((1)*(soil_mat[visited[i]][next_city]**2))) 
        # formula used: vel_iwd = a_v/(b_v+(c_v*(soil(i,j)**2))
        # a_v=1000000,b_v=0.01,c_v=1

        time=dist_matrix[visited[i]][next_city]**2/(vel_iwd[pos])
        # formula used: time(i,j) = HUD(i,j)/vel_iwd, HUD is Heuristic Undesirability
        # HUD(i,j)= dist_between(i,j)**2 (enhancement)

        delta_soil=10000/(0.01+((1)*time**2))
        # formula used: delta_soil(i,j)= a_s/(b_s+(c_s*(time(i,j)**2))
        # a_s=10000,b_s=0.01,c_s=1
        delta_soil*=avg**2/0.01+dist_matrix[visited[i]][next_city]**2
        # enhancement: delta_soil has been scaled to depend more on the distance between cities
        # avg distance is utitlized here to get sensible values

        soil_mat[visited[i]][next_city]=(1-0.05)*(soil_mat[visited[i]][next_city])-0.05*delta_soil
        # formula used: soil(i,j) = (1-p_s)*soil(i,j) - p_s*delta_soil(i,j)
        # p_s = 0.05
        soil_iwd[pos]+=delta_soil # soil_iwd is incremented by delta_soil(i,j)
        visited.append(next_city)

    a_tour_length+=dist_matrix[next_city][visited[0]]

    vel_iwd[pos]+=1000000/(0.01+((1)*soil_mat[next_city][visited[0]]**2))

    time=dist_matrix[next_city][visited[0]]**2/(vel_iwd[pos])
    delta_soil=10000/(0.01+((1)*time**2))
    delta_soil*=avg**2/0.01+dist_matrix[next_city][visited[0]]**2

    soil_mat[next_city][visited[0]]=(1-0.05)*(soil_mat[next_city][visited[0]])-0.05*delta_soil
    soil_iwd[pos]+=delta_soil
    # the lines at the end are for the computation of the path from the last city back to the first
    # they follow the same formulas used in the loop

    return visited,a_tour_length,soil_iwd[pos],vel_iwd[pos]

def water_cycle(num_drops,Best_tour):
    # Executes each time the water drops need to make a cycle
    # num_drops is the number of water drops and, 
    # Best_tour is to be returned, it contains a water drops(the best one)' tour,the tour's length and the soil_iwd for said water drop
    for i in range(num_drops):
        d=drops([random.randint(0,num_cities-1)],list(range(0,num_cities)),0,i)
        # d stores data for each drop
        if i==0:
            Best_tour.append(d[0])
            Best_tour.append(d[1])
            Best_tour.append(d[2])
        elif d[1]<Best_tour[1]:
            Best_tour[1]=d[1]
            Best_tour[0]=d[0]
            Best_tour[2]=d[2]
            # This block of if...elif statements ensures that the Best_tour stores data for the best tour of the cycle

    return Best_tour

def cycles(num_cycles):
    # A sort of main function which indirectly calls every function
    # contains a loop which executes for evey iteration/cycle of water drops
    # num_cycles is the number of iterations/cycles
    global soil_iwd,vel_iwd
    for i in range(0,num_cycles):
        # soil_iwd and vel_iwd are reset for every cycle
        soil_iwd=[0]*num_cities # init_soil_iwd = 0
        vel_iwd=[200]*num_cities # init_velocity = 200

        Best_tour=water_cycle(num_cities,[]) # Best_tour for current water cycle

        if Best_tour[0] not in current_population:
            current_population.append(Best_tour[0]) # The population for the genetic algorithm increments every cycle
        for j in range(0,num_cities):
            # The loop iterates through the best tour adjusting the soil values for each node on the best tour
            # formula used: soil(i,j)= (1+p_iwd)*soil(i,j)-((p_iwd)*(1/num_cities-1)*soil_iwd/tour_length)
            # p_iwd=0, enhancement: I have added the total tour length to the formula for better results
            if j==(num_cities-1):
                soil_mat[Best_tour[0][j]][Best_tour[0][0]]=((1)*soil_mat[Best_tour[0][j]][Best_tour[0][0]])-((1)*(1/(num_cities-1))*(Best_tour[2]/Best_tour[1]))
                 
            else:
                soil_mat[Best_tour[0][j]][Best_tour[0][j+1]]=((1)*soil_mat[Best_tour[0][j]][Best_tour[0][j+1]])-((1)*(1/(num_cities-1))*(Best_tour[2]/Best_tour[1]))
    print(Best_tour)
    return Best_tour

def generate_sample_routes(a_tour,population,num): 
    # generates random tours and returns them
    for i in range(0,num_cities):
        a_tour.append(i)
    for i in range(num):
        population.append(random.sample(a_tour,num_cities))
    return population

def invert_distance(f):
    # inverts input and returns it
    return (float(1/f))

def sort(fitness,population,t):
    # sorts population by fitness values
    for i in range(0,len(fitness)-1):
        for j in range(i,len(fitness)):
            if fitness[i]<fitness[j]:
                t[0],t[1]=fitness[i],population[i]
                fitness[i],population[i]=fitness[j],population[j]
                fitness[j],population[j]=t[0],t[1]

    return population,fitness

def fitness_calculator(population,fitness):
    # calculates fitness for every member of the population and returns it
    for i in range(0,pop_size):
        for j in range(0,num_cities-1):
            fitness[i]+=dist_matrix[population[i][j]][population[i][j+1]]
        fitness[i]+=dist_matrix[population[i][num_cities-1]][population[i][0]]
        fitness[i]=invert_distance(fitness[i]) # fitness = 1/distance

    return fitness

def mutate(citizen,pos1,pos2):
    # executes randomly and swaps 2 random cities, which is a mutation
    pos1=random.randint(0,num_cities-1)
    pos2=random.choice(list(set(citizen)-set([pos1])))
    # while True:
    #     pos2=random.randint(0,num_cities-1)
    #     if pos1!=pos2: break
    citizen[pos1],citizen[pos2]=citizen[pos2],citizen[pos1]
    return citizen

def breed(parent1, parent2,child,P1,P2):
    # Returns a 'child' from 2 citizens from the population
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        P1.append(parent1[i])   
    P2 = [e for e in parent2 if e not in P1]
    child = P1+P2
    return child

def create_children(parents,children,n):
    # generates 2 children for 2 parents for n iterations
    for i in range(0,n-1,2):
        children.append(breed(parents[i],parents[i+1],[],[],[]))
        children.append(breed(parents[i+1],parents[i],[],[],[]))
    return children

def selecting_next_gen(population,new_population,mutation_rate):
    parent_sample=int(0.8*pop_size) # These tours will create children 

    new_population.extend(create_children(population[:parent_sample],[],parent_sample))# children are appended and are to be 80% of the population

    for i in range(len(new_population)):
        if random.random()<mutation_rate:
            new_population[i]=mutate(new_population[i],0,0) # Children may mutate randomly

    for i in range(0,(int)(0.2*pop_size)):
        new_population.append(population[i]) # The best 20% tours are the elites and they always move to the next generation

    return new_population

def genetics(current_population,population_fitness,pop_size,num_generations):
    # a sort of main function for the genetic algorithm

    for i in range(num_generations):
        fitness_sorted=sort(population_fitness,current_population,[0,[]])
        current_population,population_fitness=fitness_sorted[0],fitness_sorted[1]
        # population is sorted by fitness
        current_population=selecting_next_gen(current_population,[],0.1) # new generation is created
        population_fitness=fitness_calculator(current_population,[0]*pop_size) # fitness is calculated

    fitness_sorted=sort(population_fitness,current_population,[0,[]])
    current_population,population_fitness=fitness_sorted[0],fitness_sorted[1] # last generation is sorted

    min_dist=0 # smallest tour length

    for i in range(0,num_cities-1):
        min_dist+=dist_matrix[current_population[0][i]][current_population[0][i + 1]]
    min_dist+=dist_matrix[current_population[0][num_cities - 1]][current_population[0][0]] # smallest tour_length is calculated

    return current_population[0],min_dist # Best_tour is returned

num_cycles=40 # 40 cycles
soil_mat=gen_matrix(20000,[]) # init_soil = 20000
avg=avg_dist(0) # average distance is calculated

current_population=[] # holds population of tours
population_fitness=[] # holds fitness values corresponding to current_population

cycles(num_cycles) # The IWD algorithm is applied and the current_population is filled up

pop_size=120 # population size is 120
num_generations=(8*pop_size) # num_generations is initialized

if len(current_population)<pop_size: # fills up population in case len(population)<intended length
    current_population.extend(generate_sample_routes([],[],pop_size-len(current_population))) # generate_sample_routes generates extra tours

population_fitness=fitness_calculator(current_population,[0]*pop_size) # fitness is calculated for first generation

Best_tour = genetics(current_population,population_fitness,pop_size,num_generations)# enhancement
# Best_tour stores the best tour from the genetic algorithm
print(Best_tour)
tour,tour_length=Best_tour[0],Best_tour[1] # values of Best_tour are stored














############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1}, AND YOU SHOULD ALSO
############ HOLD THE LENGTH OF THIS TOUR IN THE RESERVED INTEGER VARIABLE 'tour_length'.
############

############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE,
############ WHOSE NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATA AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")
    
    











    


