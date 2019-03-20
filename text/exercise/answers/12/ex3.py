from datetime import datetime

date_str = "02-12-2018"
d = datetime.strptime(date_str, "%d-%m-%Y")

print(d)
