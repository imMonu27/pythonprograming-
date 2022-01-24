s={1,2,3,4,5,6,7,8,9,10,55}

#len to get length of set 
print(len(s))

# remove to remove elements from set
s.remove(5)
print(s) 

# add adding values in set 
s.add(77)
print(s)

#pop remove an arbitriy element from the set and return the element removed 
print(s.pop())

#clear empties the set 
s.clear()
print(s)

# union return a new set with all iteam from both sets
a={1,2,3}
b={4,6,7}
print(a.union(b))

#interaction returns a set which contains only iteams in both set
c={12,33,44}
d={14,33,44}
print(c.intersection(d))