# Write your solution here
def print_student(student_dict,student_name):
    if student_name in student_dict:
        print(f"{student_name}: ")
        if student_dict[student_name] == {}:
            print(" no completed courses")
        else:
            print(f" {student_dict[student_name]["Course No"]} completed courses:")
            
            for key,value in student_dict[student_name].items():
                if key != "Average" and key != "Course No":
                    print(f"  {key} {value}")
            
            print(f" average grade {student_dict[student_name]["Average"]}")
    else:
        print(f"{student_name}: no such person in the database")

def add_student(student_dict,student_name):
    student_dict[student_name] = {}

def add_course(student_dict,student_name,course_tuple):
    if student_name in student_dict and course_tuple[1] != 0:
        if student_dict[student_name] == {}:
            student_dict[student_name]["Average"] = 0
            student_dict[student_name]["Course No"] = 0
        

        if course_tuple[0] not in student_dict[student_name]:
            total = 0
            total = student_dict[student_name]["Average"] * student_dict[student_name]["Course No"]
            total += course_tuple[1]
            student_dict[student_name]["Course No"] += 1
            student_dict[student_name]["Average"] = total/student_dict[student_name]["Course No"]

            student_dict[student_name][f"{course_tuple[0]}"] = course_tuple[1]
        
        if course_tuple[0] in student_dict[student_name] and course_tuple[1] > student_dict[student_name][f"{course_tuple[0]}"]:

            total = 0
            total = student_dict[student_name]["Average"] * student_dict[student_name]["Course No"]
            total += course_tuple[1]
            total -= student_dict[student_name][f"{course_tuple[0]}"]
            student_dict[student_name]["Average"] = total/student_dict[student_name]["Course No"]

            student_dict[student_name][f"{course_tuple[0]}"] = course_tuple[1]

            
            
def summary(student_dict):
    print(f"students {len(student_dict)}")

    course_no_dict_local = {}
    average_no_dict_local = {}

    for key, value in student_dict.items():
        course_no_dict_local[key] = value["Course No"]
        average_no_dict_local[key] = value["Average"]

    most_course = max(course_no_dict_local, key=course_no_dict_local.get)
    print(f"most courses completed {course_no_dict_local[most_course]} {most_course}")

    best_average = max(average_no_dict_local, key=average_no_dict_local.get)
    print(f"best average grade {average_no_dict_local[best_average]} {best_average}")
            
        
        
            
            

        
        
            
        


if __name__ == "__main__":
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")

    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")

    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    # add_course(students, "Peter", ("Introduction to Programming", 4))
    # print_student(students, "Peter")

    students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    # add_course(students, "Peter", ("Introduction to Programming", 1))
    # add_course(students, "Peter", ("Advanced Course in Programming", 1))
    # add_course(students, "Eliza", ("Introduction to Programming", 5))
    # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)
    #print(len(students))

    add_student(students, "Peter")
    add_student(students, "Emily")
    print_student(students, "Peter")
    print_student(students, "Emily")
    print_student(students, "Andy")
