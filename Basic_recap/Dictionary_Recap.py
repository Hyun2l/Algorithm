# Dictionary

dict = dict()

dict['A'] = 'Apple'
dict['B'] = "Banana"
dict['C'] = "Coconut"

if "Apple" in dict:
    print("there is a data which has 'Apple' as the key")

    #####


# Only Key data
key_list = dict.keys()

# Only value data
value_list = dict.values()



#### Set ### O(1)

set = set([1,2,3])

set.add(4)
print(set)

set.update([6,9,100000])

print(set,"Updatated new data")

