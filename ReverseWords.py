# WAP to reverse order of words

s = input("Enter Input Sentence to reverse the order of words : ")

words = s.split()
print("The words are : ", words)
words = words[::-1]
print("Reversed words String is : ", ' '.join(words))

'''
Enter Input Sentence to reverse the order of words : I am Learning Python
The words are :  ['I', 'am', 'Learning', 'Python']
Reversed words String is :  Python Learning am I

'''