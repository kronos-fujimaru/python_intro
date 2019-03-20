# f = open("hello.txt", "w", encoding="utf-8")
# f.write("Hello World!")
# f.close()

with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello World!")
