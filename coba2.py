# TYPEERROR
try:
    jumlah = 5 + "10"
except TypeError:
    print("Terjadi TypeError, pastikan Anda menjumlahkan dua angka.")

# FILENOTFOUNDERROR
try:
    file = open('file_tidak_ada.txt')
except FileNotFoundError:
    print("File tidak ditemukan. Pastikan Anda memasukkan path yang benar.")

# ZERODIVISIONERROR
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Anda mencoba membagi dengan nol. Ini tidak dapat dilakukan.")
