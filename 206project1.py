import os
import filecmp

def getData(file):
	reader = open(file, 'r')
	namelist = []
	
	for x in reader.readlines()[1:]:
		d = {}
		x = x.split(',')
		d['First'] = x[0]
		d['Last'] = x[1]
		d['Email'] = x[2]
		d['Class'] = x[3]
		d['DOB'] = x[4].strip()
		
		namelist.append(d)
		print (d)
	return namelist
		
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	

#Sort based on key/column
def mySort(data,col):
	newdata = sorted(data, key = lambda x: x[col])
	return newdata[0]['First'] + ' ' + newdata[0]['Last']
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	

#Create a histogram
def classSizes(data):
	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0
	for x in data:
		if x['Class'] == "Freshman":
			freshman += 1
		if x['Class'] == "Sophomore":
			sophomore += 1
		if x['Class'] == "Junior":
			junior += 1
		if x['Class'] == "Senior":
			senior += 1

	fresh = ('Freshman', freshman)
	soph = ('Sophomore', sophomore)
	jr = ('Junior', junior)
	sr = ('Senior', senior)
	
	tuplelist = []
	
	tuplelist.append(fresh)
	tuplelist.append(soph)
	tuplelist.append(jr)
	tuplelist.append(sr)
	
	return sorted(tuplelist, key = lambda x: x[1], reverse = True)
	
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]



# Find the most common day of the year to be born
def findDay(a):
	d = {}
	for x in a:
		bday = x['DOB']
		x = bday.split('/')
		y = x[1]
		if y not in d:
			d[y] = 1
		else:
			d[y] += 1
		# if x in d:
		# 	day = counts[x]
		# else:
		# 	day = 0
		# day = counts.get(x, 0)
		# counts[x] = counts.get(x, 0) + 1

	daylist = []
	
	for x in d.keys():
		tup = (x, d[x])
		daylist.append(tup)
	daysort = sorted(daylist, key = lambda x: x[1], reverse = True)
	daysorted = int(daysort[0][0])
	return daysorted	
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB




# Find the average age (rounded) of the Students
def findAge(a):
	agelist = []
	yearlist = []
	
	for x in a:
		year = int(x['DOB'][-4:])
		yearlist.append(year)
	
	for x in yearlist:
		agelist.append(2017-x)
	
	count = 0
	for avg in agelist:
		count += avg
	return (count // len(agelist))
		
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
	csv = open(fileName, 'w')
	
	sorteda = sorted(a, key = lambda x: x[col])
	for x in sorteda:
		csv.write('{},{},{}\n'.format(x['First'], x['Last'], x['Email']))
	csv.close()
#Input: list of dictionaries, key to sort by and output file name
#Output: None




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

