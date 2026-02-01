# # Activity-1-2-3-4 - File handling/

# open the file in read mode
file_read = open('codingal.txt','r')
print("file in read mode-")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('codingal.txt', 'w')
# write in the file
file_write.write("file in write mode ....")
file_write.write("hi! I am penguin.I am a 1yr old.")
file_write.close()

# open the file in append mode
file_append = open('codingal.txt','a')
# append in the file
file_append.write("/n File in append mode ....")
file_append.write("Hi! I am penguin. I am 1 yr old.")
file_append.close()


# Activity-1
file = open('docmnt1.txt','r')
print("/n read in parts /n")
print(file.read(8))
file.close()

file = open('docmnt1.txt','r')
print("/n Read in parts /n")
print(file.read(8))
file.close()

file = open('docmnt1.txt','a')
file.write("hi! I am a penguin and i am 1 years old.")
file.close()


file1 = open('docmnt1.txt','r')
file2 = open('codingalupdated.txt','w')

for line in file1.readlines():

    if not (line.startswith('coding')):
        print(line) 
        file2.write(line)
file2.close()
file1.close()

#ODD LINE -Activity-4

# Program to copy odd lines of one file to another

# open file in read mode

fn = open('Codingal.txt', 'r')

# open other file in write mode

fn1 = open('CodingalUpdated.txt', 'w')

# read the content of the file line by line

cont = fn.readlines()

type(cont)

for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])

    else:
        pass

# close the file

fn1.close()

# open file in read mode

fn1 = open('CodingalUpdated.txt', 'r')

# read the content of the file

cont1 = fn1.read()

# print the content of the file

print(cont1)

# close all files

fn.close()

fn1.close()
           