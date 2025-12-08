import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")

count_gray_fur = squirrel_data["Primary Fur Color"].value_counts().get("Gray", 0)
count_cinnamon_fur = squirrel_data["Primary Fur Color"].value_counts().get("Cinnamon", 0)
count_black_fur = squirrel_data["Primary Fur Color"].value_counts().get("Black", 0)
print(f"Gray:{count_gray_fur}, Cinnamon:{count_cinnamon_fur}, Black:{count_black_fur}")

squirrel_counts = {"Type": ["Gray", "Cinnamon", "Black"],
                   "Count": [count_gray_fur, count_cinnamon_fur,count_black_fur]}

squirrel_dataframe = pandas.DataFrame(squirrel_counts)
squirrel_dataframe.to_csv("Squirrel_Counts.csv")
print(squirrel_dataframe)