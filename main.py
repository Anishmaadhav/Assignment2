"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    per_month_cost = annual_cost / MONTHS_PER_YEAR
    return per_month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    per_day_cost = annual_cost / (CLASS_DAYS_PER_SEMESTER * 2)
    return per_day_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return ((cost_per_credit(annual_cost, credits)) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER


# ---- PROGRAM ----

def main():
    annual_cost = float(input("What is your cost of college for one year? "))
    credits = int(input("How many credits are you taking this semester? "))
    while True:
        print("THE COST OF COLLEGE:")
        print("1 Cost Per Semester")
        print("2 Cost Per Month")
        print("3 Cost Per Class Day")
        print("4 Cost Per Credit")
        print("5 Cost Per CS1430 Class")
        print("6 ")
        print("Q Quit")
        choice = input("Choose an option: ")
        if choice == "Q":
            print("Have a nice day!")
            break
        elif choice == "1":
            semester = cost_per_semester(annual_cost)
            print(f"One semester costs ${semester:,.2f}")
        elif choice == "2":
            month = cost_per_month(annual_cost)
            print(f"One month costs ${month:,.2f}")
        elif choice == "3":
            day = cost_per_day(annual_cost)
            print(f"One day costs ${day:,.2f}")
        elif choice == "4":
            cost_of_credit = cost_per_credit(annual_cost, credits)
            print(f"One credit costs ${cost_of_credit:,.2f}")
        elif choice == "5":
            CS1430_class = cost_per_class(annual_cost, credits)
            print(f"One CS1430 class costs {CS1430_class:,.2f}")
        else:
            print("Please pick only the choices listed!")


        
# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
