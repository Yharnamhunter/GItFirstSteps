a = set()
s = ''
n = int(input())
while s != "HELP":
    s1 = set(list(map(int, input().split())))
    s = input()
    if s != "HELP":
        if s == "YES" or s == "NO":
            if s == "YES":
                a = a | s1
            else:
                a = a - s1
print(a)