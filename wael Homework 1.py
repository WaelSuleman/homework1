# Question 1
# A


import csv
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
D1 = dict(zip(L1, L2))
print(D1)

# B


def factorial(n):
    """Calculates the factorial of a given number.

    Args:
      n: The number to calculate the factorial of.

    Returns:
      The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Get user input
num = int(input("Enter a number: "))

# Calculate the factorial
fact = factorial(num)

# Print the result
print(f"The factorial of {num} is {fact}")

# C
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
L2 = []
for i in range(len(L)):
    if L[i].startswith('B'):
        L2.append(L[i])

print(L2)

# D
d = {i: i+1 for i in range(1, 11)}
print(d)

# Question 2
binary = input("Enter a binary number: ")
decimal = 0

for digit in binary:
    decimal = decimal*2 + int(digit)

print("The decimal equivalent of", binary, "is", decimal)


# ََQuestion 3


def read_questions(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        questions = list(reader)
    return questions


def ask_questions(questions):
    score = 0
    for question in questions:
        print(question[0])
        answer = input().strip().lower()
        if answer == question[1].strip().lower():
            score += 1
    return score


def save_result(name, score):
    with open('results.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, score])


filename = input("Enter the filename of the quiz questions: ")
questions = read_questions(filename)

name = input("Enter your name: ")
score = ask_questions(questions)

print("Your score is:", score)
save_result(name, score)
