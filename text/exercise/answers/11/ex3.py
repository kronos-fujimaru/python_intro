import re

while(True):
  val = input('input number')
  if re.match("\d+$", val) is None:
    print("NG")
  else:
    print("OK")
    
