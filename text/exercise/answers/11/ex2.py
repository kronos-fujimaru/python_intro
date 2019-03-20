import re

message = "My Phone Number is 112-221-222-3"

r = re.search("[0-9-]+", message)

print(r.group())
