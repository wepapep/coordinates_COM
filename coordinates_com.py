################################################################
#calculate centre of mass for given set of coordinates
#outputs the results to a separate txt file
#im too lazy to provide reading of coordinates from another file
#the format for each line of input is
#locationname [list of points]
#where list of points is a list with all points, comma separated
#the format for a single point is
#[latitude, longitude]
#use google for coordinates or idk
#works with weather forecast script
#maybe I'll merge both of them into single script one day
#maybe
################################################################

rdown = 6; #amount of digits past point
coordinates_filename = "xycoords.txt";

xycoords = open(coordinates_filename, "w");

#insert coordinates here according to required format (see above)
#[ [string_name [ [point1_X, point1_Y] ... ] ], ... ];
coordinateslist = [
];

for coordinates in coordinateslist:
	x_com = 0;
	y_com = 0;
	farmname = coordinates[0];
	for P in coordinates[1]:
		x_com += P[0];
		y_com += P[1];

	P_com = [round(x_com/len(coordinates[1]),rdown), round(y_com/len(coordinates[1]),rdown)];

	print(coordinates[0], P_com[0], ",", P_com[1]);
	xycoords.write(str(coordinates[0]) + " " + str(P_com[0]) + " " + str(P_com[1]) +"\n");
