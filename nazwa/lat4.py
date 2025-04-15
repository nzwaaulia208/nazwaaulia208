class Siswa:
    SMK = "SMK 4 Tasikmalaya"

    def __init__(self, nama, kelas):
       self.nama = nama
       self.kelas = kelas

    def belajar(self):
        print(f"{self.nama} sedang belajar")
    
    s1 = "Siswa"("nazwa", "X PPLG 1")
    print(s1.nama)
    print(s1.kelas)
    print(s1.smk)
    s1.belajar()
