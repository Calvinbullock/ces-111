# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    """
    Put description here....
    """
    # TODO Uncoment ---- For production
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender: ")
    birthdate = input("Enter birtdate (yyyy-mm-dd): ")
    height_inch = input("Enter your height(inchs): ")
    weight_lb = input("Enter your weight(lb): ")

    # changes height and weight to floats and age to capital
    gender.upper()
    height_inch = float(height_inch)
    weight_lb = float(weight_lb)

    # # Auto test cases 
    # gender = "F"
    # birthdate = "2001-03-21"
    # weight_lb = 125.0
    # height_inch = 54.0

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthdate)
    weight_kg = kg_from_lb(weight_lb)
    height_cm = cm_from_in(height_inch)
    b_m_i = body_mass_index(weight_kg, height_cm)
    b_m_r = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    # Print the results for the user to see.
    out_put = f"Age (years): {age}\nWeight (kg): {weight_kg}\nHeight (cm): {height_cm}\nBody mass index: {b_m_i}\nBasal metabolic rate (kcal/day): {b_m_r}"
    print(out_put)


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or (
        birthdate.month == today.month and birthdate.day > today.day
    ):
        years -= 1

    return years

def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return round(pounds * 0.45359237, 2)


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return inches * 2.54


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return round(10000 * weight / (height ** 2), 2)


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "F":
        return round(447.593 + 9.247 * weight + 3.098 * height - 4.330 * age, 2)

    elif gender == "M":
        return round(88.362 + 13.397 * weight + 4.799 * height - 5.677 * age, 2)


# Call the main function so that
# this program will start executing.
main()
