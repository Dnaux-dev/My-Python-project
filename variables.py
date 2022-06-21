name = "Daniel"
age = 23
height = "3m"

msg = "hello my name is " + name + " and I'm " + str(age) + " my current height is" + height
print(msg)

msg2 = "hello my name is {} and I'm {}, my current height is {}". format(name,age,height)
print(msg2)

""" Taking user input"""
name = input ("What is your name?")
print("hello", name)