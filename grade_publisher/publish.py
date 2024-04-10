import requests

endpoint = 'https://canvas.ucsc.edu/api/v1/'
course_id = '73469'
headers = {'Content-Type': 'application/json', "Authorization": 'Bearer 9270~wX3W1YVBKcqcIeiOrF6BuZm5cPmktAWNHMmm6ohj7kKoVOHMQgoTmpZ4djtyTi1d'}

def get_student_data():
	response = requests.get(f'{endpoint}/courses/{course_id}/students', headers=headers)
	return response.json()

if __name__ == "__main__":
	grade = 10
	student_data = get_student_data()
	print(student_data)



