# with open("weather_data.csv", "r") as csv_file:
#     data = csv_file.readlines()

# print(data)

# import csv
# with open("weather_data.csv", "r") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#
#     temperatures.remove("temp")
#     print(temperatures

import pandas

data = pandas.read_csv("weather_data.csv")

""" data_dict = data.to_dict()
print(data_dict) """

""" temp_list = data["temp"].to_list()
print(temp_list)
print(sum(temp_list) / len(temp_list)) """

""" print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data.condition)
print(data["condition"])
 """
#Get Data in a Row
""" print(data[data.condition == "Sunny"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
celcius = monday.temp[0]
print(monday.temp)
fahrenheit = celcius * (9/5) + 32
print(fahrenheit)"""

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Kerem"],
    "scores": [76, 56, 97]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")