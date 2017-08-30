user_str = str(input("Enter a string"))

a = user_str.split()
b = dict()

for word in a:
    if word in b:
        b[word] += 1
    else:
        b[word] = 1

for key, value in b.items():
    print("{} {}".format(key, value))

for key in sorted(b):
    print("{:13}: {}".format(key, b[key]))
