list1 = [1,3,5,7]
list2 = [2,4,6,8]
z = zip(list1, list2)
print(z)
z_list = list(z)
print(z_list)


unzipped =zip(*z_list)
l1, l2 = list(unzipped)
print(l1)