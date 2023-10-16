

saldo = 6000000
print(f"{'ATM NTB SYARIAH':^20}")
print(20*'=')
print('\n')
pin = int(input("masukkan PIN anda : "))

if pin == 222222:
    print("Selamat Datang di ATM NTB Syariah")
    print('\n')



    while True:
        print(50 * '-')
        print("1. TARIK TUNAI")
        print("2. STOR TUNAI")
        print("3. CEK SALDO")
        print("4. KELUAR")
        print(50 * '-')

        print('\n')
        print(50 * '-')
        opsi_1 = int(input("Masukkan opsi : "))
        if opsi_1 == 1:
            print(50 * '-')
            opsi = int(input("MASUKKAN JUMLAH YANG AKAN DITARIK :"))
            print(opsi)
            print('\n')

            sisa_saldo = saldo - opsi
            print('\n')
            print("SISA SALDO SAAT INI: ",sisa_saldo)
            print(50 * '-')
            print('\n')
            is_done = input("apakah selesai ? (y/n)")
            if is_done == 'y':
                break
            print('\n')

            while True:
                print(50 * '-')
                print("1. TARIK TUNAI")
                print("2. STOR TUNAI")
                print("3. CEK SALDO")
                print("4. KELUAR")
                print(50 * '-')
                print('\n')

                print(50 * '-')
                opsi_1 = int(input("Masukkan opsi : "))
                if opsi_1 == 2:
                    print(50 * '-')
                    opsi_0 = int(input("MASUKKAN JUMLAH YANG AKAN DISTOR : "))
                    print("mengeluarkan sebanyak : ",opsi_0)
                    print('\n')

                    si_saldo =  sisa_saldo + opsi_0
                    print('\n')
                    print(50 * '-')
                    print("SALDO BERTAMBAH MENJADI : ", si_saldo)
                    print('\n')
                    is_done = input("apakah selesai ? (y/n)")
                    if is_done == 'y':
                        break
                    while True:

                        print(50*'-')
                        print("1. TARIK TUNAI")
                        print("2. STOR TUNAI")
                        print("3. CEK SALDO")
                        print("4. KELUAR")
                        print(50*'-')

                        print('\n')
                        print(50*'-')
                        opsi_1 = int(input("Masukkan opsi : "))
                        if opsi_1 == 3:
                            print('\n')
                            print(50 * '-')
                            print("JUMLAH SALDO SAAT INI : ", si_saldo)
                            print('\n')
                            print(50 * '-')
                            is_done = input("apakah selesai ? (y/n)")
                            if is_done == 'y':
                               break

        elif opsi_1 == 2:
            print(50 * '-')
            opsi_0 = int(input("[+] MASUKKAN JUMLAH YANG AKAN DISTOR : "))
            print("~ mengeluarkan sebanyak : ",opsi_0)
            print('\n')

            si_saldo = saldo + opsi_0
            print('\n')
            print(50 * '-')
            print("SALDO BERTAMBAH MENJADI : ", si_saldo)
            print('\n')
            is_done = input("apakah selesai ? (y/n)")
            if is_done == 'y':
                break

            elif opsi_1 == 3:
                print('\n')
                print(50 * '-')
                print("JUMLAH SALDO SAAT INI : ", si_saldo)
                print('\n')
                is_done = input("apakah selesai ? (y/n)")
                if is_done == 'y':
                    break

        elif opsi_1 == 3:
                print('\n')
                print(50 * '-')
                print("JUMLAH SALDO SAAT INI : ", saldo)
                print('\n')
                is_done = input("apakah selesai ? (y/n)")
                if is_done == 'y':
                    break
                print('\n')
                print(50 * '-')
                donw = input("Tekan Enter untuk (keluar) ")
                if donw == 'Enter':
                    break

else:
    print("PIN ANDA SALAH")



print('\n')
print("NTB SYARIAH")



