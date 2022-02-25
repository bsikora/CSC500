
def main():

	data = []
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	num_years = int(input("Number of years: "))
	total_rainfall = 0
	for i in range(0, num_years):
		month_data = {}
		for m in months:
			temp_rain = float(input("What are the inches of rain in " + m + " of year " +str(i+1)+ " "))
			total_rainfall = total_rainfall + temp_rain
			month_data.update({m:temp_rain})
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