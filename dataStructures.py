# list 
print("\n ---list ---\n")


numbers= [1,2,3,4]

fruits= ['apple','orange','mango']

mixed= [1,'apple',True]

# access index of list with square brackets
print('\n access list')
print(numbers[0]) 
print(fruits[-1])
print(mixed[2])

# modify list values
print('\n modify list values')
fruits.append('melon')
fruits.insert(0, 'corn')

print('\n add new values with append and insert :',fruits)

fruits.remove('apple')

print('\n remove apple values with remove :',fruits)

del fruits[0]

print('\n remove index 0 values with del :',fruits)

# slicing list

print('\n slice values of list')

sliced_fruits = fruits[0:2]

print('\n slice fruits values [0:2]',sliced_fruits)

# tuple
print("\n ---tuple ---\n")


colors=('red', 'green', 'blue', 'yellow')
single_colors=('glass', )

# access tuple values

print('\n access tuple values with index 0',colors[0])
print('\n access tuple values with index -1',colors[1])
print('tuples is imutable items ')

# dictionaries
print("\n ---dictionaries ---\n")

student= {"name":"sungep","age":25,"grade":"A"}

print(student)

# access dict items 

print(student['grade'])

# modify dict items

student['subject']="math"
print('add new items to student',student)


# update dict values

student['age']=22

print('update age values in dict',student)

# remove item with pop

student.pop('subject')

print('remove item with key subject with pop',student)

# loops dictionaries

for key,values in student.items():
    print('looping items',key,values)

# sets
print("\n ---sets ---\n")


numbers_sets={1,2,3,4}

empty_set={}

print(numbers_sets)
# modify sets

numbers_sets.add(5)

print('add sets values',numbers_sets)

numbers_sets.remove(1)

print('remove sets values',numbers_sets)

set1={1,2,3}
set2={3,4,5,}

# union values in sets

union_sets=set1 | set2

print('union sets values',union_sets)

# intersection values in sets

intersec_sets=set1 & set2

print('intersec sets valuess',intersec_sets)

# difference values in sets

diff_sets=set1 - set2

print('diff sets values',diff_sets)

# exercise manipulation data in dictionary

print("\n ---exercise ---\n")


person={'name':'John',"age":18,"gender":"male"}

print(person)
# add key-values pair to dictionary
person["address"]="jln.in aja dulu"
print('add key-values pair to dictionary',person)

# update values in dictionary
person['age']=22
print('update values from key age',person)

# remove key-values pair from dictionary
if "gender" in person:
    del person["gender"]

print('remove gender items in dictionaries',person)