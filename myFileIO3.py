
with open('myfile1.txt','w') as f:
    f.write('Hello World')
    f.truncate(5) # write only 5 letter from above string

with open('myfile1.txt','r') as f:
    print(f.read())

with open('myfile1.txt','w') as f:
    f.write('12345678910')

with open('myfile1.txt','r') as f:
    f.seek(3) # move the reading position to 3
    print(f.tell()) # tell the reading position
    content = f.read(5) # read 5 letter from reading position
    print(content)

