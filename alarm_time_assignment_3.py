def main():
	need_info = True
	while(need_info):
		try:
			time_now = int(input("What is the time now? "))
			if time_now <0 or time_now >23:
				raise ValueError
			alarm = int(input("How many hours until the alarm goes off? "))
			need_info = False
		except:
			print("Are you sure the time now is an int and between 0 and 24 hours?")
			print("Are you sure the number of hours until the arm goes off is an int?")
			need_info = True


	alarm_time = (time_now+alarm)%24

	print(alarm_time)

if __name__ == "__main__":
	main()