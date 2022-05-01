import csv
postcode = []
with open('postcodes.csv') as csvfile:
        reader = csv.reader(csvfile)
        #save each value to a array
        for i in reader:
            postcode.append(i[0])

print(postcode)

