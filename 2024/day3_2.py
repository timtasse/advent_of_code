import re

sample = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
mul(1,2)do'''

RE_DO = re.compile(r"(?:do\(\)|^)(.+?)(?:don't|$)")
RE=re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def mul(values: tuple[str,str]) -> int:
    return int(values[0]) * int(values[1])

with (open('/Users/sdilk/Downloads/adv/day3_input.txt') as fd):
    sample = "".join(fd.read().splitlines())
summ = 0
for line in sample.splitlines():
    summ += sum([mul(i) for j in RE_DO.findall(line) for i in RE.findall(j) ])

print(summ)
