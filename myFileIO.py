"""
read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

create (x): This mode creates a file and gives an error if the file already exists.

text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

binary (b): used to handle binary files (images, pdfs, etc).
"""

from PIL import Image

im = Image.open('akash1.jpeg')
im.show()

try:
    f = open('file.txt', 'x')
    f.close()
except:
    print('', end='')

f = open('file.txt', 'w')

f.write('Hello World')
# f.write('My name is Akash Kumar Parida')
f.close()

f = open('file.txt', 'a')

f.write('Akash')

f.close()

f = open('file.txt', 'r')

content = f.read();
print(content)

f.close()

