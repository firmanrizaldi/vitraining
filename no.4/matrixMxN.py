# No.3

#     Buat script input matrix MxN

#     Tentukan berapa jumlah bilangan positif dan negatif didalam matrix tsb dan tampilkan isi matrix


print("Hitung Positif dan Negatif dari Matrix")
print()

R = int(input("Masukan baris :")) 
C = int(input("Masukan kolom :")) 
  
# Initialize matrix 
matrix = [] 
jml = R*C
print ("Masukan angka sebanyak", jml)

a = 1
# For user input 
for i in range(R):          # A for loop for row entries 
    angka =[] 
    
    for j in range(C):      # A for loop for column entries 
         angka.append(int(input("angka ke %a: " %a))) 
         a = a+1
    matrix.append(angka) 

pos_count, neg_count = 0, 0
num = 0
s = 0

for s in range(R):
    for num in matrix[s]:  
        # checking condition 
        if num >= 0: 
            pos_count += 1
  
print() 
neg_count = jml - pos_count  

print("angka positf ada: ", pos_count) 
print("angka negatif ada: ", neg_count) 
print() 

print("tampilan Matrik :") 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 