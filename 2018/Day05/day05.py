f = open('/Users/Alan/Desktop/CS_Primer_Package/AdventofCode/2018/Day05/data.txt', 'r')

for y in f:
    data = y
# print(data)
print(len(data))

# Part ONE
def react(polymer):
    index = 0
    
    while index + 1 < len(polymer):
        cur = ord(polymer[index])
        fut = ord(polymer[index + 1])

        if abs(cur - fut) == 32:
            polymer = polymer[:index] + polymer[index+2:]
            if index != 0:
                index -= 1
        else:
            index += 1

    return len(polymer)
    # print(index)

print('Remaining units:', react(data))

# Part TWO
shortest = len(data)
for i in range(26):
    polymer = data
    removing_upper = chr(65 + i) # From A to Z
    removing_lower = chr(97 + i) # From a to z

    polymer = "".join([char for char in polymer if char != removing_upper])
    polymer = "".join([char for char in polymer if char != removing_lower])

    # print(len(polymer))

    curLength = react(polymer)
    
    if shortest > curLength:
        shortest = curLength

print('Shortest possible length is', shortest)