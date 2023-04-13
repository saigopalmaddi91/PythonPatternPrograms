import os
fname = input("Enter File Name : ")
if os.path.isfile(fname):
    line_count = word_count = char_count = 0
    with open(fname, 'r') as f:
        for line in f:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)
        print("The Total number of lines : ", line_count)
        print("The Total number of words : ", word_count)
        print("The Total number of chars : ", char_count)
else:
    print(f" The given file {fname} doesn't exist... ")

