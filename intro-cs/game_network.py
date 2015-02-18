# It's been a little while since I've taken a look at this code I did for the Intro
# to Computer Science class at udacity.com. It was the final project and models a
# social network for computer games.
# All the implemented functions work as described.
# To do: Make a "Make-Your-Own-Procedure." I'll keep that comment section there 
# for now even though, or maybe because, it's an eyesore.
# To do: Turn this into a simple Flask app or something??
# Nick Clark, 2/17/2015

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def getNames(s):
    names2 = []
    while True:
        q = s.find(".")
        if q != -1:
            name=s[0:s.find(" ")]
            if name not in names2:
                names2.append(name)
            s = s[q+1:]
        else:
            return names2

def create_data_structure(string_input):
    names = getNames(string_input)
    network = {}
    for i in names:
        p = string_input.find(i+" is connected to")
        if p != -1:
            connectString = string_input[p+len(i)+17:string_input.find(".",p)]
            network[i] = [connectString.split(", ")]
    for i in names:
        p = string_input.find(i+" likes to play")
        if p != -1:
            gameString = string_input[p+len(i)+15:string_input.find(".",p)]
            network[i].append(gameString.split(", "))
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user not in network:
        return None
    return network[user][0]

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user not in network:
        return None
    return network[user][1]

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        if user_B not in network[user_A][0]:
            network[user_A][0].append(user_B)
        return network
    else:
        return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network:
        network[user] = [[],games]
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if user not in network:
        return None
    secCon = []
    for i in network[user][0]:
        for j in network[i][0]:
            if j not in secCon:
                secCon.append(j)
    return secCon

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    counter = 0
    for i in network[user_A][0]:
        if i in network[user_B][0]:
            counter += 1
    return counter

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

def path_to_friend(network, user_A, user_B, visitednodes=None, path=None):
    if user_A not in network or user_B not in network:
        return None
    if visitednodes==None:
        visitednodes = []
    if path == None:
        path = []
    if user_A == user_B:
        return [user_A]
    if user_B in network[user_A][0]:
        return path+[user_A,user_B]
    visitednodes.append(user_A)
    for i in network[user_A][0]:
        if i not in visitednodes:
            p = path_to_friend(network,i,user_B,visitednodes,path)
            if p:
                return [user_A]+p
    return None


# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!



# Test cases.
net = create_data_structure(example_input)
print net

# {'Freda': [['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']], 
#  'Ollie': [['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']], 
#  'Debra': [['Walter', 'Levi', 'Jennie', 'Robin'], ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']], 
#  'Olive': [['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']], 
#  'Levi': [['Ollie', 'John', 'Walter'], ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']], 
#  'Jennie': [['Levi', 'John', 'Freda', 'Robin'], ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']], 
#  'Mercedes': [['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']], 
#  'John': [['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']], 
#  'Robin': [['Ollie'], ['Call of Arms', 'Dwarves and Swords']], 
#  'Bryant': [['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 
#  'Walter': [['John', 'Levi', 'Bryant'], ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']]}

print 'Debra' not in net
# False

print net["Debra"][0]
# ['Walter', 'Levi', 'Jennie', 'Robin']

print path_to_friend(net, "John", "Ollie")
# ['John', 'Bryant', 'Ollie']

print get_connections(net, "Debra")
# ['Walter', 'Levi', 'Jennie', 'Robin']

print add_new_user(net, "Debra", [])
# {'Freda': [['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']], 
#  'Ollie': [['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']],
#  'Debra': [['Walter', 'Levi', 'Jennie', 'Robin'], ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']],
#  'Olive': [['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']],
#  'Levi': [['Ollie', 'John', 'Walter'], ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']],
#  'Jennie': [['Levi', 'John', 'Freda', 'Robin'], ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']],
#  'Mercedes': [['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']],
#  'John': [['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']],
#  'Robin': [['Ollie'], ['Call of Arms', 'Dwarves and Swords']],
#  'Bryant': [['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']],
#  'Walter': [['John', 'Levi', 'Bryant'], ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']]}

print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])
# {'Freda': [['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']],
#  'Nick': [[], ['Seven Schemers', 'The Movie: The Game']],
#  'Ollie': [['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']],
#  'Debra': [['Walter', 'Levi', 'Jennie', 'Robin'], ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']],
#  'Olive': [['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']],
#  'Levi': [['Ollie', 'John', 'Walter'], ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']],
#  'Jennie': [['Levi', 'John', 'Freda', 'Robin'], ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']],
#  'Mercedes': [['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']],
#  'John': [['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']],
#  'Robin': [['Ollie'], ['Call of Arms', 'Dwarves and Swords']],
#  'Bryant': [['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']],
#  'Walter': [['John', 'Levi', 'Bryant'], ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']]}

print get_connections(net, "Mercedes")
# ['Walter', 'Robin', 'Bryant']

print get_games_liked(net, "John")
# ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']

print add_connection(net, "John", "Freda")
# {'Freda': [['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']],
# 'Nick': [[], ['Seven Schemers', 'The Movie: The Game']],
# 'Ollie': [['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']],
# 'Debra': [['Walter', 'Levi', 'Jennie', 'Robin'], ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']],
# 'Olive': [['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']],
# 'Levi': [['Ollie', 'John', 'Walter'], ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']],
# 'Jennie': [['Levi', 'John', 'Freda', 'Robin'], ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']],
# 'Mercedes': [['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']],
# 'John': [['Bryant', 'Debra', 'Walter', 'Freda'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']],
# 'Robin': [['Ollie'], ['Call of Arms', 'Dwarves and Swords']],
# 'Bryant': [['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 
# 'Walter': [['John', 'Levi', 'Bryant'], ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']]}

print get_secondary_connections(net, "Mercedes")
# ['John', 'Levi', 'Bryant', 'Ollie', 'Olive', 'Freda', 'Mercedes']

print connections_in_common(net, "Mercedes", "John")
# 2

network = create_data_structure('')
network = add_new_user(network,'Alice',[])
network = add_new_user(network,'Bob',[])
network = add_connection(network,'Alice','Bob')
print network
# {'Bob': [[], []],
#  'Alice': [['Bob'], []]}

print 'Alice' in network
# True

print network['Alice'][0]
#['Bob']

print get_connections(network,'Alice')
#['Bob']