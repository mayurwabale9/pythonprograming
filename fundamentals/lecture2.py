# concept of print function 

# f- string


name='mayur'
age=19
salary=50000

print (f'hii my name is {name} and my age is {age} and my salary is {salary}')
print ('hii my name is {} and my age is {} and my salary {} is '.format(name,age,salary))



# concept of list 
lst1 = []
lst = [1,2,3,32.45,'hiii','world',True,False,[10,20,30],[100,200,300],{1,2,3},]



# if conditon


name = input("enter your name : ")

if name == "mayur":
    print(f"your name is {name}")


coin_side = input('enter the coin side :')

if coin_side =="head":
    print("you win the game")

else:
    print("you loss the game")


coin_side = input("enter the coin side")

if coin_side.lower() == "head":
    print(f"you win yhe game")


if coin_side.lower() == "tail":
    print("I win yhe game")


else:
    print("enter the correct coin side")


# %%
# concept of Indexing and slicing 
 
str = "welcome to the world python programing"
str1 = "Hello World"
# %%
print(str[4])


# str[start:stop:step]
# %%
print(str1[::2])
# %%


'''
quation :
write a program to print wether the value entered by user is palindrome or not

logic:
1.ask user to enter string 
2.reverse the string 
3.compar the original string with the reverse string 
4.if both are same then it is palindrome otherwise it is not palindrome 

'''
# %%
string = input("enter a string : ")
string1=string[::-1]  # str1[start:stop:step]  : --> -1 means reverse the string

if string == string1:
    print(f"{string} is a palindrome")

else:
    print(f"{string} is not a palindrome")
# %%
