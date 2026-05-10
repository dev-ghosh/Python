from operator import truediv  ##taking input
# name=input("what is your name ? ")
# fav_clr = input("what is your favorite color ? ")
# print(name+" likes "+fav_clr)
  ##type conversion
# birth_year=input("birth year")
#      #age=2026-birth_year will be wrongg
# age=2026-int(birth_year)
# print(age)
  ##string
# course= "python for beginners"
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[:]) #can be used for cloning
# print(course[1:])
# another=course[:]
# print(another)
# name="jennifer"
# print(name[1:-1])
  ##formatted strings
# first="john"
# last="smith"
# msg=f"{first} [{last}] is a coder"
# print(msg)
  ##if-else
is_hot= False
is_cold= False
if is_hot:
    print("its a hot day")
    print("drink plenty of water")
elif is_cold:
    print("its a cool day")
    print("wear warm clothes")
else:
    print("its a lovely day")

print("enjoy your day") #this will be printed irrrespective of true false

