a='abracadabra'
b = set(a)
print(f"unique values of string: {b}\n\n\n")
d={}
for i in b:
	d[i] = 0

print(d, "\n\n\n")

for j in a:
	d[j] += 1
				
print(d)



# =========================================================#
# Easy way of doing the problem
# d={}
# for i in b:
# 	d[i] = a.count(i)

# print(d)