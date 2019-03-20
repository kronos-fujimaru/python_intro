class ShortError(Exception):
    pass

nums = [100, 200, 400, 0, 300]

for num in nums:
    try:
        if num < 100:
            raise ShortError
        else:
            print(num)
    except ShortError as e:
        print("num is short")
