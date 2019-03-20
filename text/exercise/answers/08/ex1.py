nums = [100, 200, 400, 0, 300]

try:
    print(nums[4])
except IndexError as e:
    print("error")
else:
    print("success")
