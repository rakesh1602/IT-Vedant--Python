# Q1.write a code to add a element 'eleven' , inside list at the end
x=[2,4,6,8,10]
x.append("eleven")
print(x)

# Q2.perform an operation to get the following output
x.insert(0,"one")
print(x)

# Q3.perform an operation to merge the list y inside list x
y=[12,13,14]
x.extend(y)
print(x)

#Q4.perform an operation to get the following output output-: [14, 13, 12, 'eleven', 10, 8, 6, 4, 2, 'one']
x.reverse()
print(x)

#Q5.Perform one single operation to remove 'eleven', 10, 8 all together at once
del x[3:8]
print(x)

#  Q6.write a code to remove 'one' element from the list
x.pop(-1)
print(x)

# Q7.write a code to get the following output
x =["hey","there","hello","world"]
y= " "

print(y.join(x))




