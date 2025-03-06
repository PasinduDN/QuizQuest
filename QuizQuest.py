questions = [
    {
        'prompt': 'Which of the following is the correct extension of the Python file?',
        'options': ['1) .python', '2) .py', '3) .pl', '4) .p'],
        'answer': 2 
    },
    {
        'prompt': 'What is the output of `print(2 ** 3)` in Python?',
        'options': ['1) 6', '2) 8', '3) 9', '4) 23'],
        'answer': 2 
    },
    {
        'prompt': 'Which of the following is used to define a block of code in Python?',
        'options': ['1) Curly braces `{}`', '2) Indentation', '3) Square brackets `[]`', '4) Parentheses `()`'],
        'answer': 2  
    },
    {
        'prompt': 'What does the `len()` function do in Python?',
        'options': ['1) Returns the type of an object', '2) Returns the length of an object', '3) Converts a string to lowercase', '4) Sorts a list'],
        'answer': 2 
    },
    {
        'prompt': 'Which of the following is NOT a Python data type?',
        'options': ['1) int', '2) float', '3) char', '4) str'],
        'answer': 3  
    },
    {
        'prompt': 'What is the result of `3 + 5 * 2` in Python?',
        'options': ['1) 16', '2) 13', '3) 10', '4) 8'],
        'answer': 2  
    },
    {
        'prompt': 'Which keyword is used to define a function in Python?',
        'options': ['1) func', '2) define', '3) def', '4) function'],
        'answer': 3 
    },
    {
        'prompt': 'What does the `range(5)` function return?',
        'options': ['1) A list of numbers from 0 to 5', '2) A list of numbers from 1 to 5', '3) A sequence of numbers from 0 to 4', '4) A sequence of numbers from 1 to 4'],
        'answer': 3 
    },
    {
        'prompt': 'Which of the following is used to comment a single line in Python?',
        'options': ['1) //', '2) #', '3) /* */', '4) <!-- -->'],
        'answer': 2  
    },
    {
        'prompt': 'What is the output of `print(type(3.14))` in Python?',
        'options': ['1) int', '2) float', '3) str', '4) bool'],
        'answer': 2 
    }
]

def runQuiz(questions):

    score = 0

    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        while True:
            try:
                answer = int(input("Enter your answer [1, 2, 3 or 4] : "))
                if (answer==1 or answer==2 or answer==3 or answer==4):
                    if(answer == question['answer']):
                        score += 10
                        print("Correct, hooray..!")
                        print(f"This is your total marks ({score}/100)\n")
                        break
                    else:
                        print(f"Wrong.. The correct answer is : {question['answer']}")
                        print(f"This is your total marks ({score}/100)\n")
                        break
                else:
                    print(f"'{answer}' is Invalid input... Please enter a valid number.")
            except ValueError:
                  print(f"'{answer}' is Invalid input... Please enter a valid number.")

runQuiz(questions)