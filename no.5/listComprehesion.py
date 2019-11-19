# No.5

#     Array input:
#     [
#     [field1, field2, field2, ... dst],
#     [field1, field2, field2, ... dst],
#     ... dst
#     ]

#     Diproses menjadi string dgn format:
#     field1~field2field2...|field1field2field2~...|... dst

#     Gunakan list comprehesion jika memungkinkan

print()
# opsi pertama
Array = [
    ['field1', 'field2', 'field2'],
    ['field1', 'field2', 'field2']
]
print()
print("list sebelum di proses: ", Array)
hasil = ''.join(''.join(map(str, x)) for x in Array)
print()
print("list sesudah di proses: ",hasil)

print()
# opsi kedua
list =[str(x) for x in input("Enter multiple value: ").split()] 

print("list sebelum di proses: ", list)

result = '-'.join(map(str, list)) 
print()
print("list sesudah di proses: ", result)