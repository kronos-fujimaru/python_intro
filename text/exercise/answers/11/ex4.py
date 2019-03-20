mail_re = "^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+\.([a-zA-Z0-9\._-]+)+$"

import re

while(True):
  val = input('input mail')
  if re.match(mail_re, val) is None:
    print("NG")
  else:
    print("OK")
