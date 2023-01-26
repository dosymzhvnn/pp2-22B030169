# Loop through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
# Loop throough The index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
# Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]