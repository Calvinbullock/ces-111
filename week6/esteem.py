def scoreing_q_1_2_4_6_7(score):
    # Takes letter grade and changes it to number
    match score:
        case "D":
            return 0
        case "d":
            return 1
        case "a":
            return 2
        case "A":
            return 3


def scoreing_q_3_5_8_9_10(score):
    # Takes letter grade and changes it to number
    match score:
        case "D":
            return 3
        case "d":
            return 2
        case "a":
            return 1
        case "A":
            return 0


def main():
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")

    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")

    print(
        "1. I feel that I am a person of worth, at least on an equal plane with others."
    )

    # # TODO uncoment for production
    # q_1 = input("Enter D, d, a, or A: ")
    # print("2. I feel that I have a number of good qualities.")
    # q_2 = input("Enter D, d, a, or A: ")
    # print("3. All in all, I am inclined to feel that I am a failure.")
    # q_3 = input("Enter D, d, a, or A: ")
    # print("4. I am able to do things as well as most other people.")
    # q_4 = input("Enter D, d, a, or A: ")
    # print("5. I feel I do not have much to be proud of.")
    # q_5 = input("Enter D, d, a, or A: ")
    # print("6. I take a positive attitude toward myself.")
    # q_6 = input("Enter D, d, a, or A: ")
    # print("7. On the whole, I am satisfied with myself.")
    # q_7 = input("Enter D, d, a, or A: ")
    # print("8. I wish I could have more respect for myself.")
    # q_8 = input("Enter D, d, a, or A: ")
    # print("9. I certainly feel useless at times.")
    # q_9 = input("Enter D, d, a, or A: ")
    # print("10. At times I think I am no good at all.")
    # q_10 = input("Enter D, d, a, or A: ")

    # Test cases answer total_anser == 21
    q_1 = "A"
    q_2 = "A"
    q_3 = "D"
    q_4 = "a"
    q_5 = "d"
    q_6 = "a"
    q_7 = "a"
    q_8 = "a"
    q_9 = "a"
    q_10 = "d"

    total_score = (
        scoreing_q_1_2_4_6_7(q_1)
        + scoreing_q_1_2_4_6_7(q_2)
        + scoreing_q_3_5_8_9_10(q_3)
        + scoreing_q_1_2_4_6_7(q_4)
        + scoreing_q_3_5_8_9_10(q_5)
        + scoreing_q_1_2_4_6_7(q_6)
        + scoreing_q_1_2_4_6_7(q_7)
        + scoreing_q_3_5_8_9_10(q_8)
        + scoreing_q_3_5_8_9_10(q_9)
        + scoreing_q_3_5_8_9_10(q_10)
    )

    print(f"Your score is {total_score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


main()
