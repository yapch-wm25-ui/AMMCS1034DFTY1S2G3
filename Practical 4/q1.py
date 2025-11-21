score = float(input("Enter a score: "))

grade = ""

if score >=90 and score <= 100:
    grade = "A"
elif score >=80 and score <= 90:
    grade = "B"
elif score >=70 and score <= 80:
    grade = "C"
elif score >=60 and score <= 70:
    grade = "D"
elif score >=0 and score <= 60:
    grade = "F"
else:
    grade =""

    match grade:
        case "A" | "F":
            print("You got an", grade,  "for the test.")
        case "B" | "C"| "D":
            print("You got an", grade,  "for the test.")
        case _:
            print("You have entered a wrong input")


