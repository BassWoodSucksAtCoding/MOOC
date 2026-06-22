# Write your solution here
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = json.loads(my_request.read())

    enabled_courses = []

    for course in courses:
        if course["enabled"]:
            enabled_courses.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
    
    return enabled_courses

def retrieve_course(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    course = json.loads(my_request.read())

    course_info = {}
    course_info["weeks"] = len(course)
    hours_total = 0
    exercise_total = 0
    student_list = []

    for key, values in course.items():
        hours_total += values["hour_total"]
        exercise_total += values["exercise_total"]
        student_list.append(values["students"])
    
    course_info["students"] = max(student_list)
    course_info["hours"] = hours_total
    course_info["hours_average"] = int(hours_total/max(student_list)) 
    course_info["exercises"] = exercise_total
    course_info["exercises_average"] = int(exercise_total/max(student_list)) 

    return course_info

    




