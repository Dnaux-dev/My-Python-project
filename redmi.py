# functions in python
#List Comprehension
#Arithmetics
#Dictionaries, set, lists and tuples
#Args and kwargs
#comparisons in python
#logical operators
#Datatypes
#concatenation
#string formatting 
#Loops

List = ["Ade","Bola","Adebayo","Clement","Daniel","Adele","Bayo"]
# def filter_words(word_list,letter):
#    return filter(lambda word:word[0]==letter,word_list)
# print(filter_words(List,'A'))


# def startswithA(num):
#  for i in num:
#   if i.startswith("A"):
#    print(i)

# print(startswithA(List))


def Fibonacci(n):
 if n <0:
  print("Incorrect input, enter a positive integer")
 elif n ==0:
  return 0
 elif n == 1 or n ==2:
  return 1
 else:
  return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input("How many terms?"))

i = 0
for i in range(n):
 print(Fibonacci(i))

