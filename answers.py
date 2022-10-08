#directory:   /home/imtiaz/code.py
text_file = open('file.txt','r')

#Another method using full location
text_file2 = open('/home/imtiaz/file.txt','r')
print('First Method')
print(text_file)

print('Second Method')
print(text_file2)