# while loop

i = 1

while i == 1:
  print(i)

  i = i+1

# For Loop
# hear for gatting odd values you do i is value is 1 then i meas 1 divided by 2 then ans is 0.5 than is not = to 1 than condition is fales yjan i=1 is write
for i in range(0,21):
  if i % 2 ==1:
    print(i)

for i in range (0,21):
  if i % 2 ==0:
   print(i)

# string Data Types along with list

str= ['Hello','World','Pythonprograming']

for i in str:
  print(i)

str= ('Hello','World','Pythonprograming')

for i in str:
  print(i)

name = 'India'

print(type(name))


'''
Note:
    when any function defined inside a class it is called
    "Method of respective class"


'''

# meethods of string

print(name.capitalize())    # camel casing
print(name.casefold())
print(name.lower())         #lower casing
print(name.upper())         #upper casing


date="HEAD"

name=[1,0,5,7,8,9]


name.reverse()
print(name)
name.sort()
print(name)

# sort only for numerical values not alphbatical
str=("A","B","C","D")
print(str.sort())

#------------------------
student =['mayur','kuldeep','riya','divyanshi','abdul']


for index, name in enumerate(name):
  print(f"index: {index}, name: {name}")

  '''
index: 0, name: mayur
index: 1, name: kuldeep
index: 2, name: riya
index: 3, name: divyanshi
index: 4, name: abdul
'''