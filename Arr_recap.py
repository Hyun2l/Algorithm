arr = [1,2,3]


arr.append(4) # O(1)
# 마지막 element에 해당 숫자 추가


arr.insert(1,10) # O(N)
print("element added in 2nd place : ",arr)


arr.remove(10) # O(N) -> 너무 느림 so,

remove_set = {1,10}

removed = [i for i in arr if i not in remove_set]
print ("Removed in O(1) : ", removed)





arr.sort() # O(NlogN)
print("Ascending order : ",arr)


arr.sort(reverse = True )
print("Descending order : ", arr)


arr.reverse()
print("Fliping elements :", arr)



arr.count(1) # O(N)




