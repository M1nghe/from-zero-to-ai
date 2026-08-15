#List = [] ordered and changeable. Duplicates OK
#Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#Tuple = () ordered and unchangeable. Duplicates OK. Faster



scores = [85,92,78,60,95]

scores.append(99)
scores.remove(92)
scores[0]=28
first = scores[0]
last=scores[-1]
length = len(scores)

#for i,score in enumerate(scores):
#    print(f"第{i+1}个成绩:{score}")

#divisible_by_3 = [n for n in range(1,101) if n%3 ==0]
#print(divisible_by_3)


"""PRA1
lista = [1,2,3,4,5]
list2a = [2*x for x in lista]
print(list2a)"""

"""Pra2
list = [3,7,1,9,4,6,8]
new_list = [x for x in list if x>5]
print(new_list)
"""

#Pra3
lst = [85,92,78,95,88,76,90]
"""sum=0
for i in list:
    sum = i + sum"""
total_score = sum(lst)
print(total_score/len(lst))
      









"""
fruits = ["orange",'apple','pineapple','kiwi']

#print(dir(fruits))
#print(help(fruits))

#print(fruits[1:3])
#for fruit in fruits:
#    print(fruit)
#print(len(fruits))
#print('apple' in fruits)

#fruits[0]='mango'
#fruits.sort()
#fruits.reverse()
#fruits.append('melon')
#fruits.insert(2,'pear')
#fruits.remove("apple")
#print(fruits.index("apple"))
print(fruits)
"""