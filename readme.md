[73, 74, 75, 71, 69, 72, 76, 73]
invert
[73, 76, 72, 69, 71, 75, 74, 73]

# 0
[(73), 76, 72, 69, 71, 75, 74, 73]
min = None
max = None
l = { 73: 0 }
[0]

# 1
[73, (76), 72, 69, 71, 75, 74, 73]
min = 73
max = 73
l = { 73: 0, 76: 1}
[0, 0]

# 2
[73, 76, (72), 69, 71, 75, 74, 73]
min = 73
max = 76
l = { 73: 0, 76: 1, 72: 2}
[0, 0, 1]

# 3
[73, 76, 72, (69), 71, 75, 74, 73]
min = 72
max = 76
l = { 73: 0, 76: 1, 72: 2, 69: 3}
[0, 0, 1, (i - l[72(next high value)])]

# 4
[73, 76, 72, 69, (71), 75, 74, 73]
min = 69
max = 76
l = { 73: 0, 76: 1, 72: 2, 69: 3}
[0, 0, 1, 1, (i - l[72])(2)]

# 5
[73, 76, 72, 69, 71, (75), 74, 73]
min = 69
max = 76
l = { 73: 0, 76: 1, 72: 2, 69: 3, 71: 4}
[0, 0, 1, 1, 2, (i - l[76])(4)]

# 6
[73, 76, 72, 69, 71, 75, (74), 73]
min = 69
max = 76
l = { 73: 0, 76: 1, 72: 2, 69: 3, 71: 4, 75: 5}
[0, 0, 1, 1, 2, 4, (i - l[75])(1)]

# 7
[73, 76, 72, 69, 71, 75, 74, (73)]
min = 69
max = 76
l = { 73: 0, 76: 1, 72: 2, 69: 3, 71: 4, 75: 5, 74: 6}
[0, 0, 1, 1, 2, 4, 1, (i - l[74])(1)]

ANS = [0, 0, 1, 1, 2, 4, 1, 1]