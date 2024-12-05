import re

sample = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
mul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mu
mul(1,2)'''

RE=re.compile(r"mul\((\d{1,3}),(\d{1,3})\)", flags=re.MULTILINE)


def mul(values: tuple[str,str]) -> int:
    return int(values[0]) * int(values[1])

with open('/Users/sdilk/Downloads/adv/day3_input.txt') as fd:
    match = RE.findall(fd.read())
#match = RE.findall(sample)

summ = 0
for i in match:
    print(mul(i))
    summ += mul(i)

print(summ)
