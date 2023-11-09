from datetime import date

print(date.today())
print(type(date.today()))

dates = str(date.today())
print(dates)
date_list = dates.split("-")
print(date_list)
new_date = date_list[1]+"/"+date_list[2]+"/"+date_list[0]
print(new_date)
