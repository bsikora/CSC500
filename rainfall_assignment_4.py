
def main():

	data = []
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	try:
		num_years = int(input("Number of years: "))
		if num_years <= 0:
			raise
	except:
		print("Please make sure number of years is an integer and greater than 0")
		exit()
	total_rainfall = 0
	for i in range(0, num_years):
		month_data = {}
		j = 0
		while(j < len(months)):
			try:
				temp_rain = float(input("What are the inches of rain in " + months[j] + " of year " +str(i+1)+ ": "))
			except:
				print("Inches of rain fall needs to be a float!")
				continue
			total_rainfall = total_rainfall + temp_rain
			month_data.update({months[j]:temp_rain})
			j = j + 1
		data.append(month_data)

	print("Total months = ", num_years*len(months))
	print("Total rainfall = ", total_rainfall)

	for m in months:
		ave_rain = 0
		for d in data:
			ave_rain = ave_rain + d[m]
		print("Average rainfaill in",m,"=", str(ave_rain/num_years))

if __name__ == "__main__":
    main()