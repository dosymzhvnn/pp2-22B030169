# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a range of item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)