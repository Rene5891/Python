file_name = input('Введите имя файла - ')
file_1 = open(file_name, 'r', encoding='utf-8')
#line = file_1.readline()
#while line != '':              
#    print(line.strip())        
#    line = file_1.readline()
#for line in file_1:
#    print(line.strip())
print(file_1.read())
file_1.close()
