# No. 2

#     Buat script python untuk menentukan apakah suatu bilangan adalah Prima atau Bukan Prima

#     Input: angka x

#     Output:

#     x adalah bilangan prima

#     atau

#     x bukan bilangan prima


x = int(input("Masukkan angka: "))

# bilangan prima harus lebih besar dari 1
if x > 1:
    for i in range(2,x):

        if (x % i) == 0:
            print(x, "bukan bilangan prima")
            break
    else:
        print(x,"adalah bilangan prima")
# bila bilangan kurang atau sama dengan satu
else:
    print(x, "bukan bilangan prima")