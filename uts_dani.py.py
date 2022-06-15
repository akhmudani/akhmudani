# Aplikasi Pembelian Handphone
print("_____Login_____")
nama = input("Username : ")
pw = input("Password : ")
Nama1 = input("Masukan Nama Pembeli : ")
print()
print("Selamat Datang di MStore Pamekasan")
print("Daftar Menu :")
daftar1 = ["Vivo X50 pro","Vivo X50","Vivo V20","Vivo V20 SE","Vivo V19"]
daftar2 = ["Vivo V17 Pro","Vivo V15 Pro","Vivo V11 pro","Vivo Y50","Vivo Y30"]
daftar3 = ["Vivo Z1 Pro","Vivo S1 Pro","Vivo S1","Vivo Y12","Vivo Y91"]
print("Daftar 1 : ",daftar1,"\nDaftar 2 : ",daftar2,"\nDaftar 3 : ",daftar3)
jawab = 'ya'
while jawab == 'ya' :
    pilbar = input("Pilih barang : ")
    if pilbar == 'Vivo X50 pro' :
        Harga = 9999000
        print("Vivo X50 pro : ",Harga,"\nPilihan Warna :\n 1. Glaze Black\n 2. Frost Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo X50' :
        Harga = 6999000
        print("Vivo X50 : ",Harga,"\nPilihan Warna :\n 1. Alpha Grey\n 2. Glaze Black")
        warna = input("Pilihan warna : ")
    elif pilbar == 'Vivo V20' :
        Harga = 4999000
        print("Vivo V20 : ",Harga,"\nPilihan Warna :\n 1. Gravity Black\n 2. Oxygen Blue")
        warna = input("Pilihan warna : ")
    elif pilbar == 'Vivo V20 SE' :
        Harga = 3999000
        print("Vivo V20 SE : ",Harga,"\nPilihan Warna :\n 1. Gravity Black\n 2. Oxygen Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo V19' :
        Harga = 3999000
        print("Vivo V19 : ",Harga,"\nPilihan warna :\n 1. MoonStone SWhite\n 2. Ocean Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo V17 Pro' :
        Harga = 4999000
        print("Vivo V17 Pro : ",Harga,"\nPilihan Warna :\n 1. Satin Black\n 2. Silk White")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo V15 Pro' :
        Harga = 4999000
        print("Vivo V15 Pro : ",Harga,"\nPilihan Warna :\n 1. Topas Blue\n 2. Coral Red")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo V11 pro' :
        Harga = 3499000
        print("Vivo V11 pro : ",Harga,"\nPilihan Warna :\n 1. Glamour Red\n 2. Royal Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo Y50' :
        Harga = 3299000
        print("Vivo Y50 : ",Harga,"\nPilihan Warna :\n 1. Starry Black\n 2. irish Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo Y30' :
        Harga = 2799000
        print("Vivo Y30 : ",Harga,"\nPilihan Warna :\n 1. Emerald Black\n 2. Moonstone White")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo Z1 Pro' :
        Harga = 3499000
        print("Vivo Z1 Pro : ",Harga,"\nPilihan Warna :\n 1. Black\n 2. Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo S1 Pro' :
        Harga = 3699000
        print("Vivo S1 Pro : ",Harga,"\nPilihan Warna :\n 1. Glowing Black\n 2. Crystal Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo S1' :
        Harga = 2499000
        print("Vivo S1 : ",Harga,"\nPilihan Warna :\n 1. Cosmic Green\n 2. Skyline blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo Y12' :
        Harga = 1999000
        print("Vivo Y12 : ",Harga,"\nPilihan Warna :\n 1. Burgundy Red\n 2. Aqua Blue")
        warna = input("Pilihan Warna : ")
    elif pilbar == 'Vivo Y91' :
        Harga = 1799000
        print("Vivo Y91 : ",Harga,"\nPilihan Warna :\n 1. Starry Black\n 2. Aqua Blue\n 3. Sunset Red")
        warna = input("Pilihan Warna : ")
    else :
        print("Silahkan Masukan Pilihan Yang Benar")
    print()
    jumbar = int(input("Masukan jumlah Barang yang dibeli : "))
    bayar = jumbar * Harga
    print("Jumlah Yang Harus Dibayar : Rp.",bayar)
    pembayaran = int(input("Masukkan Pembayaran : "))
#Struk Pembayaran
    print()
    print("=".center(30, "="))
    print(" STRUK PEMBAYARAN ".center(30, "="))
    print("= MStore Pamekasan ".center(30, "="))
    print("Admin        : ", nama, "\nNama Pembeli : ", Nama1)
    print(".".center(30, "."),"\n")
    print("Nama Barang     : ", pilbar)
    print("Warna Barang    : ", warna)
    print("Harga Satuan    :  Rp.", Harga)
    print("Jumlah Barang   : ", jumbar)
    if bayar > 5000000:
        bonus = bayar * 20/100
        total = bayar - bonus
        print("Bonus           :  20%")
        print("".center(28, "-"), "+")
        print("Total Pembayaran : Rp.", bayar - bonus)
        print("".center(30, "-"))
        print("Tunai            : Rp.", pembayaran)
        print("Kembalian        : Rp.", pembayaran - total)
        print(" TERIMAKASIH ".center(30, "="))
        print(" ATAS KUNJUNGANNYA ".center(30, "="))
    else:
        print("".center(28, "-"), "+")
        print("Total Pembayaran : Rp.", bayar)
        print("".center(28, "-"))
        print("Tunai            : Rp.", pembayaran)
        print("Kembalian        : Rp.", pembayaran - bayar)
        print()
        print(" TERIMAKASIH ".center(30, "="))
        print(" ATAS KUNJUNGANNYA ".center(30, "="))
        print("=".center(30, "="))
    jawab = str(input("mau beli lagi ? : "))

print()


