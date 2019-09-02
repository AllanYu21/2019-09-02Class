# basics.py

x = input("Input a command: ")
print("You entered {}.".format(x))
if x == 'add' or x != 'a': 
 	print("Add")
 	a = 1
 	b = 2
 	print("a = {}".format(a))
 	c = a + b
 	print("{} + {} = {}".format(a,b,c))
elif x == 's' :
 	print("subtract")
 	a = 1 
 	b = 2 
 	c = a - b
 	print ("{} - {} = {}".format(a,b,c))
else:
	print("Is not an active command")
	print("Enter a new command")

print("Done")