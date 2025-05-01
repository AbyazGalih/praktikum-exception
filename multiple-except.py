def main():
    print("PROGRAM PEMBAGIAN BILANGAN")

    
    try: 
        a = float(input("Masukkan a: "))
        b = float(input("Masukkan b: "))
        hasil = a/b
    except ZeroDivisionError:
       print("\nERROR: Nilai b tidak boleh nol") 

    except ValueError:
       print("\nERROR: a dan b harus berupa angka")

    except KeyboardInterrupt:
       print("\nERROR: jangan tekan CTRL +C")

    else:
        print("nilai a:", a)
        print("nilai b:", a)
        print("hasil dari a/b:", hasil)


if __name__ == "__main__":
    main()