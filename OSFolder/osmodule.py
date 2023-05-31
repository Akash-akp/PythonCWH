import os
if not os.path.exists('dta'):
    os.mkdir('dta')
if not os.path.exists('data'):
    os.mkdir('data')
folder = os.listdir()
print(folder)
print(os.getcwd())
os.chdir("dta")
print(os.getcwd())
os.chdir('../')

for i in range(0,100):
    if not os.path.exists(f'data/Tutorial {i+1}'):
        os.mkdir(f'data/Tutorial {i+1}')
    else:
        os.rmdir(f'data/Tutorial {i+1}')

if not os.listdir('data'):
    os.rmdir('data')

