"""
Name: Velja Smigic
File Name: student_gpa_app.py
Description: This app calculates time units and processes student GPAs 
             to determine Dean's List or Honor Roll eligibility.
"""

# --- PART 1: Student GPA App ---

def main():
    print("--- Student Qualification Processor ---")
    print("(Enter 'ZZZ' as the last name to quit)\n")

    while True:
        # Ask for and accept student's last name
        last_name = input("Enter student's last name: ")
        
        # Quit processing if last name is 'ZZZ'
        if last_name.upper() == 'ZZZ':
            print("Exiting program...")
            break
            
        # Ask for and accept first name
        first_name = input("Enter student's first name: ")
        
        # Ask for and accept GPA as a float
        try:
            gpa = float(input(f"Enter GPA for {first_name} {last_name}: "))
        except ValueError:
            print("Invalid input. Please enter a numerical value for GPA.")
            continue

        # Test for Dean's List (3.5 or greater)
        if gpa >= 3.5:
            print(f"*** {first_name} {last_name} has made the Dean's List! ***")
        
        # Test for Honor Roll (3.25 or greater)
        # Note: If a student is 3.5+, they technically meet both criteria.
        elif gpa >= 3.25:
            print(f"--- {first_name} {last_name} has made the Honor Roll. ---")
        
        else:
            print(f"{first_name} {last_name} does not qualify for honors this time.")
        
        print("-" * 30)

if __name__ == "__main__":
    main()