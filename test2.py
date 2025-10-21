def x():
    data = []
    print("SCORE SEPAK BOLA HARI INI")
    while True:
        n1 = input("Nama Tim Pertama: ")
        n2 = input("Nama tim Kedua: ")
        
        s1 = input("Skor Untuk Tim Pertama:")
        s2 = input("Skor Untuk Tim Kedua:")
        
   
        if s1 > s2:
            ex = print(f"Kemenangan diraih oleh {n1} dengan skor {s1}")
            data.append(n1)        
        elif s2 > s1:
            fx = print(f"Kemenangan diraih oleh {n2} dengan skor {s2}")
            data.append(n2)
        pilih = input("Apakah ingin melanjutkan mengisi data skor? (y/n)")
        if pilih.lower() == "n":
            break
        
    print("---Semua Data Kemenangan Di Turnamen Ini---")
    for i in data:
        print(i)
x()