def main():
    print("PROGRAM PEMBAGIAN BILANGAN")

    
    try: 
        a = float(input("Masukkan a: "))
        b = float(input("Masukkan b: "))
        hasil = a/b
    except (ZeroDivisionError,ValueError,KeyboardInterrupt):
       print("\nERROR: Anda telah melakukan kesalahan pada inputan") 


    else:
        print("nilai a:", a)
        print("nilai b:", a)
        print("hasil dari a/b:", hasil)


if __name__ == "__main__":
    main()