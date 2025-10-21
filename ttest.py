panjang = int(input("Masukkan nilai panjang: "))
lebar = int(input("Masukkan nilai lebar: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)


if  luas >= keliling:
    print(f"luas {luas} lebih besar dari keliling {keliling} adalah rumah")
    
else:
    print(f"keliling {keliling} lebih besar dari luas {luas} adalah hotel")
