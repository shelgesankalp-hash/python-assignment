#Create sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}


#Access set elements (Iterate through set)
print("set 1 elements:")
for elem in set1:
    print(elem,end="")
    print("\nSet 2 elements:")
    for elem in set2:
        print(elem, end="")
        print()


#Union Sets
union_set = set1.intersection(set2)
print("Union of set1 and set2:", union_set)


#Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:",
intersection_set)


#Difference of sets (Set1 - set2)
difference_set = set1.difference(set2)
print("Difference(set1 - set2):", difference_set)


#Difference of sets (set2 - set1)
difference_set2 = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2)