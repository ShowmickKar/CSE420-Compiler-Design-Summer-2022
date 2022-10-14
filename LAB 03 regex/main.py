import re

# driver code
n = int(input())
regex_list = []
for _ in range(n):
    regex_list.append(input())
m = int(input())
strings = []
for _ in range(m):
    s = input()
    matches = False
    for i in range(len(regex_list)):
        if re.match(regex_list[i], s):
            print(f"YES, {i + 1}")
            matches = True
            break
    if not matches:
        print("NO 0")
