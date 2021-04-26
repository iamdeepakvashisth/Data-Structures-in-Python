x={1:10, 2:20}
y={3:30, 4:40}
z={5:50,6:60}
for d in (y,z):
    x.update(d)
print(x)