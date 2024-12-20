file = open('Sample_File.txt','r')
print(file.read())
file.close()

file = open('Sample_File.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Sample_File.txt','r')
print("\n Reading first line...")
print(file.readline())
file.close()

file = open('Sample_File.txt','r')
print("\n Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Sample_File.txt','r')
print("\n Looping through the lines...")
for line in file:
  print(line)
file.close()