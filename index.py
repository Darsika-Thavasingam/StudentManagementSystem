#student management system


#class
class Student:
    total_students = 0 #class variable

    #constractor
    def __init__(self,name,age,grade):
        self.__id = Student.total_students + 1 #private variable 
        self.name = name
        self.age = age
        self.grade = grade
        Student.total_students += 1
    
    #display student info

    def display_info(self):
        print("Student ID:", self.__id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

    def get_id(self): #using getter method to access private variable
        return self.__id
    

    @classmethod
    def show_total_students(cls):#class method for class variable
        print("Total Students:", cls.total_students)
    

    @staticmethod
    def welcome():#static method
        print("Welcome to the Student Management System")

class GraduateStudent(Student):
    def __init__(self, name, age, grade, thesis):
        super().__init__(name, age, grade)
        self.thesis = thesis

    def display_info(self):
        super().display_info()
        print("Thesis:", self.thesis)


    #list to store students
students = []
FILENAME = "students.txt"

def add_student():#add student details
    try:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade(0-100): "))
        if 0 <= grade <= 100:
            s = Student(name, age, grade)
            students.append(s)
            print("Student added successfully!")
        else:
            print("Grade must be between 0 and 100.")   
    except ValueError:
        print("Invalid input. Please enter  numbers for age and grades.")


def add_graduate_student():#add graduate student details
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = float(input("Enter grade(0-100): "))
        thesis = input("Enter thesis title: ")
        g = GraduateStudent(name, age, grade, thesis)
        students.append(g)
        print("Graduate student added successfully!")
    except ValueError:
        print("Invalid input.")


#view student details
def view_students():
    if not students:
        print("No students available.")
    else:
        for s in students:
            s.display_info()
            print("-" * 30)


#search student by id
def search_student():
    try:
        sid = int(input("Enter student ID to search: "))
        Found = False
        for s in students:
            if s.get_id() == sid:
                s.display_info()
                Found = True
                break
        if not Found:
            print("Student not found.")
    except ValueError:
        print("Invalid input!")

#save students to file
def save_to_file():
    with open(FILENAME, "w") as f: 
        for s in students:
            if isinstance(s, GraduateStudent):
                f.write(f"{s.get_id()},{s.name},{s.age},{s.grade},{s.thesis},Graduate\n")
            else:
                f.write(f"{s.get_id()},{s.name},{s.age},{s.grade},N/A,Student\n")
    print("Data saved to students.txt")

def load_from_file():
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[-1] == "Graduate":
                    g = GraduateStudent(data[1], int(data[2]), float(data[3]), data[4])
                    students.append(g)
                else:
                    s = Student(data[1], int(data[2]), float(data[3]))
                    students.append(s)
        if students:
            Student.total_students = max(s.get_id() for s in students)
        print("Data loaded from students.txt")
    except FileNotFoundError:
        print("No saved data found.")

#main program
def main():
    Student.welcome() 

    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. Add Graduate Student")
        print("3. View All Students")
        print("4. Search Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Show Total Students")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

       
        if choice == "1":
            add_student()
        elif choice == "2":
            add_graduate_student()
        elif choice == "3":
            view_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            Student.show_total_students()
        elif choice == "8":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

#run main program
if __name__ == "__main__":
    main()