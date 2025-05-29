<<<<<<< HEAD
#DAY2
"""
Q1: Print all student names and their majors
Q2: Average score per course per student 
Q3: Find students who scored >90 in final of Python101 
Q4: Add new course AI101 for student S101
Q5: Print average for each course
"""
university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#1.)
for i in university_data:
    print("Name of the student is ",university_data[i]["name"],"and the major is",university_data[i]["major"])
"""
OUTPUT:
Name of the student is  Alice Johnson and the major is Computer Science
Name of the student is  Bob Smith and the major is Mathematics
Name of the student is  Clara Lopez and the major is Physics
"""
#2.)
for a, b in university_data.items():
    print("Student id is: ",a,"Studentname is ",b["name"])
    for c, d in b["courses"].items():
        average = sum(d.values()) / len(d)
        print("the course is ",c,"the average is ",average)
    print()
"""
OUTPUT:
Student id is:  S101 Studentname is  Alice Johnson
the course is  Python101 the average is  91.33333333333333
the course is  Math201 the average is  81.0

Student id is:  S102 Studentname is  Bob Smith
the course is  Math201 the average is  90.33333333333333
the course is  Stats101 the average is  83.0

Student id is:  S103 Studentname is  Clara Lopez
the course is  Physics101 the average is  78.33333333333333
the course is  Math201 the average is  70.0
"""
#3.)
l=[]
for std_id,std_info in university_data.items():
    if "Python101" in std_info["courses"]:
        if std_info["courses"]["Python101"]["final"] >90:
            l.append(std_info['name'])
print("The students who scored more than 90 in python 101 is ",l)
"""
OUTPUT:
The students who scored more than 90 in python 101 is  ['Alice Johnson']
"""
#4.)
university_data["S101"]["courses"].update({"AI101":{"midterm": 75, "final": 82, "project": 78}})
print(university_data['S101'])
#university_data["S101"]["courses"]["AI101"] = {"midterm": 90, "final": 92, "project": 95}
"""
OUTPUT:
{'name': 'Alice Johnson', 'major': 'Computer Science', 'courses': {'Python101': {'midterm': 88, 'final': 92, 'project': 94}, 'Math201': {'midterm': 78, 'final': 85, 'project': 80}, 'AI101': {'midterm': 75, 'final': 82, 'project': 78}}}
"""

#5.)
for std_id,std_info in university_data.items():
    print("Name of the student is ",std_info["name"])
    for course,course_data in std_info["courses"].items():
        average = sum(course_data.values()) / len(course_data)
        print("Average:",course, average)

    print()
"""
OUTPUT:
Name of the student is  Alice Johnson
Average: Python101 91.33333333333333
Average: Math201 81.0
Average: AI101 78.33333333333333

Name of the student is  Bob Smith
Average: Math201 90.33333333333333
Average: Stats101 83.0

Name of the student is  Clara Lopez
Average: Physics101 78.33333333333333
Average: Math201 70.0
=======
#DAY2
"""
Q1: Print all student names and their majors
Q2: Average score per course per student 
Q3: Find students who scored >90 in final of Python101 
Q4: Add new course AI101 for student S101
Q5: Print average for each course
"""
university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#1.)
for i in university_data:
    print("Name of the student is ",university_data[i]["name"],"and the major is",university_data[i]["major"])
"""
OUTPUT:
Name of the student is  Alice Johnson and the major is Computer Science
Name of the student is  Bob Smith and the major is Mathematics
Name of the student is  Clara Lopez and the major is Physics
"""
#2.)
for a, b in university_data.items():
    print("Student id is: ",a,"Studentname is ",b["name"])
    for c, d in b["courses"].items():
        average = sum(d.values()) / len(d)
        print("the course is ",c,"the average is ",average)
    print()
"""
OUTPUT:
Student id is:  S101 Studentname is  Alice Johnson
the course is  Python101 the average is  91.33333333333333
the course is  Math201 the average is  81.0

Student id is:  S102 Studentname is  Bob Smith
the course is  Math201 the average is  90.33333333333333
the course is  Stats101 the average is  83.0

Student id is:  S103 Studentname is  Clara Lopez
the course is  Physics101 the average is  78.33333333333333
the course is  Math201 the average is  70.0
"""
#3.)
l=[]
for std_id,std_info in university_data.items():
    if "Python101" in std_info["courses"]:
        if std_info["courses"]["Python101"]["final"] >90:
            l.append(std_info['name'])
print("The students who scored more than 90 in python 101 is ",l)
"""
OUTPUT:
The students who scored more than 90 in python 101 is  ['Alice Johnson']
"""
#4.)
university_data["S101"]["courses"].update({"AI101":{"midterm": 75, "final": 82, "project": 78}})
print(university_data['S101'])
#university_data["S101"]["courses"]["AI101"] = {"midterm": 90, "final": 92, "project": 95}
"""
OUTPUT:
{'name': 'Alice Johnson', 'major': 'Computer Science', 'courses': {'Python101': {'midterm': 88, 'final': 92, 'project': 94}, 'Math201': {'midterm': 78, 'final': 85, 'project': 80}, 'AI101': {'midterm': 75, 'final': 82, 'project': 78}}}
"""

#5.)
for std_id,std_info in university_data.items():
    print("Name of the student is ",std_info["name"])
    for course,course_data in std_info["courses"].items():
        average = sum(course_data.values()) / len(course_data)
        print("Average:",course, average)

    print()
"""
OUTPUT:
Name of the student is  Alice Johnson
Average: Python101 91.33333333333333
Average: Math201 81.0
Average: AI101 78.33333333333333

Name of the student is  Bob Smith
Average: Math201 90.33333333333333
Average: Stats101 83.0

Name of the student is  Clara Lopez
Average: Physics101 78.33333333333333
Average: Math201 70.0
>>>>>>> 0d551c5 (Initial commit)
"""