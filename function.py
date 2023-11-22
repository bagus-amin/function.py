#NO 1 Profil
    #Deklarasi
def profil(nama, alamat, gender, umur, hobi):
    print("Nama:", nama)
    print("Alamat:", alamat)
    print("Gender:", gender)
    print("Umur:", umur)
    print("Hobi:", hobi)
    #pemanggilan
profil("Bam","bogor","Laki-laki","19tahun","Membaca")
#NO 2 NILAI KELULUSAN
    
    #Deklarasi
def cek_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

    #Pemanggilan 
nilai_mahasiswa = 90
status_kelulusan = cek_kelulusan(nilai_mahasiswa)
print("Status Kelulusan:", status_kelulusan)
#NO 3
def cetak_ganjil(batas):
    for nilai in range(1, batas + 1, 2):
        print(nilai)

# Pemanggilan 
cetak_ganjil(100)
