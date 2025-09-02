# Write your solution here
list = []
i = int(input("New item: "))
while i != 0:
    
    list.append(i)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")
    i = int(input("New item: "))

print("Bye!")


