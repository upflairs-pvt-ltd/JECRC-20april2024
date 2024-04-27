import os 
# print(os.getcwd())
# C:\Users\Ranjit\Desktop\JECRC-20april2024
# print(os.listdir())
# ['.git', 'day5.py', 'day6.py', 'day7.py', 'jecrc.py', 'README.md', 'test.py', '__pycache__']
# os.mkdir("JECRC")
os.makedirs("JECRC2" , exist_ok=True)
path_var = r"C:\Users\Ranjit\Desktop\JECRC-20april2024\JECRC"
os.chdir(path_var)
print(os.getcwd())

# open('test.txt','x')
# file = open('test.txt','w') 
# data = "Hello we are from jecrc"
# data2 = "Hello jecrc"
# file.write(data2)

# file = open('test.txt','r')
# data = file.read()
# file.close()
# print(data)

open('test.txt')