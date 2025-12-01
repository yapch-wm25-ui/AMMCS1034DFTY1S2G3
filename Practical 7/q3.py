# Returns the highest and the second highest scores from a list of scores.
def get_top_two_scores(scores):
    scores.sort(reverse = True)
    return scores[:2]

# Returns the average of all scores contained in a list of scores.
def calculate_average(scores):
    return sum(scores)/len(scores)


# Returns the appropriate ordinal suffix for a given number.
def get_ordinal_suffix(number):
    if number >=11 and number <=13:
        return "th"
    else:
         match (number %10):
                    case 1:
                        return "st"
                    case 2:
                        return "nd"
                    case 3:
                        return "rd"
                    case _:
                        return "th"


def main():
    number = read_size()
    scores = read_scores(number)
    first,second = get_top_two_scores(scores)

    print("\n The Highest Score        :{:.0f}%".format(first))
    print("\n The Second Highest Score :{:.2f}%".format(second))
    print("\n The Average Scpre        :{:.2f}%".format(calculate_average(scores)))




def read_size():
    while True:
        number = input("Enter the number of students: ")
        if number.isdigit():
            number = int(number)
            if number >= 1 and number <=10**10:
                return number
            else:
                print("Error: Only Positive Integer is Allowed\n")
        else:
            print("Error: Only Integer is Allowed!\n")

def read_scores(loop):
    floats = []
    count = 0

    while True:
        number = input("Enter a score: ")
        try:
            number = float(number)
            if number >= 0 and number <= float("inf"):
                floats.append(number)
                count += 1
                if count == loop:
                    return floats
            else:
                print("Error: Only Positive Value or 0 is Allowed!\n")
        except ValueError:
            print("Error: Only Floating-point number is Allowed\n")

main()