f = open('/Users/Alan/Desktop/CS_Primer_Package/AdventofCode/2018/Day03/data.txt', 'r')

data = []
for y in f:
    line = y.split()
    data.append(line)
    # data.sort()
    # print(line)

# print(data)

# Part ONE
clothCount = {}
allClaims = []

for line in data:
    claimID = line[0]
    begin = line[2].split(',')
    size = line[3].split('x')

    left = int(begin[0]) + 1 # begins where it should begin
    right = left + int(size[0]) # last num should not be included
    top = int(begin[1][:-1]) + 1 # sim left
    bot = top + int(size[1]) # sim right
    allClaims.append([claimID, left, right, top, bot]) # For Part TWO
    # print(left, right, top, bot)

    for i in range(left, right):
        for j in range(top, bot):
            clothCount[(i, j)] = clothCount.get((i, j), 0) + 1

overlap = 0
for key in clothCount.values():
    if key > 1:
        overlap += 1
print('Overlapping area =', overlap)

# Part TWO
for claim in allClaims:
    overlapFlag = True
    left = claim[1]
    right = claim[2]
    top = claim[3]
    bot = claim[4]
    
    for i in range(left, right):
        for j in range(top, bot):
            if overlapFlag and clothCount[(i, j)] > 1:
                overlapFlag = False

    if overlapFlag:
        print('The one claim that doesn''t overlap with anyone else: ', claim[0])
        # break