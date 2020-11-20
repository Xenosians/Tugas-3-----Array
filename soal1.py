arrBerat = []

def hitungMinMax():
    global bMin, bMax
    bMin = min(arrBerat) 
    bMax = max(arrBerat) 
    print (f"Berat Balita Maximum : ", bMax ,"Kg")
    print (f"Berat Balita Minimum : ", bMin , "Kg")

def rerata(arrBerat):
    total = sum(arrBerat)/len(arrBerat) 
    rerata = print("Rerataan nya adalah" , total , "Kg")
    return rerata

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    a = float(input())
    arrBerat.append(a)
hitungMinMax()
rerata(arrBerat)
