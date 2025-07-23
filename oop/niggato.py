class Student :
    def __init__(self,nom,grade):
        self.nom = nom 
        self.grade = grade

class Classroom:
    def __init__(self, name,maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []
    
    def addStudent(self,student):
        if(len(self.students) < self.maxStudents):
            self.students.append(student)
        else :
            print("I CANT ADD THE STUDENT IM SORRY :(")
    

    def display(self):
        print("Les etudiants :")
        for i in range(0,len(self.students)):
            print(self.students[i].nom)
    

s1 = Student("Haitham",19)
s2 = Student("Mouad",8)
s1 = Student("Guiltra", -1)

python = Classroom("python",2)

python.addStudent(s2)
python.display()