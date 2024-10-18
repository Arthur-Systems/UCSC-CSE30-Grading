import argparse
import sys
import requests
import zyphraser


def get_students(course_id, headers):
	students = []
	users_url = f"{endpoint}/courses/{course_id}/users"
	while users_url:
		response = requests.get(users_url, headers=headers, params={"enrollment_type": "student", "per_page": 200})
		if response.status_code != 200:
			print(f"Failed to retrieve students. Status code: {response.status_code}, Response: {response.text}")
			sys.exit(1)
		students.extend(response.json())
		users_url = None
		if 'Link' in response.headers:
			links = response.headers['Link'].split(',')
			for link in links:
				if 'rel="next"' in link:
					users_url = link[link.find('<') + 1:link.find('>')]
	return students


def find_assignment(assignments, assignment_name):
	normalized_assignment_name = assignment_name.replace(" ", "").lower()
	for assignment in assignments:
		normalized_name = assignment['name'].replace(" ", "").lower()
		if normalized_name == normalized_assignment_name:
			return assignment
	return None


def get_assignments(course_id, headers):
	assignments = []
	assignments_url = f"{endpoint}/courses/{course_id}/assignments"
	while assignments_url:
		response = requests.get(assignments_url, headers=headers, params={"per_page": 40})
		if response.status_code != 200:
			print(f"Failed to retrieve assignments. Status code: {response.status_code}, Response: {response.text}")
			sys.exit(1)
		assignments.extend(response.json())
		assignments_url = None
		if 'Link' in response.headers:
			links = response.headers['Link'].split(',')
			for link in links:
				if 'rel="next"' in link:
					assignments_url = link[link.find('<') + 1:link.find('>')]
	return assignments


def post_comment(course_id, assignment_id, student_id, headers, comment):
	comment_url = f"{endpoint}/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}/comments"
	payload = {
		"SubmissionComment": {
			"comment": comment
		}
	}
	response = requests.put(comment_url, headers=headers, json=payload)
	if response.status_code != 200:
		print(
			f"Failed to post comment for student {student_id}. Status code: {response.status_code}, Response: {response.text}")


def get_comments(course_id, assignment_id, student_id, headers):
	comment_url = f"{endpoint}/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}/comments"
	response = requests.get(comment_url, headers=headers)
	if response.status_code != 200:
		print(
			f"Failed to retrieve comments for student {student_id}. Status code: {response.status_code}, Response: {response.text}")
		return None
	submission = response.json()
	print(submission)
	print(submission.get("SubmissionComment", []))
	return submission.get("submission_comments", [])


def get_submission(course_id, assignment_id, student_id, headers):
	submission_url = f"{endpoint}/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}"
	response = requests.get(submission_url, headers=headers)
	if response.status_code != 200:
		print(
			f"Failed to retrieve submission for student {student_id}. Status code: {response.status_code}, Response: {response.text}")
		return None
	return response.json()


def apply_late_penalty(course_id, assignment_id, student_id, headers, updated_grade):
	submission_url = f"{endpoint}/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}"
	payload = {
		"submission": {
			"posted_grade": updated_grade,
			"late_policy_status": ("missing" if updated_grade in [0, "0"] else "late"),
			"seconds_late_override": 0
		}
	}
	response = requests.put(submission_url, headers=headers, json=payload)
	if response.status_code != 200:
		print(
			f"Failed to update grade for student {student_id}. Status code: {response.status_code}, Response: {response.text}")


def get_grades(course_id, headers, assignment_name, csv_file):
	# Get the list of students
	students = get_students(course_id, headers)

	# Get the list of assignments
	assignments = get_assignments(course_id, headers)

	# Find the specified assignment
	assignment = find_assignment(assignments, assignment_name)
	if not assignment:
		print(f"Assignment '{assignment_name}' not found.")
		print("Available assignments:", [assign['name'] for assign in assignments])
		sys.exit(1)

	# Get grades from CSV using zyphraser
	grades = zyphraser.get_scores(csv_file, assignment_name)

	# Create a dictionary to map student names to grades from CSV
	student_grades = {(grade[1], grade[0]): grade[2] for grade in grades}

	# Check and update the grade for each student
	for student in students:
		first_name = student['sortable_name'].split(", ")[1]
		last_name = student['sortable_name'].split(", ")[0]
		csv_grade = float(student_grades.get((first_name, last_name))) if (first_name,
		                                                                   last_name) in student_grades else 0
		submission = get_submission(course_id, assignment['id'], student['id'], headers)
		if submission and 'grade' in submission:
			current_grade = float(submission['grade']) if submission['grade'] else 0

			if csv_grade > current_grade:
				grade_difference = csv_grade - current_grade
				penalty_adjusted_grade = current_grade + (grade_difference * 0.8)

				# Update the grade with the penalty applied only to the difference
				apply_late_penalty(course_id, assignment['id'], student['id'], headers, penalty_adjusted_grade)

				print(
					f"Updated grade for student {student['sortable_name']}: Current Grade: {current_grade}, New Grade: {csv_grade}, Adjusted Grade with Penalty: {penalty_adjusted_grade}"
				)
		else:
			print(f"No current grade found for student {student['sortable_name']}")


def main():
	parser = argparse.ArgumentParser(
		description='Apply late penalty and update grades for a specific assignment in Canvas')
	parser.add_argument('--access_token',
	                    default='9270~wX3W1YVBKcqcIeiOrF6BuZm5cPmktAWNHMmm6ohj7kKoVOHMQgoTmpZ4djtyTi1d',
	                    help='The Canvas API access token')
	parser.add_argument('assignment_name', help='Name of the assignment to update grades for')
	parser.add_argument('csv_file', help='Path to the CSV file with student grades')
	args = parser.parse_args()

	global endpoint
	endpoint = 'https://canvas.ucsc.edu/api/v1'
	course_id = '77593'  # Course ID for the course
	headers = {
		'Content-Type': 'application/json',
		"Authorization": f'Bearer {args.access_token}'
	}

	# Get and update grades
	get_grades(course_id, headers, args.assignment_name, args.csv_file)


if __name__ == '__main__':
	main()