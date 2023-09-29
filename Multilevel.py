d={}
class student:
  def __init__(self):
    self.name=input("Enter the name ")
    self.usn=input("Enter the usn ")
    self.age=int(input("Enter the age "))
  def display(self):
    print("NAME",self.name)
    print("USN",self.usn)
    print("AGE",self.age)
class deriv1(student):
  def __init__(self):
    student.__init__(self)
    self.sem=input("Enter sem ")
    self.sub=[]
    self.total=0
    for i in range(1,6):
      m=int(input("Enter the marks in subject "))
      self.sub.append(m)
      self.total+=m
    self.per=(self.total/500)*100
    deriv1.display(self)
  def display(self):
    student.display(self)
    print("SEMISTER:",self.sem)
    for i in range(5):
      print("Marks in subject are ",self.sub[i])
    print("Percent =",self.per)
class deriv2(deriv1):
  def __init__(self):
    deriv1.__init__(self)
    d.update({self.name:{
             "name":self.name,
             "usn":self.usn,
             "age":self.age,
             "semester":self.sem,
             "subject":self.sub,
             "total":self.total,
             "percent":self.per,
            }})
def printtemp():
  for key in d:
    print(key,d[key])
while True:
  print("1.Add student details\n2.Display Student Details\n3.Exit")
  ch=int(input("Enter your choice"))
  if ch==1:
    d2=deriv2()
  elif ch==2:
    printtemp()
  elif ch==3:
    break
