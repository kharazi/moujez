from __future__ import division

import pickle

a =  pickle.load(open("src.res"))
b = pickle.load(open("sum.res"))

c = 0
y = 0
for i in range(len(a)):
    c += 1
    if a[i] == b[i]:
        y += 1

print c, "c"
print y, "y"
print y / c * 100.0 