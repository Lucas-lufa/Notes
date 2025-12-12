with open('24/s1', 'r') as f:
    s1 = f.read()
with open('24/s2', 'r') as f:
    s2 = f.read()
s1s = s1.split('\n')
s2s = s2.split('\n')

totals = []

for each in s1s:
    x = s2s.count(each)
    x = x * int(each)
    totals.append(x)

print(sum(totals))