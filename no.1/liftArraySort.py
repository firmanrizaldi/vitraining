# No. 1

#     ambil tujuan lantai terdekat terlebih dahulu

#     Misalnya:
#     Jumlah Orang: 4
#     Tujuan Orang 1: Lantai 14
#     Tujuan Orang 2: Lantai 20
#     Tujuan Orang 3: Lantai 5
#     Tujuan Orang 4: Lantai 1
#     Posisi Lift sekarang: 10

#     Maka:
#     Lift bergerak turun ke lantai 5, 1
#     Lalu naik ke lantai 14, 20


#     dikumpulkan besok paling lambat jam 17.00

#     hint : gunakan array sort di Python

# function sort array

def insertionSort(Array):
    for i in range(1, len(Array)):
        j = Array[i]
        k = i - 1
        while k >=0 and Array[k] > j:
            Array[k + 1] = Array[k]
            k -= 1
        Array[k + 1] = j


i = 0

# inputan jumlah orangnya
jmlOrang = int(input("Jumlah orang = "))

# kasih array kosong
Array=[] 

# perulangan untuk menginput tujuan lantainya
# misal jumlah orangnya 7 maka akan mengkinput 7 kali

# kenapa jmlOrang+1 karena index array dimulai dari nol
for i in range(1,jmlOrang+1):

    lantai = int(input("Tujuan orang %i: Lantai = " %i))

    # fungsi membuat inputan lantai jadi sebuah array
    Array.append(lantai)

# input posisi lift
posisiLift = int(input("posisi Lift sekarang = "))

# fungsi untuk membagi array yang kurang dari posisi lift
result = filter(lambda x: x < posisiLift, Array)
print("Lift Bergerak Turun Ke Lantai= ")
print(list(result))

# fungsi untuk membagi array yang lebih dari posisi lift
result = filter(lambda x: x > posisiLift, Array)
print("Lift Bergerak Naik Ke Lantai= ")
print(list(result))




