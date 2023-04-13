import zipfile

f = zipfile.ZipFile('files_zipped.zip', 'w', zipfile.ZIP_DEFLATED)  # Zip Operation
f.write('abc.txt')
f.write('emp.csv')
f.write('input.txt')

print("Files Zipped Successfully!!!")

# Unzip Operation

f = zipfile.ZipFile('files_zipped.zip', 'r', zipfile.ZIP_STORED)
names = f.namelist()
print(names)
for name in names:
    f1 = open(name, 'r')
    text = f1.read()
    print("File Name : ", name)
    print("Content : ", text)
    f1.close()
    print()
