print("Let's check your grades")
name=input("What's your name?")
grades= int(input("what were total marks in exams?"))

if grades>=90:
    print(f"Congrats {name}, You got an A!")
elif grades >= 80:
    print(f"Great job {name}, you got a B.")
elif grades>=70:
    print("You got a C.")
elif grades>=60:
    print("You got a D.")
else:
    print("Its an F, try again.")