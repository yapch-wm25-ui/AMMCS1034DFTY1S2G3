numbers = []

while True:
    number= input("Enter an integer or the 'Q'/'q' to exit: ")

    if number == "Q" or number == "q":
        break
    try:
        numbers.append(int(number))
    except ValueError:
        print("Only integer is allowed!\n")

    if len(numbers):
        numbers = numbers[::-1]

        print("\n Integers in reversed order:",end=" ")
        for num in numbers:
            print(num,end=" ")
    else:
        print("No Integers.")