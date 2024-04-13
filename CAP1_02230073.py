################################
# Samten Thinlay
# 1. Electrical
# 02230073
################################
# REFERENCES
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://github.com/kying18/rock-paper-scissors
# https://youtu.be/Qcefu1jVPds?si=bw3T3BUpaVHk7Cq5
# https://youtu.be/Stx952qn9co?si=CRLFVzngpS9iKXu5
# https://youtu.be/zfdfJMw9n1g?si=kQEZdStI56aRLiLM
################################
# SOLUTION
# Your Solution Score: 49483
# CSF101-CAP/input_3_cap1.txt
################################# 
# Reading the input.txt file
def read_input(input_3_cap1): # We define a fucntion "read_input"
    x = [] # We simply create an empty list
    with open('input_3_cap1.txt', 'r') as document: # For every line in the document
        for y in document: # Using whitespace as the delimiter, divide the lines into two halves
            contrast_picked, end_result = y.split() # To the list above, create a tuple with the two components and append it
            x.append((contrast_picked, end_result)) # The values of "my_choice" and "end_result" should be created as a tuple, then added to the list
    return x # Return the list that includes "end_result" and "my_choice."

# Obtaining the points for every round or game
def calculate_score(Total_Matches_Competed): # Determine a score by utilizing the "Total_Matches_Competed" data
    Point = 0 # For every round, the initial value is 0
    for contrast_picked, end_result in Total_Matches_Competed: # Go over every match in "Total_Matches_Competed" one after the other
   
        score = {'A' : 1, 'B': 2, "C": 3}
        RESULT = {"X":0,"Y" :3, "Z" :6}

        # and expose the values contained in "contrast_picked(opponents choice)" as well as "end_result."
        if end_result == 'X':  # We have to be DEFEATED
            if contrast_picked == 'A': # Contrast chose Rock
                Point += 3 #  Rock previals over scissors
            elif contrast_picked == 'B': # Contrast chose Paper
                Point += 1  # Paper previals over rock 
            elif contrast_picked == 'C': # Contrast chose Scissors
                Point += 2 #  Scissors previals over paper
        elif end_result == 'Y':  # We have to create a DRAW
            if contrast_picked == 'A': # Rock was his/her choice
                Point += 4  # Rock results in a tie against Rock
            elif contrast_picked == 'B': # Paper  was his/her choice
                Point += 5  # Paper results in a tie against Paper
            elif contrast_picked == 'C': # Scissors  was his/her choice
                Point += 6  # Scissors results in a tie against  Scissors
        elif end_result == 'Z':  # We must PREVAIL
            if contrast_picked == 'A': # Rock  was his/her choice
                Point += 8  # Paper triumphs over Rock
            elif contrast_picked == 'B': # Paper  was his/her choice
                Point+= 9 # Scissors triumphs over Paper
            elif contrast_picked == 'C': # Scissors  was his/her choice
                Point += 7 # Rock triumphs over Scissor

    print(f"The Total result of the given input is:{Point}") # Outputting the entire score obtained from the input file

# Executing the program
type_file_name = "input_3_cap1.txt"  # The data provided by the assignment 
calculate_score(read_input(type_file_name)) # Determine the score by utilizing the information gleaned from reading the input file