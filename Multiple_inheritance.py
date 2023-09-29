class student:
  def __init__(self):
    self.name=input("Enter the name ")
    self.usn=input("Enter the usn ")
  def display(self):
    print("Name:",self.name)
    print("Usn:",self.usn)
    print("Age:",self.age)
class ugstudent(student):
  def __init__(self):
    student.__init__(self)
    self.sem=input("Enter the sem ")
    self.fee=int(input("Enter the fee "))
    self.stipend=int(input("Enter the balance "))
    ugstudent.display(self)
  def display(self):
    student.display(self)
    print("SEMISTER:",self.sem)
    print("FEE:",self.fee)
    print("STILLPENDING:",self.stipend)
class pgstudent(student):
  def __init__(self):
    student.__init__(self)
    self.sem=input("Enter the sem ")
    self.fee=int(input("Enter the fee "))
    self.stipend=int(input("Enter the balance "))
    pgstudent.display(self)
  def display(self):
    student.display(self)
    print("SEMISTER:",self.sem)
    print("FEE:",self.fee)
    print("STILLPENDING",self.stipend)
while True:
  print("1.UG student\n2.PG student\n3.Exit")
  ch=int(input("Enter your choice "))
  if ch==1:
    ug=ugstudent()
    ug.display()
  elif ch==2:
    pg=pgstudent()
    pg.display()
  else:
    break
