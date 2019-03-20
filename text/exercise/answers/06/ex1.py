def average(*nums):

    num_sum = 0
    for num in nums:
        num_sum += num

    return num_sum / len(nums)

result1 = average(10, 20, 30, 40)
result2 = average(100, 300, 200)

print(result1)
print(result2)
