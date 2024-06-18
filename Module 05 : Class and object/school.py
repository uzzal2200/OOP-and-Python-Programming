class Student:
    def __init__(self, name, cls, id):
        self.name = name 
        self.id = id
        self.cls = cls
    def __repr__(self):
        return f' name : {self.name}, class : {self.cls}, id : {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self):
        return f'Teacher name : {self.name}, subject : {self.subject}, id : {self.id}'
    
class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    def add_teacher(self,name, subject):
        id = len (self.teachers) + 101
        teacher = Teacher( name, subject , id )
        self.teachers.append(teacher)

    def enroll ( self , name , fee ):
        id = len( self.students)
        student = Student('name' , 'C' , id)
        self.students.append(student)
        return f'{name} is enrolled with id : {id} extra fee : {fee - 6500}'
    def __repr__(self) -> str:
        print('Welcome to ', self.name)
        print('----------OUR TEACHER----------')
        for teacher in self.teachers:
            print(teacher)
        print('----------OUR STUDENTS----------')
        for student in self.students:
            print(student)
             

# pakhi = Student('noton pakhi' , 9, 220)
# print(pakhi)
# raihan = Teacher('Raihan', 'alogorithm', 101)
# print(raihan)
phitron = School('phitron')
phitron.enroll('noman',5300)
phitron.enroll('abir',6500)
phitron.enroll('noman',6700)
phitron.add_teacher('jhankar', 'OOP')
phitron.add_teacher('Rahat khan pathan', 'c c++ DSA')
phitron.add_teacher('arifur', 'Database')
print(phitron)



