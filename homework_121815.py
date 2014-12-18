'''
HOMEWORK: Reading and Writing Files in Python
@author: laura egerdal
Created on Wed Dec 17 19:30:57 2014
'''

# PART 1: Read in drinks.csv and store the header in a list
import csv
with open('drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    drinks = [row for row in csv.reader(f)]

# Part 2: Isolate the beer_servings column in a list of integers called 'beers'
beers = [row[1] for row in drinks]

# Part 3: Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'
NA_beers = [row[1] for row in drinks if row[5] == 'NA']
EU_beers = [row[1] for row in drinks if row[5] == 'EU']

# Part 4: Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
NA_avg = round(sum(float(row) for row in NA_beers)/len(NA_beers),2)
EU_avg = round(sum(float(row) for row in EU_beers)/len(EU_beers),2)

# Part 5: Write a CSV file called 'avg_beer.csv' with two columns and three rows
output = [['continent', 'avg_beer'], ['NA', NA_avg], ['EU', EU_avg]]
with open('beer_avgs.csv', 'wb') as f:
    csv.writer(f).writerows(output)



'''
BONUS:
Learn csv.DictReader() and use it to redo Parts 1, 2, and 3.
'''

# PART 1: Read in drinks.csv and store the header in a list
import csv
drinks = csv.DictReader(open('drinks.csv'))
header = drinks.fieldnames

# Part 2: Isolate the beer_servings column in a list of integers called 'beers'  
# Part 3: Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'

'''
It apppears that I can only iterate through a reader object once.
Given this, I'm building all three lists in one iteration.
'''
    
beer_servings = []
NA_beers = []
EU_beers = []

for row in drinks:
    beer_servings.append(row['beer_servings'])
    if row['continent'] == 'NA':
        NA_beers.append(row['beer_servings'])
    elif row['continent'] == 'EU':
        EU_beers.append(row['beer_servings'])
    else:
        pass
 
 
# Part 4 & 5 with DictWriter! 

# Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
# Write a CSV file called 'avg_beer.csv' with two columns and three rows

NA_avg = round(sum(float(row) for row in NA_beers)/len(NA_beers),2)
EU_avg = round(sum(float(row) for row in EU_beers)/len(EU_beers),2)

with open('beer_avgs2.csv', 'w') as csvfile:
    fieldnames = ['continent', 'avg_beer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()   
    writer.writerow({'continent': 'NA', 'avg_beer': NA_avg})
    writer.writerow({'continent': 'EU', 'avg_beer': EU_avg})
