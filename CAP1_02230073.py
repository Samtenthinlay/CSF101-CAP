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
    with open('input_3_cap1.txt', 'r') as files: # For each line in the file
        for y in files: # Split the lines into two parts using whitespace as the delimiter
            contrast_picked, end_result = y.split() # Create a tuple containing the two parts and append it to the above list
            x.append((contrast_picked, end_result)) # Create a tuple containing the values of 'my_choice' and 'end_result', and append it to the list
    return x # Return the list containing 'my_choice' and 'end_result'

# Calculating the point for each game/round
def calculate_score(Total_Matches_Competed): # Calculate a score based on "Total_Matches_Competed"
    Point = 0 # The starting point for each round is 0
    for contrast_picked, end_result in Total_Matches_Competed: # Iterate through each game in "Total_Matches_Competed" 
   
        score = {'A' : 1, 'B': 2, "C": 3}
        RESULT = {"X":0,"Y" :3, "Z" :6}

        # and reveal the values of 'contrast_picked(opponents choice)' and 'end_result'
        if end_result == 'X':  # We must be DEFEATED
            if contrast_picked == 'A': # Contrast chose Rock
                Point += 3 #  Rock previals over scissors
            elif contrast_picked == 'B': # Contrast chose Paper
                Point += 1  # Paper previals over rock 
            elif contrast_picked == 'C': # Contrast chose Scissors
                Point += 2 #  Scissors previals over paper
        elif end_result == 'Y':  # We need to produce a DRAW
            if contrast_picked == 'A': # He/She chose Rock
                Point += 4  # Rock results in a tie against Rock
            elif contrast_picked == 'B': # He/She chose Paper
                Point += 5  # Paper results in a tie against Paper
            elif contrast_picked == 'C': # He/She chose Scissors
                Point += 6  # Scissors results in a tie against  Scissors
        elif end_result == 'Z':  # We need to WIN
            if contrast_picked == 'A': # He/She chose Rock
                Point += 8  # Paper triumphs over Rock
            elif contrast_picked == 'B': # He/She chose Paper
                Point+= 9 # Scissors triumphs over Paper
            elif contrast_picked == 'C': # He/She chose Scissors
                Point += 7 # Rock triumphs over Scissor

    print(f"The Total result of the given input is:{Point}") #Printing out the total result of the points from the input file

# Running the program
type_file_name = "input_3_cap1.txt"  # the given input from the assignment 
calculate_score(read_input(type_file_name)) # Calculate the score using the data obtained from reading the input file