'''A = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# please provide one line of Python that takes 𝐴 and makes a new list having only the even intergers of list 𝐴.

B = [i for i in A if i%2 == 0]

print(B)'''

'''import random

# generate two lists A and B randomly
A = [random.randint(1, 100) for i in range(12)]
B = [random.randint(1, 100) for i in range(16)]
# generate a list that contains only the elements in both generated lists without duplicates
# using as few lines as possible 
common = [data for data in A if (data in B)]
result = [] if common == [] else list(set(common))
result.sort(key = common.index)
print('The generated two lists A and B:')
print('A=', A)
print('B=', B)
print('Overlaps with duplicates:', common)
print('Resulting list:', result)'''

'''import random

# generate a number randomly with at most 13 digits 
num = [str(random.randint(0,9)) for i in range(random.randint(1,13))]
if len(num)>1 and num[0] == '0':num.pop(0)
given_number = "".join(num)
# compute the maximum shuffling difference
num.sort(reverse=True)	#ex:1234952 -> 9543221
M = "".join(num)
num.sort()				#ex:1234952 -> 1223459
m = "".join(num)
difference = int(M) - int(m)
print("The given number", given_number, " has the maximum shuffling difference",
      difference, "(=", M, "-", m, ").")
'''
'''
#
# Write a Python class named Rectangle constructed by a length and width 
# in addition, it has a method, area(), to compute the area of a rectangle.

class Rectangle():
	def __init__(self,length,width):
		self.length = length
		self.width = width
	def area(self):
		return self.length * self.width

length = int(input("Please give the length of the rectangle:"))
width = int(input("Please give the width of the rectangle:"))
newRectangle = Rectangle(length, width)
print('the area of the input rectang is', newRectangle.area())'''

import random

number = [random.randint(0,9) for i in range(4)]#
print(number)
print("Welcome to the A and B Game and a 4-digit number is generated.\nPlease guess a number:")
while(True):
	guess = str(input())#"Please guess a number:"#print(guess)
	if(guess == "exit"):
		print("the correct number is","".join([str(i) for i in number]))
		break
	guess_num = [int(i) for i in guess]#print(guess_num)
	A = B = 0
	for i in range(4):
		if number[i] == guess_num[i]:	#correct number and position
			A+=1
		elif number[i] in guess_num:	#have number but wrong position
			B+=1
	print(A,"A,",B,"B")
	if A == 4:
		print("correct")
		break