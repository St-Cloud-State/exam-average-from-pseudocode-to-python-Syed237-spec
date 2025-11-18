"""
Full Name: Muhammad Mehdi
Class-Section: Fa25 IS 250-01
Assignment Title: Calculate Average of Three Scores
Submission Date: 17/11/2025
"""

"""
Write your pseudocode here.
Do not write any Python code in this section.
Your pseudocode should describe your overall approach in your own words.

1. Prompt the user to enter three exam scores.
2. Store these scores in variables.
3. Create a function to calculate the average of the three scores.
4. Print each individual score on separate lines.
5. Print the calculated average score on a new line.
"""

# Your Python code begins below this line.
# Importing the necessary library to get user input
def calculate_average(score1, score2, score3):
    # Calculate the sum of the scores
    total = score1 + score2 + score3
    # Compute the average by dividing the sum by 3
    average = total / 3
    # Return the average score
    return average

# Prompt the user to enter the first score and store it as a float
score1 = float(input("Enter first score: "))
# Prompt the user to enter the second score and store it as a float
score2 = float(input("Enter second score: "))
# Prompt the user to enter the third score and store it as a float
score3 = float(input("Enter third score: "))

# Print the first score entered by the user
print(f"First score: {score1}")
# Print the second score entered by the user
print(f"Second score: {score2}")
# Print the third score entered by the user
print(f"Third score: {score3}")

# Call the function to calculate the average of the three scores
average_score = calculate_average(score1, score2, score3)

# Print the average score on a new line
print(f"The average score is: {average_score}")

  
