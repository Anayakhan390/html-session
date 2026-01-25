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