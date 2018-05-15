# -*- coding: utf-8 -*-

import csv, sys , pprint , math

rooster = []
table = {}
nrr = {}


# ---------------------------------Load Points table, and net run rate ---------------------------------
filename = 'pTable.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:

            table[row[0]] = int(row[5])
            nrr[row[0]] = float(row[6])

    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
f.close()


#------------------------------------Load the Remaining fixtures left -----------------------------------

filename = 'fixtures.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:

            rooster.append([row[0],row[1]])

    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
f.close()

#------------------------------Calculating the tentative points table at end of season -------------------


points = []
points.append(table.copy())
points_new = []

for i in range(len(rooster)) :
	for k in range(len(points)) :
		temp = points[k].copy()
		for j in range(2) :
			if j == 0 :

				points[k][rooster[i][j]] = points[k][rooster[i][j]] + 2  # Adds 2 points to the winning team

			else :

				temp[rooster[i][j]] = temp[rooster[i][j]] + 2  # Adds 2 points to the winning team
				points.append(temp.copy()) # Creates another points table for an alternate winning scenario


#------------------------------Sort the points table according to the net run rate-------------------


for i in points :

	result= [k for k in sorted(nrr, key=nrr.get)] # Sorts the Team according to NRR
	result = sorted(result, key=i.get)            # Sorts the Team accoring the points  
	points_new.append(result[:])                  # Slices and appends the new sorted points table into a new list


#------------------------------Input the number of teams that can qualift to the next stage-------------------

print("number of teams that can qualift to the next stage : ")
qualify = int(raw_input())


#------------------------------Predict the chances of each team qualifying to next stage-------------------


predict = {'SRH':0.00000000,'CSK':0.00000000,'KKR':0.00000000,'RR':0.00000000,'KXIP':0.00000000,'MI':0.00000000,'RCB':0.00000000,'DD':0.00000000}

for i in points_new :
	for j in i[-qualify:] :  # Only the Top teams which qualify in each scenario

		predict[j] = predict[j] + 1/(math.pow(2,len(rooster))) # Total no of math.pow(2,len(rooster)) outcomes possible. , so each outcomes adds a weight of 1/math.pow(2,len(rooster)) to the team

pprint.pprint(predict)














