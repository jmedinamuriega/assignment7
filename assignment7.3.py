# 3. Interactive Help Desk Bot
# Objective:
# The aim of this assignment is to 
# create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands
# (e.g., "help", "issue", "contact support"). 
# If a command is found, print a response related to the command.

# Task 2: Issue Categorizer
# If the user's input contains the word "issue",
# further categorize the issue based on keywords such as "login", "performance", "error", 
# etc. Print out the category of the issue for the support team.

pred_words=["help", "issue", "contact support"]
problem=input("How can I help you today?")
problem=problem.lower()

for i in range(len(pred_words)):
    if pred_words[i] in problem:
        index=i       
print(f"I see that your need is related to: {pred_words[index]}, let me redirect you to the support team.")
    
    
if "issue" in problem:
    if "login" in problem:
        print("issue related to log in")
    elif "performance" in problem:
        print("issue releated to performance")
    elif "error" in problem:
        print("issue releated to an error")
    else:
        print("issue not categorized")