list1 = [1,2,3]
list2 = [i + 1 for i in list1]
print(list1)
print(list2)



print([str(i) +' is even' if i%2==0 else str(i) +' is odd' for i in range(1,100) ])