f = open('/Users/Alan/Desktop/CS_Primer_Package/AdventofCode/2018/Day04/data.txt', 'r')

sleepTotal = {}
guards = [None]*9999
data = []

for y in f:
    line = y.split()
    data.append(line)
    data.sort()
    # print(line)

# print(data)

for index in range(len(data)):
    line = data[index]
    # print(line)

    if line[2] == 'Guard':
        cur_num = line[3]
    elif line[2] == 'wakes':
        prevLine = data[index-1]
        start = int(prevLine[1][3:5])
        end = int(line[1][3:5])
        sleepTime = end - start

        sleepTotal[cur_num] = sleepTotal.get(cur_num, 0) + sleepTime
    
print(sleepTotal)
Guard = max(sleepTotal, key=lambda x: sleepTotal[x])
print('Guard', Guard, '\n')



timeTotal = {}
for index in range(len(data)):
    line = data[index]
    
    if line[2] == 'Guard':
        cur_num = line[3]
    elif line[2] == 'wakes' and cur_num == Guard:
        prevLine = data[index-1]
        start = int(prevLine[1][3:5])
        end = int(line[1][3:5])
        
        for sleeping in range(start, end):    
            timeTotal[sleeping] = timeTotal.get(sleeping, 0) + 1

print(timeTotal)
Time = max(timeTotal, key=lambda x: timeTotal[x])
print('Time', Time, '\n\n\n')



# Stategy 2
allGuardsChart = {}
for possibleGuard in sleepTotal.keys():
    timeTotal = {}
    for index in range(len(data)):
        line = data[index]
    
        if line[2] == 'Guard':
            cur_num = line[3]
        elif line[2] == 'wakes' and cur_num == possibleGuard:
            prevLine = data[index-1]
            start = int(prevLine[1][3:5])
            end = int(line[1][3:5])
        
            for sleeping in range(start, end):    
                timeTotal[sleeping] = timeTotal.get(sleeping, 0) + 1

    # print(timeTotal)
    maxTime = max(timeTotal, key=lambda x: timeTotal[x])
    allGuardsChart[possibleGuard] = maxTime

print(allGuardsChart)
maxFreq = max(allGuardsChart.values())
maxFreqGuard = max(allGuardsChart, key=lambda x: allGuardsChart[x])
print('Guard', maxFreqGuard)
print('Freq', maxFreq)
print('Final answer', maxFreq * int(maxFreqGuard[1:]))