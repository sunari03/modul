data=[]
while(True):
    nama=input("Nama : ")
    nim=input("Nim  : ")
    tugas=int(input("Nilai Tugas :"))
    uts=int(input("Nilai UTS :"))
    uas=int(input("Nilai UAS:"))
    akhir = (30 * tugas / 100) + (35 * uts / 100) + (35 * uas / 100)
    data.append([nama, nim, tugas, uts, uas, akhir])
    ulangi=input("Tambah data (y/t)?")
    if ulangi.lower() == 't':
        break;

print("\nDaftar nama\n")
print("========================================================================")
print("|  Nama  |   Nim    |   Tugas  |    UTS   |    UAS     |     Akhir     |")
print("========================================================================")
for x in data:
 print("|{0:8s}|{1:10s}|{2:10d}|{3:10d}|{4:12d}|{5:15f}|".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print("========================================================================")
