
score = 85

result = "Success" if score >= 80 else "Fail"


print(result)

####

arr = [1,2,3,4,5,5,5]

removal_set = {3,5}

result = []

for i in arr:
     if i not in removal_set:
          result.append(i)
print(result)




