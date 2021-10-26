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

input_file = "AISearchfile048.txt"

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
    file_string = read_file_into_string("D:/Year 2 Projects/AI SEARCH/qcfb85/" + the_particular_city_file_folder + "/" + input_file, ord_range)#line changed
    #file_string = read_file_into_string("../" + the_particular_city_file_folder + "/" + input_file, ord_range)
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

code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs("D:/Year 2 Projects/AI SEARCH/qcfb85/alg_codes_and_tariffs.txt")#line changed
#code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs("../alg_codes_and_tariffs.txt")

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

algorithm_code = "AC"

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

"""Go to line 452 to start, the ACO algorithm and formula's used are based on and derived from this video:
   https://www.youtube.com/watch?v=wfD5xlEcmuQ&ab_channel=GopalPrasadMalakar"""

def calc_mean(sum):# enhancement(check improve_phero_matrix(mean))
    # calculates mean distance value
    for i in dist_matrix:
        for j in i:
            sum+=j
    return sum/(num_cities**2)

def gen_matrix(n,mat):
    # Used to create the matrix of pheromones and,
    # the matrix that is used in updating the pheromone value after a group of ants complete a tour
    # n is the value to fill the matrix with, mat is the matrix to be returned
    mat=[num_cities*[n] for i in range(0,num_cities)]
    return mat

def improve_phero_matrix(mean):# enhancement
    # increases pheromone_between(i,j) if distance(i,j) is less than mean distance in dist_matrix and,
    # decreases it, if vice versa
    for i in range(0,num_cities):
        for j in range(0,num_cities):
            if dist_matrix[i][j]<mean:
                phero_matrix[i][j]+=0.2
            else:
                phero_matrix[i][j]-=0.1

def adjust_pheromones(m1,m2):
    # This function is used in updating the pheromone after a group of ants complete a tour
    # m1 is the pheromone count, m2 also known as matrix_of_change is to be added to the pheromone count
    for i in range(len(m1)):
        for j in range(len(m1)):
            m1[i][j]*=0.5 # evaporation factor E is 0.5
            m1[i][j]+=m2[i][j]

    return m1

def prob_calc(current_city,available_cities,prob_list):
    # generates a list of probabilities corresponding to the distance from the current city to each available city
    # prob_list is the list of probabilties to be returned
    for i in range(0,len(available_cities)):
        prob_list.append(((phero_matrix[current_city][available_cities[i]])**1.0)*(1/(0.01+dist_matrix[current_city][available_cities[i]]))**6.0)
        # The formula used is(pheromone_at(i,j)**a)*((1/dist_between(i,j))**B)
        # a=1.0, B=6.0, 0.01 is a small value to prevent division by 0 error
    
    prob_list=[item/sum(prob_list) for item in prob_list]
    return prob_list

def ant_tour(visited,unvisited,a_tour_length):
    # Executes every time an ant needs to make a tour
    # visited and unvisited are lists storing what their name states and a_tour_length stores the tour_length
    # visited is returned when it contains a full tour and a_tour length is also returned
    for i in range(0,num_cities-1):
        unvisited=list(set(unvisited)-set(visited))
        next_city=random.choices(unvisited,prob_calc(visited[i],unvisited,[]),k=1)[0]
        # random.choices is used to utilize a weighted probability with the help of prob_calc()

        a_tour_length+=dist_matrix[visited[i]][next_city]
        visited.append(next_city)
        # loop terminates after visited contains a full tour

    a_tour_length+=dist_matrix[next_city][visited[0]]
    # adding distance between last to first city
    return visited,a_tour_length

def ants_move_out(number_of_ants,l,matrix_of_change):
    # Executes each time a group of ants need to make an excursion
    # l stores the tour and tour_length of each ant, matrix_of_change stores the value for updating the phero_matrix
    for i in range(0,number_of_ants):
        start=random.choices(options,phero_home,k=1)[0]# enhancement
        # pheromones have been assigned to starting positions based on the quality of tours they produce
        # options is a list of each city, phero_home contains the pheromone count of each city
        ant=ant_tour([start],list(range(0,num_cities)),0)
        # ant_tour generates a tour for an ant and returns the tour and its length
        l.append(ant)

        for j in range(0,num_cities-1):
            matrix_of_change[ant[0][j]][ant[0][j+1]]+=num_cities/ant[1]
            # The value (Q/tour_length) is added to the matrix_of_change(i,j) which is later added to phero_matrix(i,j)
            # Q=num_cities

        matrix_of_change[ant[0][num_cities-1]][start]+=num_cities/ant[1] # adding to the pheromone count from last to first city
        phero_home[start]+=num_cities/ant[1] # phero_home is updated
    return l # the tour/tour_length of each ant is returned

def excursions(num_excursions,Mintour):
    # A sort of main function which indirectly calls every function
    # contains a loop which executes for evey iteration/excursion of the group of ants
    # num_excursion is the number of iterations/excursions, mintour stores the best tour and its length which is eventually returned
    for i in range(0,num_excursions):
        matrix_of_change=(gen_matrix(0,[])) # reset after each iteration

        tours=ants_move_out(10,[],matrix_of_change) # generates tour/tour_length for number_of_ants = 10

        adjust_pheromones(phero_matrix,matrix_of_change) # adjusts the pheromone values at each position based on the ants' tours

    Mintour=tours[0] # initially stores first tour of the last excursion
    # finds the actual smallest tour and stores it in mintour
    for i in tours:
        if Mintour[1]>i[1]:
            Mintour=i

    print(Mintour)
    return Mintour # best tour found by the ACO algorithm

def calc_dist(swapped,swaplen):
    # Calculates swaplen for swapped tour
    global mintour,b
    for i in range(0,num_cities-1):
        swaplen+=dist_matrix[swapped[i]][swapped[i + 1]]
    swaplen+=dist_matrix[swapped[num_cities - 1]][swapped[0]]
    # calculation occurs above

    if swaplen<mintour[1]:
        # if swapped tour is better, mintour will now become swapped tour
        mintour=[]
        mintour.append(swapped)
        mintour.append(swaplen)
        b=True

def three_opt(counter,swapped,swaplen): # enhancement
    # applies a sort of 3-opt algorithm to the best tour found by ACO
    # counter is the number of iterations, swapped will store adjusted array and swaplen will store its length
    global mintour,b

    while counter>0:
        swapped=[]# swapped is reset
        swapped.extend(mintour[0])# swapped will store the mintour

        a=random.choice(options) # swapping position 1
        b=random.choice(list(set(options)-set([a]))) # swapping position 2
        c=random.choice(list(set(options)-set([a,b]))) # swapping position 3
        
        # swapping will happen in the next few lines
        # 5 different scenarios with a, b and c being swapped will take place and calc_dist will calculate the distance
        # If the swapped tour is better in any one of the scenarios the loop will continue forgoing the rest of the statements
        # Boolean variable b is used to facilitate this process

        swapped[a],swapped[b]=swapped[b],swapped[a]# b a c
        calc_dist(swapped,swaplen)
        if b==True:
            b=False
            continue

        swapped[b],swapped[c]=swapped[c],swapped[b]# c a b
        calc_dist(swapped,swaplen)
        if b==True:
            b=False
            continue

        swapped[c],swapped[a]=swapped[a],swapped[c]# a c b
        calc_dist(swapped,swaplen)
        if b==True:
            b=False
            continue

        swapped[b],swapped[a]=swapped[a],swapped[b]# b c a
        calc_dist(swapped,swaplen)
        if b==True:
            b=False
            continue

        swapped[c],swapped[b]=swapped[b],swapped[c]# c b a
        calc_dist(swapped,swaplen)
        if b==True:
            b=False
            continue

        counter,swaplen=counter-1,0 # counter is decremented by 1 and swaplen is reset

    return mintour

phero_home=[1]*num_cities # initializing phero_home as a list filled with 1s
options=list(range(0,num_cities)) # list of all cities

phero_matrix=(gen_matrix(1,[])) # phero_matrix is intitalized to a matrix full of 1s
improve_phero_matrix(calc_mean(0)) # phero_matrix values are adjusted using the mean distance between cities

mintour=excursions(100,[]) # mintour is returned after num_excursions=100 excursions/iterations take place

b=False # b is initialized
three_opt(10*num_cities**2,[],0) # 3-opt algorithm is used to improve the rour returned by the ACO algorithm

print(mintour)
tour,tour_length=mintour[0],mintour[1]  # values of mintour are stored












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











    


