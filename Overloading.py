class cal:
	def area(self,l=None,b=None,h=None):
		if l!=None and b!=None and h!=None:
			print("Area of trianle ",l*b*h)
		elif l!=None and b!=None:
			print("Area of rectangle ",l*b)
		elif l!=None:
			print("Area of sqaure is",l*l)
c1=cal()
a=int(input("Enter length of square"))
c1.area(a)
a=int(input("Enter length of rectangle"))
b=int(input("Enter the breadth of rectangle"))
c1.area(a,b)
a=int(input("Enter length of triangle"))
b=int(input("Enter the breadth of triangle"))
c=int(input("Enter height of triangle"))
c1.area(a,b,c)
		
