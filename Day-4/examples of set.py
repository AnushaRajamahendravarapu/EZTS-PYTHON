#union
a={1,2,3,4,5}
b={3,2,1,4,5}
print(a.union(b))
print(a|b)

#intersection
a={1,3,5,2}
b={2,3,6,7}
print(a.intersection(b))
print(a&b)

#intersection_update
a={2,3,7,8}
b={3,4,7,9}
a.intersection_update(b)
print(a)

#difference
a={2,4,6,8}
b={1,3,5,7}
print(a.difference(b))
print(a-b)

#difference_update
a={1,2,3,4}
b={2,3,5,6}
a.difference_update(b)
print(a)

#symmetric_difference
a={1,2,3,4}
b={2,3,5,6}
print(a.symmetric_difference(b))
print(a^b)

#symmetric_difference_update
a={1,2,3,4}
b={2,3,5,6}
a.symmetric_difference_update(b)
print(a)

#isdisjoint
a={1,2,3,4}
b={2,3,5,6}
print(a.isdisjoint(b))

#issubset
a={1,2,3,4}
b={2,3}
print(a.issubset(b))

#issuperset
a={1,2,3,4}
b={2,3}
print(a.issuperset(b))

