import requests

endpoint = 'https://canvas.ucsc.edu/api/v1'
course_id = '73469'
headers = {
    'Content-Type': 'application/json',
    "Authorization": 'Bearer 9270~wX3W1YVBKcqcIeiOrF6BuZm5cPmktAWNHMmm6ohj7kKoVOHMQgoTmpZ4djtyTi1d'
}

# Get the list of assignments for the course
assignments_url = f"{endpoint}/courses/{course_id}/assignments"
response = requests.get(assignments_url, headers=headers)
assignments = response.json()

test_student_id = '113511'
grades = {}

# Loop through assignments to get grades
for assignment in assignments:
    assignment_id = assignment['id']
    submission_url = f"{endpoint}/courses/{course_id}/assignments/{assignment_id}/submissions/{test_student_id}"
    response = requests.get(submission_url, headers=headers)
    submission = response.json()
    grades[assignment['name']] = submission.get('grade', 'Not graded')

# Print grades
for assignment_name, grade in grades.items():
    print(f"{assignment_name}: {grade}")

# Publish a grade of 1 for the assignment "PA1"
for assignment in assignments:
    if assignment['name'] == 'PA3: Cryptography':
        assignment_id = assignment['id']
        grade_data = {
            "submission": {
                "posted_grade": "999999"
            }
        }
        submission_url = f"{endpoint}/courses/{course_id}/assignments/{assignment_id}/submissions/{test_student_id}"
        response = requests.put(submission_url, headers=headers, json=grade_data)
        if response.status_code == 200:
            print("Grade published successfully.")
        else:
            print(f"Failed to publish grade. Status code: {response.status_code}, Response: {response.text}")
