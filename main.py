#No1
'''try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred", "due to zero division")'''
#No2
'''try:
    variable = 10
    print(variable / 0)
    print(variable + "hello")
    
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Type is error checked by Fahim")'''

#No3
'''try:
    word = "spam"
    print(word / 0)
except:
   print("An error occurred")'''

#No4
'''try:
    print("Hello")
    print("sm" / 0)

except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")'''

#No5
'''try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last")'''

#No6

'''print(1)
raise ValueError
print(2)'''

#No7
'''name = "123"
raise NameError("Invalid name!") '''

#No8
'''try:
    num = 5 / 0
except:
    print("An error occurred")
    raise'''

#No9
'''print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)'''

#No10
''''temp = -10
assert (temp >= 0), "Colder than absolute zero!"
print(temp)'''

#No11
'''myfile = open("filename.txt")'''

'''letters = ['p', 'q', 'r', 's', 'p', 'u']
letters.remove('q')
print(letters)'''

'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break'''

