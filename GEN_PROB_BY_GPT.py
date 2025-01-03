#This code will generate a random maths problem 
#this code can be simplified
import random

def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/' and num1 % num2 != 0:
        num1, num2 = num2, num1  # Swap if division is not a whole number
    problem = f"{num1} {operator} {num2}"
    answer = eval(problem)
    return problem, answer

def main():
    correct_answers = 0
    total_problems = 5  # You can change this to set the number of problems
    for _ in range(total_problems):
        problem, correct_answer = generate_problem()
        print(f"Problem: {problem}")
        user_answer = float(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")
    
    print(f"You got {correct_answers}/{total_problems} problems correct.")

if __name__ == "__main__":
    print("Welcome to the Math Quiz!\n")
    main()
