print("This program is an implementation of the Rosenberg")
print("Self-Esteem Scale. This program will show you ten")
print("statements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the")
print("statements by responding with one of these four letters:")

print("D means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.")

print("1. I feel that I am a person of worth, at least on an equal plane with others.")
q_1 = input("Enter D, d, a, or A: ")
print("2. I feel that I have a number of good qualities.")
q_2 = input("Enter D, d, a, or A: ")
print("3. All in all, I am inclined to feel that I am a failure.")
q_3 = input("Enter D, d, a, or A: ")
print("4. I am able to do things as well as most other people.")
q_4 = input("Enter D, d, a, or A: ")
print("5. I feel I do not have much to be proud of.")
q_5 = input("Enter D, d, a, or A: ")
print("6. I take a positive attitude toward myself.")
q_6 = input("Enter D, d, a, or A: ")
print("7. On the whole, I am satisfied with myself.")
q_7 = input("Enter D, d, a, or A: ")
print("8. I wish I could have more respect for myself.")
q_8 = input("Enter D, d, a, or A: ")
print("9. I certainly feel useless at times.")
q_9 = input("Enter D, d, a, or A: ")
print("10. At times I think I am no good at all.")
q_10 = input("Enter D, d, a, or A: ")

def scoreing_q_1_to_7(score):
    match score:
        case "D":
            return 0
        case "d":
            return 1
        case "a":
            return 2
        case "A":
            return 3

def scoreing_q_8_to_10(score):
    match score:
        case "D":
            return 3
        case "d":
            return 2
        case "a":
            return 1
        case "A":
            return 0

q_1

print("Your score is 21.")
print("A score below 15 may indicate problematic low self-esteem.")
