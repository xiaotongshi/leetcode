import sys
import collections
# num = [4, 5, 6, 7, 8]
# hua = ['H', 'S', 'C', 'D', 'D']
num = []
hua = []
d = {str(i):i for i in range(2, 11)}
d['A'] = 1
d['J'] = 11
d['Q'] = 12
d['K'] = 13
for _ in range(5):
    n, h = list(sys.stdin.readline().split())
    num.append(d[n])
    hua.append(h)

tonghua = False
if hua.count(hua[0]) == 5:
    tonghua = True

shunzi = False
santiao = False
sitiao = False
hulu = False
cn = list(collections.Counter(num).values())

if 4 in cn:
    sitiao = True
if 3 in cn:
    santiao = True
if 2 in cn:
    hulu = True
if sum(cn) == 5:
    if (max(num) - min(num) == 4) or (sum(num) - 1 == 46):
        shunzi = True

if tonghua & shunzi:
    res = 1
elif sitiao:
    res = 2
elif santiao & hulu:
    res = 3
elif tonghua:
    res = 4
elif shunzi:
    res = 5
elif santiao:
    res = 6
else:
    res = 7
print(res)