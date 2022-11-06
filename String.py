string="Python Programming"
stringTwo= "I love PYTHON programming"
print(string)

#Type and length
print(type(string))
print("Length of sting is :",   len(string))

#Indexing
print("Inde of :", string[14])
print("Inde of :", string[-3])

#Slicing
print("slicing ", (string[0:5]))
print("slicing till last index ", (string[7:]))
print("with step size ",string[0:23:2])
print("Slicing ", string[0:6:1])
print("slicing ", stringTwo[6:13:])
print("reverse order ", stringTwo[::-1])

#Reverse order
print("reverse order ", string[-1::-1])
print("reverse order ", string[::-1])


#Mathematical operations
# + = concatation
# *  = multiple copies

s1="Python"
s2="Programming"

print(" After concatation : ",s1+" "+s2)
print("After mulitple copies : ",s1*4)

#Removing Spaces
s3="     Hello Peoples     "
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())


#Finding substring
#find
'''
print(s3.find("hello"))
print(s3.find("pk",4,-1))

#index
print(s3.index("hello"))
print(s3.index("pk",4,-1))
'''

#Count
s4="SDSDGFDHDHHDFGDFDHD"
print("Occurances of ",s4.count("D"))

#String is immutable
s4="python"
#s4[0]="P"

#Replace
print(s4)
print("After repalcing: ",s4.replace("python","java"))

#Split
stringThree= "I love python@gmail.com"
print("after split : ", stringTwo.split(" "));
print("after split : ", stringThree.split("@"));
print("after split : ", stringThree.split("v"));

#Join
list=["I","Love","Python"]
newList="**".join(list)
print(newList)


#Changing cases of string
#Upper
print(stringTwo.upper())
#Lower
print(stringTwo.lower())
#Swapcase - upper to lower, lower to upper
print(stringTwo.swapcase())
#Title 
print(stringTwo.title())
#Capitalize
print(stringTwo.capitalize())

#To Check type of data in string
s5="abc123"
s6="$$#%%##"
s7="1234"
s8="PYHTON"
s9="python"
print(s5.isalnum())
print(s6.isalnum())
print(s6.isalpha())
print(s7.isdigit())
print(s8.islower())
print(s9.isupper())


#format a string
name="Rakesh"
age=24
print("mu name is {}, mu age is {} ".format(name,age))
print("mu name is {1}, mu age is {0} ".format(name,age))
print(f"Hello {name}, your age is {age}")

#Escape sequnce \n
s10="Python\nprogramming"
print(s10)
