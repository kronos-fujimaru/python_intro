count = 0

while(count < 3):
    count += 1
    if(count == 2):
        continue
    if(count == 4):
        break

    print(count)
else:
    print("success")
