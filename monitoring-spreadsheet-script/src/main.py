import requests
import json
from spreadsheet import SpreadSheet

CREDENTIALS_PATH='./auth/credentials.json'
TOKEN_PATH='./auth/token.json'
BASE_URL='http://localhost:3333/api/'

def main():
    try:
        response = requests.get(f'{BASE_URL}courses').text
        courses = json.loads(response)
    except:
        print('Could not establish connection to api')
        exit(1)

    print('Which course do you wanna save? ')
    for i, course in enumerate(courses):
        print(f'{i} - {course["title"]}')

    choice = int(input('> '))
    spreadsheet_id = str(input('Enter the id of your spreadsheet: '))
    chosen_course_id = courses[choice]['id']
    print('getting course works...')

    try:
        response = requests.get(f'{BASE_URL}course-works/{chosen_course_id}').text
        course_works = json.loads(response)
    except:
        print('Could not get course works')
        exit(1)

    print('getting all students...')
    
    try:
        response = requests.get(f'{BASE_URL}students/{chosen_course_id}').text
        all_students = json.loads(response)
    except:
        print('Could not get students')
        exit(1)

    try:
        spreadsheet = SpreadSheet(CREDENTIALS_PATH, TOKEN_PATH, spreadsheet_id)
        spreadsheet.authorize()
        print('saving course works into your spreadsheet...')
        spreadsheet.save_course_works(course_works, all_students)
        spreadsheet.list_all_students(all_students, course_works)
        print('all done!')
    except:
        print('Could not fill spreadsheet')
        exit(1)

if __name__ == '__main__':
    main()
