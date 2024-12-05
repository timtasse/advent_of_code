import typing
#list1 = []#3,4,2,1,3,3]
#list2 = []#4,3,5,3,9,3]
liste = []
with open('/Users/sdilk/Downloads/adv/day2_input.txt') as fd:
    for line in fd.readlines():
        liste.append([int(i) for i in line.split()])
#        val1, val2 = line.split()
#        list1.append(int(val1))
#        list2.append(int(val2))

#liste = [
#    (7,6,4,2,1),
#    (1,2,7,8,9),
#    (9,7,6,2,1),
#    (1,3,2,4,5),
#    (8,6,4,4,1),
#    (1,3,6,7,9)
#]
#print(liste)
def check(values: typing.Iterable[int]) -> bool:
    typ = 0 # 0 = undef, 1 = inc, 2 = dec
    last = 0
    for i in values:
        if typ == 1:
            if i <= last:
                return False
            if abs(i-last) > 3:
                return False
        elif typ == 2:
            if i >= last:
                return False
            if abs(last - i) > 3:
                return False
        else:
            if last:
                if last < i:
                    typ = 1
                elif last > i:
                    typ = 2
                else:
                    return False
                if abs(last - i) > 3:
                    return False
        last = i
    return True

summ = 0
for values in liste:
    val = check(values)
    if val:
        print(f"{values}: {val}")
        summ += 1
        
print(summ)
