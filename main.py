# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row[1])

# to extract rows and column using pandas
import pandas
# data = pandas.read_csv("weather_data.csv")
#
# monday = data[data.day == "Monday"]
# temp_max  = monday.temp[0]
# print(temp_max)
# cogo = (temp_max * 9/5) + 32
# print(cogo)

#create a dataframe from scratch
# data_dict = {
#     "students":["amy", "ase","pav"],
#     "score":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_sui =data[data["Primary Fur Color"] == "Gray"]
print(grey_sui)