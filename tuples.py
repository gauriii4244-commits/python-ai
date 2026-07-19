# tup = ("Samruddhi","Aarya","Sneha")
# print(tup[0])
# print(tup.index("Samruddhi"))
# print(tup.count("Samruddhi"))

# #practice questions 
# #Q1. Create a tuple of 5 of your favorite colors, and print the whole tuple.
color = ("Pink","Blue","Yellow","Red","Brown")
print(color)

#Q2. Print the first and last item of that tuple using indexing.
print(color[0])
print(color[4])

# #Q3. Try to change one item in the tuple (e.g., colors[0] = "Purple") and see what happens — read the error carefully.
# color[0]="Purple"
# print(color)#doesn't support item assignments 

print("Pink" in color)   # True
print("Purple" in color) # False
print("Orange " in color)

tupl = (1,2,3,4,5)
print(tupl)
new_list = list(tupl)
print(new_list)
new_list[2]=5
print(new_list)

tup1 = (1,2,3)
tup2 = (4,5,6,)
print(tup1 + tup2)

tup3 = (1, 2, 2, 3, 2, 4)
print(tup3.count(2))

new_tup = ("sam",19,87.8,True)
print(type(new_tup[0]))
print(type(new_tup[2]))
print(type(new_tup[3]))
print(type(new_tup[1]))

a,b,c = (1,2,3)
print(a)
print(b)
print(c)