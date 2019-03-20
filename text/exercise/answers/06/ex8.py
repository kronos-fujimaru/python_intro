@processing
def add_all_count(count):
    total = 0
    for i in range(count):
      total += i
    return total

def processing(func):
    def new_function(*args):
        print("processing...")
        result = func(*args)
        print("finished")
        return result
    return new_function


total = add_all_count(10000000)
print(total)
