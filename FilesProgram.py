f = open("input.txt", 'w')
f.write("ALL STUDENTS ARE LAZY")

with open("input.txt", 'r+') as f:
    text = f.read()
    print("Data before Modification : ")
    print(text)
    print("The current cursor position is : ", f.tell())
    f.seek(17)
    f.write("NERDS!!!")
    f.seek(0)
    text = f.read()
    print("Data After Modification : ")
    print(text)