# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
# Part. 2
# #=======================================
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
C0A880_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
C0F9A0_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
C0G640_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
C0R190_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
C0X260_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Store HUMD data value
C0A880_HUMD = [row['HUMD'] for row in C0A880_data]
C0F9A0_HUMD = [row['HUMD'] for row in C0F9A0_data]
C0G640_HUMD = [row['HUMD'] for row in C0G640_data]
C0R190_HUMD = [row['HUMD'] for row in C0R190_data]
C0X260_HUMD = [row['HUMD'] for row in C0X260_data]

# Find "-99.000" and "-999.000", and substitute to "None"
if '-99.000' in C0A880_HUMD or '-999.000' in C0A880_HUMD:
   C0A880_HUMD['-99.000'] = "None"
   C0A880_HUMD['-999.000'] = "None"
   C0A880_Sum = "None"
else:
   # Sum
   C0A880_Sum = sum(list(map(float,C0A880_HUMD)))
#===
if '-99.000' in C0F9A0_HUMD or '-999.000' in C0F9A0_HUMD:
   C0F9A0_HUMD['-99.000'] = "None"
   C0F9A0_HUMD['-999.000'] = "None"
   C0F9A0_Sum = "None"
else:
   C0F9A0_Sum = sum(list(map(float,C0F9A0_HUMD)))
#===
if '-99.000' in C0G640_HUMD or '-999.000' in C0G640_HUMD:
   C0G640_HUMD['-99.000'] = "None"
   C0G640_HUMD['-999.000'] = "None"
   C0G640_Sum = "None"
else:
   C0G640_Sum = sum(list(map(float,C0G640_HUMD)))
#===
if '-99.000' in C0R190_HUMD or '-999.000' in C0R190_HUMD:
   C0R190_HUMD['-99.000'] = "None"
   C0R190_HUMD['-999.000'] = "None"
   C0R190_Sum = "None"
else:
   C0R190_Sum = sum(list(map(float,C0R190_HUMD)))
#===
if '-99.000' in C0X260_HUMD or '-999.000' in C0X260_HUMD:
   C0X260_HUMD['-99.000'] = "None"
   C0X260_HUMD['-999.000'] = "None"
   C0X260_Sum = "None"
else:
   C0X260_Sum = sum(list(map(float,C0X260_HUMD)))
#=======================================
# Part. 4
#=======================================
# Print result
#print(C0A880_HUMD)
#print(C0A880_Sum)
#print(['C0A880', C0A880_Sum])
print([['C0A880', C0A880_Sum], ['C0F9A0', C0F9A0_Sum], ['C0G640', C0G640_Sum], ['C0R190', C0R190_Sum], ['C0X260', C0X260_Sum]])
#========================================
