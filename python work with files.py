


# open('informasiyalaar.txt','w')




# path = 'C:/ygefydgbewygfh/informations.txt'


# open(path,'w')



# path2 = 'C:/ygefydgbewygfh/test.py'

# open(path2,'w')


# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','w')


# file.close()



# file = open('asbfiyhb.txt','w')
# file.write('david kurusskii')



# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','a')

# file.write('\naygy hgduygd')


# file.close()
# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','a')

# file.write('\nbvncbvmvb mcvcb')


# file.close()

# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r')


# file.close()

# try:
#     file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r')
# except FileNotFoundError:
#     print ('bele bir fayl movcud deyil')



# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r')


# for i in file:
#     print(i, end = '')


# file.close()

# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r')

# print(file.read())


# file.close()


# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r')

# readfile1 = file.read()

# print('chitaem 1 raz', readfile1)


# readfile2 = file.read()

# print('chitaem 2 raz', readfile2)


# file.close()



# file = open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r',encoding = 'utf-8')

# siyahi =file.readlines()
# print(siyahi)

# file.close()



# with open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r') as fayl:
#     for i in fayl:
#         print(i)

# fayl.write('davi dkurusskii')




# with open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r') as fayl:
#     fayl.seek()
#     print(fayl.tell())


# with open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r+') as fayl:
#     print(fayl.read())



# with open('C:/ygefydgbewygfh/yeni informasiyalar.txt','a') as fayl:
#     fayl.write("\nElcin suleymanov")





# with open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r+') as fayl:
    
#     fayl_oxu = fayl.read()
#     fayl_oxu ='Vuqar babasli' +fayl_oxu
#     fayl.seek(0)
#     fayl.write(fayl_oxu)
#     print()



with open('C:/ygefydgbewygfh/yeni informasiyalar.txt','r+') as fayl:
    siyahi = fayl.readlines()
    siyahi.insert(3,'vladimir putin')
    fayl.seek(0)
    fayl.writelines(siyahi)

print(siyahi)




















