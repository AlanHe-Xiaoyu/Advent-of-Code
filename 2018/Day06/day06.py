f = open('/Users/Alan/Desktop/CS_Primer_Package/AdventofCode/2018/Day06/data.txt', 'r')

data = []
for y in f:
    line = y.split()
    x_axis = int(line[0][:-1])
    y_axis = int(line[1])
    data.append([x_axis, y_axis])
    # data.sort()

print(data)

# Part ONE
# for line in data:
    