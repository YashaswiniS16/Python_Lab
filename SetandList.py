while True:
	print("1.List Operations\n")
	print("2.Set Operations\n")
	print("3.Exit\n")
	n=int(input("Enter your choice"))
	if n==1:
		l=[]
		a=int(input("Enter the range\n"))
		print("Enter list Elements\n")
		for i in range(0,a):
			l.append(input())
		while True:
			print("\n1.Append a Element into list\n")
			print("2.Insert an element in to list\n")
			print("3.Remove an element in the list\n")
			print("4.Pop a element\n")
			print("5.Maximum element of the list\n")
			print("6.Minimum of the list\n")
			print("7.Sorting of list\n")
			print("8.Reverse of the lis\n")
			print("9.Length of the List\n")
			print("10.Count number of times elements repeated\n")
			print("11.Slice of the lis\n")
			print("12.Exit to menu\n")
			print("13.Exit\n")
			print(l)
			b=int(input("Enter your choice\n"))
			if b==1:
				l1=input("Enter the element to be appended")
				l.append(l1)
				print("After appending list is ",l)
			elif b==2:
				l3=input("Enter the element to be inserted")
				l4=int(input("Enter the position to be inserted"))
				l.insert(l4,l3)
				print("After inserting list is ",l)
			elif b==3:
				print(l)
				l5=input("Enter the element to be removed")
				l.remove(l5)
				print("After removing list is ",l)
			elif b==4:
				print("The poped element is",l.pop())
			elif b==5:
				print("The maximum element is ",max(l))
			elif b==6:
				print("The minimum element is ",min(l))
			elif b==7:
				l.sort()
				print("After sorted list is ",l)
			elif b==8:
				lr=l.reverse()
				print("Reverse of the list ",l)
			elif b==9:
				print("Length of the list",len(l))
			elif b==10:
				l6=input("Enter the elements to be counted")
				print("Count of ",l6,"is",l.count(l6))
			elif b==11:
				s1=int(input("Enter the starting position"))
				e=int(input("Enter the ending position"))
				print(l[s1:e])
			elif b==12:
				break
			elif b==13:
				exit()
			else:
				exit()
	if n==2:
		s={12,16,36,89}
		s1={12,56,32}
		while True:
			print("\n1.Length of the set\n")
			print("2.Union of the set\n")
			print("3.Intersection of set\n")
			print("4.Difference of the set\n")
			print("5.Symmetric Difference of the set\n")
			print("6.Add element to the set\n")
			print("7.Check if element is present in the set\n")
			print("8.Check for subset\n")
			print("9.Remove element from set\n")
			print("10.Maximum and minimum of the set\n")
			print("12.Exit to Menu\n")
			print("13.Exit")
			print(s)
			c=int(input("Enter your choice\n"))
			if c==1:
				print("Length of the set is ",len(s))
			elif c==2:
				print(s,"Union",s1,"is",s.union(s1))
			elif c==3:
				print(s,"Intersection",s1,"is",s.intersection(s1))
			elif c==4:
				print(s,"Difference",s1,"is",s1.difference(s1))
			elif c==5:
				print(s,"Symmetric Difference",s1,"is",s.symmetric_difference(s1))
			elif c==6:
				s3=int(input("Enter the element to be added"))
				s.add(s3)
				print("After adding",s)
			elif c==7:
				s4=int(input("Enter the element to be checked"))
				if s4 in s:
					print(s4,"Element Exists")
				else:
					print(s4,"doesnt exist")
			elif c==8:
				print(s1.issubset(s))
			elif c==9:
				s5=int(input("Enter the element to be removed"))
				s.remove(s5)
				print("After removing ",s)
			elif c==10:
				print("Maximum is ",max(s),"Minimum is ",min(s))
			elif c==12:
				break
			elif c==13:
				exit()
			else:
				exit()
	elif n==3:
		exit()
	else:
		exit()
