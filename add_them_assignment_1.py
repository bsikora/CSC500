def add_two(num1, num2):
	return num1+num2

def sub_two(num1, num2):
	return num1 - num2

def main():
	num1_s = input("Please enter number 1: ")
	num2_s = input("Please enter number 2: ")

	try:
		num1 = float(num1_s)
		num2 = float(num2_s)
	except:
		print("Did you actually put in a number", num1_s, num2_s)
		exit()

	print(add_two(num1,num2))
	print(sub_two(num1, num2))

if __name__ == "__main__":
	main()