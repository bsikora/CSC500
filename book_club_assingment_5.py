def main():


	s_num_books = input("Number of books you have purchased this month: ")
	try:
		num_books = int(s_num_books)
	except:
		print("String given in input was not an int, please try with an int!")
		exit()

	num_points = 0
	if num_books == 0:
		num_points = 0
	elif num_books == 2:
		num_points = 5
	elif num_books == 4:
		num_points = 15
	elif num_books == 6:
		num_points = 30
	elif num_books >= 8:
		num_points = 60

	print("Number of points earned =", num_points)

if __name__ == "__main__":
    main()