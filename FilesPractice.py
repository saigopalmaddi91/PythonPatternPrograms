# Opening a file

f = open('abc.txt', 'w')
# 7 modes :  r - read(default), w - write, a - append, r+ - read and write, w+ - write and read, a+ - append and read,
# x - exclusive
print("File Name : ", f.name)
print("File Mode : ", f.mode)
print("Is File Closed: ", f.closed)
print("Is file readable : ", f.readable())
print("Is file writable : ", f.writable())

f.write("This is a Sample Text File \n")
f.write("This is written using python program \n")

l = ["Apple", "Banana", "Cherry", "Kiwi"] # We can take tuple, set and dict (Only keys will be added, Keys should be string type) also

f.writelines(l)

f = open("abc.txt", "r")

print("f.read() method : ", f.read())
print("f.read(n) method : ", f.read(10))
print("f.readline() method : ", f.readline())
print("f.readlines() method : ", f.readlines())

f.close()
print("Is File Closed : ", f.closed)
