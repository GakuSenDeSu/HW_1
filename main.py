# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '108038520.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive data points from the beginning.
target_data_1 = list(filter(lambda item: item['station_id'] == 'C0A880', data)) # Have checked: -99.000 all in other items, not in HUMD
target_data_2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', data)) # Have checked: -99.000 all in other items, not in HUMD
target_data_3 = list(filter(lambda item: item['station_id'] == 'C0G640', data)) # Have checked: -99.000 all in other items, not in HUMD
target_data_4 = list(filter(lambda item: item['station_id'] == 'C0R190', data)) # Have checked: -99.000 all in other items, not in HUMD
target_data_5 = list(filter(lambda item: item['station_id'] == 'C0X260', data)) # Have checked: -99.000 all in other items, not in HUMD

# Store HUMD data value
C0A880_HUMD = [row['HUMD'] for row in target_data_1]
C0F9A0_HUMD = [row['HUMD'] for row in target_data_2]
C0G640_HUMD = [row['HUMD'] for row in target_data_3]
C0R190_HUMD = [row['HUMD'] for row in target_data_4]
C0X260_HUMD = [row['HUMD'] for row in target_data_5]

# Sum
C0A880_Sum = sum(list(map(float,C0A880_HUMD)))
C0F9A0_Sum = sum(list(map(float,C0F9A0_HUMD)))
C0G640_Sum = sum(list(map(float,C0G640_HUMD)))
C0R190_Sum = sum(list(map(float,C0R190_HUMD)))
C0X260_Sum = sum(list(map(float,C0X260_HUMD)))


#=======================================


# Part. 4

#=======================================

# Print result

#print(C0A880_HUMD)
#print(C0A880_Sum)

print([['C0A880', C0A880_Sum], ['C0F9A0', C0F9A0_Sum], ['C0G640', C0G640_Sum], ['C0R190', C0R190_Sum], ['C0X260', C0X260_Sum]])


#========================================
