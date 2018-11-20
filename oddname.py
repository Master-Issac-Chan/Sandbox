"""Input name and print only odd (number positioned) characters"""

name = input("Enter name: ")
#check name is not blank
while len(name) <= 0:
    print("Invalid name. Please re-enter.")
    name = input("Enter name: ")
    print (name[::2])
    #print odd characters in name using for loop & range
    for i in range(0, len(name), 2):
        print(name[i], end='')