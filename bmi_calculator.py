# bmi_calculator.py
# BMI Calculator with retry functionality for AICTE Oasis Infobyte Internship
# Author: Aditya Mishra
# Date: January 2026

def calculate_bmi(wt, ht):
    """Calculate BMI using formula: BMI = weight / (height^2)"""
    return wt / (ht ** 2)


def get_bmi_category(bmi):
    """Categorize BMI into health categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    """Main function to run BMI calculator"""
    print("=" * 50)
    print("BMI Calculator")
    print("=" * 50)
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
        
        # Display BMI reference
        print("\nBMI Categories Reference:")
        print("  Underweight: BMI < 18.5")
        print("  Normal weight: 18.5 <= BMI < 24.9")
        print("  Overweight: 25 <= BMI < 29.9")
        print("  Obesity: BMI >= 30")

    except ValueError:
        print("Error: Please enter valid numeric data")


def run_calculator():
    """Run calculator with retry loop"""
    while True:
        main()
        if input("\nDo you want to calculate again? (yes/no): ").strip().lower() != 'yes':
            print("Thank you for using BMI Calculator!")
            break


if __name__ == "__main__":
    run_calculator()
