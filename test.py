arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rev = True
for i in arr:
    if rev:
        for k in i:
            print(k, end=" ")
        rev = False
    else:
        for k in reversed(i):
            print(k, end=" ")
        rev = True