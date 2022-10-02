print("program to change the first item (22) of a lsit within the following tuple to 222")
t=(11,[22,33],44,55)
print(t)
x=list(t)
x[1][0]=222
t=tuple(x)
print(t)