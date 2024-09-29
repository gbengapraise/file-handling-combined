file = open('Codingal.txt', 'r')
data = file.read()
print(data)
file.close()

file_read = open('Codingal.txt', 'r')
data = file_read.read
print(data)
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write('I am a coding student')
file_write.close()

file_append= open('Codingal.txt', 'a')
file_append.write('I am a loyal coding student')
file_append.close()


file = open('Codingal.txt', 'r')
content = file.read()
split_content = content.split('\n')

print("Lines in the file are:", len(split_content))