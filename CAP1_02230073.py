################################
# Samten Thinlay
# 1. Electrical
# 02230073
################################
# REFERENCES
# @DQ-Logo
# @Blackbox.ai
################################
# SOLUTION
# Your Solution Score:49483
# CSF101-CAP/input_3_cap1.txt
################################# 
# Reading the input.txt file
def read_input(input_3_cap1): # We define a fucntion "read_input"
    x = [] # We simply create an empty list
    with open('input_3_cap1.txt', 'r') as files: # For each line in the file
        for y in files: # Split the lines into two parts using whitespace as the delimiter
            my_choice, end_result = y.split() # Create a tuple containing the two parts and append it to the above list
            x.append((my_choice, end_result)) # Create a tuple containing the values of 'my_choice' and 'end_result', and append it to the list
    return x # Return the list containing 'my_choice' and 'end_result'

# Calculating the point for each game/round
def calculate_score(Total_Matches_Competed): # Calculate a score based on "Total_Matches_Competed"
    Point = 0 # The starting point for each round is 0
    for my_choice, end_result in Total_Matches_Competed: # Iterate through each game in "Total_Matches_Competed" 
    # and reveal the values of 'my_choice' and 'end_result'
        score = {'A' : 1, 'B': 2, "C": 3}
        RESULT = {"X":0,"Y" :3, "Z" :6}
        if end_result == 'X':  # we will loose
            if my_choice == 'C': # my choice is scissor to loose the game 
                Point += 3 #  sum of my choice score and result value of x
            elif my_choice == 'A': # my choice is rock to loose the game
                Point += 1  # sum of my choice score and result value of x
            elif my_choice == 'B': # my choice is paper to loose the game
                Point += 2 #  sum of my choice score and result value of x

        elif end_result == 'Y':  # the game will be draw
            if my_choice == 'A': # my choice is rock to draw the game
                Point += 4  # sum of my choice score and result value of y
            elif my_choice == 'B': # my choice is paper to draw the game
                Point += 5  # sum of my choice score and result value of y
            elif my_choice == 'C': # my choice is scissor to draw the game
                Point += 6  # sum of my choice score and result value of y

        elif end_result == 'Z':  # We will WIN the game 
            if my_choice == 'B': # my choice is paper to win the game
                Point += 8  # sum of my choice score and result value of z
            elif my_choice == 'C': # my choice is scissor to win the game
                Point+= 9 # sum of my choice score and result value of z
            elif my_choice == 'A': # my choice is rock to win the game
                Point += 7 # sum of my choice score and result value of z
    print(f"The Total result of the given input is:{Point}") #Printing out the total result of the points from the input file

# Running the program
type_file_name = "input_3_cap1.txt"  # the given input from the assignment 
calculate_score(read_input(type_file_name)) # Calculate the score using the data obtained from reading the input file