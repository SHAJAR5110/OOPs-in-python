class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def display(self):
        print(f"Name : {self.name} \nMarks :{self.marks}")

student1=student('shajar',90)        
student1.display()

student2=student('Hasnat',95)
student2.display()
        