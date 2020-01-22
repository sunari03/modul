nomor = 0
data = {}
while (True):
    pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:")

    if pilihan == 't':
        while (True):
            nama = input("Nama: ")
            nim = int(input("Nim: "))
            tugas = int(input("Nilai Tugas: "))
            uts = int(input("Nilai UTS: "))
            uas = int(input("Nilai UAS: "))
            akhir = (tugas*.30+uts*.35+uas*.35)
            nomor+=1
            data[nomor] = [nama,nim,tugas,uts,uas,akhir]
            penentu = input("Tambah Data Lagi? (y/t)")
            if penentu == 't':
                break

    elif pilihan == 'l':
        print("Daftar Nilai")
        print("===============================================================")
        print("|  NO  |   NAMA   |  NIM  |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
        print("===============================================================")
        if len(data) == 0:
            print("|                        DATA KOSONG!                         |")
        else:
            for key,list in data.items():
                print("|  {0}   |  {1}   |  {2}  |   {3}   |  {4}  |  {5}  |  {6}    |".format(key,list[0],list[1],list[2],list[3],list[4],list[5]))
        print("===============================================================")

    elif pilihan == 'h':
        print("Hapus Data Mahasiswa")
        print("===============================================================")
        print("|  NO  |   NAMA   |  NIM  |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
        print("===============================================================")
        if len(data) == 0:
             print("|                          DATA KOSONG!                       |")
        else:
            for key,list in data.items():
                print("| {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format(key,list[0],list[1],list[2],list[3],list[4],list[5]))
        print("===============================================================")
        nomor = int(input("Nomor: "))
        if nomor in data:
            del data[nomor]
            print("Data Telah Di Hapus!")
        else:
            print("Nomor Yang Anda Masukkan Salah!")

    elif pilihan == 'u':
        print("Ubah Data Mahasiswa")
        print("===============================================================")
        print("|  NO  |   NAMA   |  NIM  |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
        print("===============================================================")
        if len(data) == 0:
            print("|                     DATA KOSONG!                     |")
        else:
            for key,list in data.items():
                print("| {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format(key,list[0], list[1], list[2], list[3], list[4], list[5]))
        print("===============================================================")
        masnomor = int(input("Nomor: "))
        if masnomor in data:
            nama = input("Masukkan Nama: ")
            nim = int(input("Masukkan NIM: "))
            tugas = int(input("Nasukkan Nilai Tugas: "))
            uts = int(input("Masukkan Nilai UTS: "))
            uas = int(input("Masukkan Nilai UAS: "))
            akhir = (tugas*.30+uts*.35+uas*.35)
            data[masnomor] = [nama,nim,tugas,uts,uas,akhir]
            print("\nData Telah Di Ubah!")
        else:
            print("Nomor Yang Anda Masukkan Tidak Tersedia!")

    elif pilihan == 'c':
        print("Cari Data Mahasiswa")
        masnim = int(input("Masukkan NIM: "))
        for nim in data.values():
            if masnim == nim[1]:
                print("========================================================")
                print("|   NAMA   |  NIM  |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
                print("========================================================")
                print("|  {0}     | {1}   |  {2}    |  {3}  |  {4}  |  {5}    |".format(nim[0],nim[1],nim[2],nim[3],nim[4],nim[5]))
                print("========================================================")

    elif pilihan == 'k':
        break
