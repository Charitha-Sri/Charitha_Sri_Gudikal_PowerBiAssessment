#DAY6
class Dept:
    dept_count=0
    def __init__(self,id,name,loc,hod):
        self.id=id
        self.name=name
        self.loc=loc
        self.hod=hod
        Dept.dept_count+=1

    def display(self):
        print(f"Dept ID: {self.id}")
        print(f"Dept Name: {self.name}")
        print(f"Dept Location: {self.loc}")
        print(f"Dept HOD: {self.hod}")
   
    @classmethod
    def dept_cou(cls):
        print(f"The total Number of students in Department are {cls.dept_count}")

Department=[]
#Giving the user input
n=int(input("Enter the Number of Departments: "))
for i in range(n):
    print(f"\nEnter details for department {i + 1}:")
    id=int(input("Enter the ID: "))
    name=input("Enter the name: ")
    loc=input("Enter the Location: ")
    hod=input("Enter the HOD: ")
    dept = Dept(id, name, loc, hod)
    Department.append(dept)
#Printing the department 
print("\n--- Department Details ---")
for dept in Department:
    dept.display()
#Printing the total number of departments
Dept.dept_cou()
print("Enter--\n")
option=int(input("Enter the choice \n 1.)Search with dept id \n 2.)Search with dept name \n"))
#searching the dept by dept id
if option==1:
    search_id = int(input("Enter Department ID to search: \n"))
    found = False
    for dept in Department:
        if dept.id==search_id:
            dept.display()
            found=True
            break
    if not found:
        print("Not Found by Dept ID")
#searching by dept name
if option ==2:
    search_name=input("Enter dept name to search: \n")
    found=False
    for deptn in Department:
        if deptn.name==search_name:
            deptn.display()
            found=True
            break
    if not found:
        print("Not Found by Dept name")

"""
OUTPUT:
Enter the Number of Departments: 3

Enter details for department 1:
Enter the ID: 101
Enter the name: cse
Enter the Location: hyd
Enter the HOD: sam

Enter details for department 2:
Enter the ID: 102
Enter the name: it
Enter the Location: bang
Enter the HOD: curran

Enter details for department 3:
Enter the ID: 103
Enter the name: ece
Enter the Location: chen
Enter the HOD: tim

--- Department Details ---
Dept ID: 101
Dept Name: cse
Dept Location: hyd
Dept HOD: sam

Dept ID: 102
Dept Name: it
Dept Location: bang
Dept HOD: curran

Dept ID: 103
Dept Name: ece
Dept Location: chen
Dept HOD: tim

The total Number of students in Department are 3
Enter--

Enter the choice
 1.)Search with dept id
 2.)Search with dept name
 2
Enter dept name to search:
it
Dept ID: 102
Dept Name: it
Dept Location: bang
Dept HOD: curran
"""