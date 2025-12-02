from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
myapp = Flask(__name__)

# Define the grading system for Australia
SYSTEM_AUS = {
    "HD": 4.00,
    "D": 3.00,
    "C": 2.00,
    "P": 1.00,
    "Fail": 0.00
} 

# Define the grading system for Malaysia
SYSTEM_MY = {
    "HD": 4.00,
    "D": 3.67,
    "C": 3.00,
    "P": 2.33,
    "Fail": 0.00,
    "F": 0.00 # Also include "F" for fail
}

# Function to get the grade point based on the grading system
def get_grade_point(grade, system_type):
    # Remove any leading/trailing whitespace from the grade
    grade = grade.strip()
    # Select the appropriate grading system
    mapping = SYSTEM_AUS if system_type == 'AUS' else SYSTEM_MY
    # Return the grade point, default to 0.00 if grade is not found
    return mapping.get(grade, 0.00)

# Route for the index page
@myapp.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Route for calculating GPA and CGPA, accepts POST requests
@myapp.route('/calculate', methods=['POST'])
def calculate():
    # Get the JSON data from the request
    data = request.get_json()
    # Extract the grading system type, default to 'AUS' if not provided
    system_type = data.get('system', 'AUS')
    # Extract the semesters data
    semesters_data = data.get('semesters', [])

    # Initialize total grade points and credits
    total_grade_points = 0
    total_credits = 0
    
    # List to store results for each semester
    results = []

    # Iterate through each semester
    for i, sem in enumerate(semesters_data):
        sem_grade_points = 0
        sem_credits = 0
        
        processed_subjects = []

        # Iterate through each subject in the semester
        for sub in sem['subjects']:
            try:
                # Get subject details, using .get() to avoid KeyError
                code = sub.get('code')
                name = sub.get('name')
                grade = sub.get('grade')
                credits_str = sub.get('credits')

                # Check if any required data is missing
                if not all([code, name, grade, credits_str is not None]):
                    # Print a warning message if data is missing
                    print(f"Warning: Skipping subject in semester {i+1} due to missing data: {sub}")
                    # Skip to the next subject
                    continue

                # Convert credits to float
                credit = float(credits_str)

                # Get the grade point for the subject
                point = get_grade_point(grade, system_type)
                
                # Calculate the subject's total grade points
                sub_total_gp = point * credit
                
                # Add to the semester's total grade points and credits
                sem_grade_points += sub_total_gp
                sem_credits += credit
                
                # Store the processed subject data
                processed_subjects.append({
                    'code': code, 'name': name,
                    'grade': grade,
                    'credits': credit,
                    'point': point
                })
            except ValueError:
                print(f"Warning: Skipping subject in semester {i+1} due to invalid credits value '{sub.get('credits')}' for subject {sub.get('code')}.")
                continue
            except Exception as e:
                print(f"An unexpected error occurred while processing subject {sub.get('code')} in semester {i+1}: {e}")
                continue

        # Calculate the GPA for the semester
        gpa = 0.00
        if sem_credits > 0:
            gpa = sem_grade_points / sem_credits

        # Add the semester's grade points and credits to the total
        total_grade_points += sem_grade_points
        total_credits += sem_credits

        # Append the semester's results to the list
        results.append({
            'semester_index': i + 1,
            'subjects': processed_subjects,
            'gpa': round(gpa, 2),
            'total_credits': sem_credits
        })
    
    # Calculate the CGPA
    cgpa = 0.00
    if total_credits > 0:
        #CGPA is total grade points divided by total credits
        cgpa = total_grade_points / total_credits

    # Render the results template with the calculated data
    return render_template('result.html', 
                           results=results,
                           cgpa=round(cgpa, 2), 
                           system=system_type)

# Run the application if this file is executed
if __name__ == '__main__':
    # Start the Flask development server
    myapp.run(debug=True, host='0.0.0.0')