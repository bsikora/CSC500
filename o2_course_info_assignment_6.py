def main():

	c_n = input("Course name: ")
	room = {"CSC101":3004,"CSC102":4501,"CSC103":6755,"NET110":1244,"COM241":1411}
	instructor = {"CSC101":"Haynes","CSC102":"Alvarado","CSC103":"Rich","NET110":"Burke","COM241":"Lee"}
	meeting = {"CSC101":"8:00 a.m.","CSC102":"9:00 a.m.","CSC103":"10:00 a.m.","NET110":"11:00 a.m.","COM241":"1:00 p.m."}

	if c_n in room:
		print(c_n, "room", room[c_n],"Instructor", instructor[c_n], "Time", meeting[c_n])
	else:
		print(c_n, "was not a valid course offering.")

if __name__ == "__main__":
    main()