def main():
	
	time_now = int(input("What is the time now? "))
	alarm = int(input("How many hours until the alarm goes off? "))
	alarm_time = (time_now+alarm)%24

	print(alarm_time)

if __name__ == "__main__":
	main()