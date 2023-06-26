
counts = dict()
names = ['Hannah', 'Jonathan','Hannah', 'Lilly', 'Hannah', 'Jonathan', 'Nichole','Hannah', 'Jonathan', 'Lilly', 'Michael']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] +1


print(counts)