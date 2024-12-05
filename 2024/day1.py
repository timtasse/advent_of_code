
list1 = []#3,4,2,1,3,3]
list2 = []#4,3,5,3,9,3]
with open('/Users/sdilk/Downloads/adv/day1_input.txt') as fd:
    for line in fd.readlines():
        val1, val2 = line.split()
        list1.append(int(val1))
        list2.append(int(val2))

list1.sort()
list2.sort()
summ = 0
for i in range(len(list1)):
    summ += abs(list1[i] - list2[i])

print(summ)
