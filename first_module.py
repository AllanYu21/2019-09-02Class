# first_module.py


def addition(a, b):
 	print("Add")
 	
 	print("a = {}".format(a))
 	c = a + b
 	print("{} + {} = {}".format(a,b,c))
 	return 

def subtraction(a,b):
 	print("subtract")
 	c = a - b
 	print ("{} - {} = {}".format(a,b,c))
 	return
def addsubtract(a,b,symbol):
	if symbol == "+":
		c = a+b
	elif symbol == "-":
		c = a-b
	else:
		c = "Unreconginzed"
	return c		


if __name__ == "__main__":
	x = input("Input a command: ")
	print("You entered {}.".format(x))

	a = input("a = ")
	b = input("b = ")

	if x == 'add' or x == 'a': 
	 	answer = addsubtract(int(a),int(b),"+")
	elif x == 's' :
		answer = addsubtract(int(a),int(b),"-")
	 	
	else:
		print("Is not an active command")
		print("Enter a new command")

	print("c = {}".format(answer))
	print("Done")