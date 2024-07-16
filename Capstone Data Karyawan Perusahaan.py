# Program Data Karyawan Perusahaan
from prettytable import PrettyTable

# Data Karyawan Perusahaan menggunakan dictionary di dalam list(karena mempermudahkan untuk pemanggilan key lebih)
karyawan = [
    {'Nama': 'Subhan Paphu', 'ID_Karyawan': 'ID-001', 'Departemen': 'Operasional', 'Jabatan': 'Manager Operasional', 'Tanggal_Bergabung': '2 Januari 2024', 'Gaji_Bulanan(RP)': 15000000},
    {'Nama': 'Sugand Mukti', 'ID_Karyawan': 'ID-002', 'Departemen': 'Keuangan', 'Jabatan': 'Kepala Keuangan', 'Tanggal_Bergabung': '20 Juni 2024', 'Gaji_Bulanan(RP)': 13000000},
    {'Nama': 'Nazil Ramadhan', 'ID_Karyawan': 'ID-003', 'Departemen': 'Keuangan', 'Jabatan': 'Akuntan', 'Tanggal_Bergabung': '13 April 2024', 'Gaji_Bulanan(RP)': 9000000},
    {'Nama': 'Fikri AR', 'ID_Karyawan': 'ID-004', 'Departemen': 'Eksplorasi', 'Jabatan': 'Geolog', 'Tanggal_Bergabung': '8 Januari 2024', 'Gaji_Bulanan(RP)': 8000000},
    {'Nama': 'Raul Aditya', 'ID_Karyawan': 'ID-005', 'Departemen': 'Teknik', 'Jabatan': 'Insinyur Pertambangan', 'Tanggal_Bergabung': '24 Maret 2024', 'Gaji_Bulanan(RP)': 10000000}
]


# Fungsi untuk menampilkan Data Karyawan Perusahaan (READ)
def READData(karyawan): 
    while True :
        print('\n\n\t    ========= READData =========')
        print('----------------------------------------------------')
        print('1. Tampilkan Seluruh Data Karyawan')
        print('2. Data Karyawan Tertentu')
        print('3. Data Karyawan Berdasarkan Nama')
        print('4. Data Karyawan Berdasarkan Departemen')
        print('5. Data Karyawan Berdasarkan Jabatan ')
        print('6. Data Karyawan Rentang Gaji Bulanan')
        print('7. Kembali ke Menu Utama')
        print('----------------------------------------------------\n')
        read = input('Masukkan Pilihan Submenu Anda (1-7):')



        if read == '1':                                
            if len(karyawan) != 0:
                print('\nDaftar Data Karyawan')
                

                def getNama(karyawan):
                    return karyawan['Nama']
                sorted_karyawan = sorted(karyawan, key=getNama)


                table = PrettyTable()
                table.field_names = ['No', 'Nama', 'ID_Karyawan', 'Departemen', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']


                for i, detail in enumerate(sorted_karyawan, 1):
                    table.add_row([i, detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                print(table)
            else:
                print('Tidak ada Data Karyawan yang tersedia.')



        elif read == '2':
            if len(karyawan) != 0:
                while True:
                    id_karyawan = input('\n\nMasukkan ID Karyawan yang ingin dicari (format : ID-000) : ').upper()
                    if len(id_karyawan) == 6 and id_karyawan[:3] == 'ID-' and id_karyawan[3:].isdigit():
                        detail = None
                        for i in karyawan:
                            if i ['ID_Karyawan'].upper() == id_karyawan:
                                detail = i
                                break


                        if detail:
                            table = PrettyTable()
                            table.field_names = ['Nama', 'ID Karyawan', 'Departemen', 'Jabatan', 'Tanggal Bergabung', 'Gaji Bulanan(RP)']
                            table.add_row([detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                            print(table)
                        else:
                            print('Data Karyawan dengan ID tersebut tidak ditemukan.')
                        break


                    else:
                        print('ID Karyawan tidak sesuai Format. (format : ID-000) Silakan input kembali...')
            else:
                print('Tidak ada Data Karyawan yang tersedia.')



        elif read == '3':
            if len(karyawan) != 0:
                nama = input('Masukkan Nama Karyawan yang ingin dicari : ').strip().lower()
                filtered_karyawan = [i for i in karyawan if nama in i['Nama'].lower()]


                if filtered_karyawan:
                    print(f'\nData Karyawan dengan Nama yang cocok dengan "{nama}"')
                    table = PrettyTable()
                    table.field_names = ['No', 'Nama', 'ID_Karyawan', 'Departemen', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']


                    for i, detail in enumerate(filtered_karyawan, 1):
                        table.add_row([i, detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                    print(table)


                else:
                    print(f'\nTidak ada Karyawan dengan Nama yang cocok dengan "{nama}". Silakan input kembali...')
            else:
                print('Tidak ada Data Karyawan yang tersedia...')



        elif read == '4':
            if len(karyawan) != 0:
                departemen = input('Masukkan Bagian Nama Departemen yang ingin ditampilkan : ').strip().lower()
                filtered_karyawan = [i for i in karyawan if departemen in i['Departemen'].lower()]


                if filtered_karyawan:
                    print(f'\nData Karyawan dengan Departemen yang mengandung "{departemen.capitalize()}" ')
                    table = PrettyTable()
                    table.field_names = ['No', 'Nama', 'ID_Karyawan', 'Departemen', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']
                    

                    for i, detail in enumerate(filtered_karyawan, 1):
                        table.add_row([i, detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                    print(table)


                else:
                    print(f'\nTidak ada Karyawan dengan Departemen yang mengandung "{departemen.capitalize()}". Silakan input kembali...')
            else:
                print('Tidak ada Data Karyawan yang tersedia.')




        elif read == '5':
            if len(karyawan) != 0:
                jabatan = input('Masukkan Awal Jabatan yang ingin ditampilkan : ').strip().lower()
                filtered_karyawan = [i for i in karyawan if i['Jabatan'].lower()  [:len(jabatan)] == jabatan]


                if filtered_karyawan:
                    print(f'\nData Karyawan dengan Jabatan yang dimulai dengan "{jabatan.capitalize()}" ')
                    table = PrettyTable()
                    table.field_names = ['No', 'Nama', 'ID_Karyawan', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']


                    for i, detail in enumerate(filtered_karyawan, 1):
                        table.add_row([i, detail['Nama'], detail['ID_Karyawan'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                    print(table)


                else:
                    print(f'\nTidak ada Karyawan dengan Jabatan yang dimulai dengan "{jabatan.capitalize()}". Silakan input kembali.')
            else:
                print('Tidak ada Data Karyawan yang tersedia.')



        elif read == '6':
            if len(karyawan) != 0:
                while True:
                    try:
                        min_gaji = int(input('Masukkan Minimal Gaji Bulanan yang ingin ditampilkan : '))
                        max_gaji = int(input('Masukkan Maksimal Gaji Bulanan yang ingin ditampilkan : '))
                        if min_gaji >= 0 and max_gaji >= 0 and min_gaji <= max_gaji:
                            filtered_karyawan = [item for item in karyawan if min_gaji <= item['Gaji_Bulanan(RP)'] <= max_gaji]


                            if filtered_karyawan:
                                print(f'\n\nData Karyawan dengan Rentang Gaji Bulanan antara {min_gaji} dan {max_gaji} :')
                                table = PrettyTable()
                                table.field_names = ['No', 'Nama', 'ID_Karyawan', 'Departemen', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']


                                for i, detail in enumerate(filtered_karyawan, 1):
                                    table.add_row([i, detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                                print(table)


                            else:
                                print(f'Tidak ada Karyawan dengan Rentang Gaji Bulanan antara {min_gaji} dan {max_gaji}. Silakan input kembali...')
                            break
                        else:
                            print('Pastikan Minimal Gaji tidak lebih Besar dari Maksimal Gaji dan Angka yang dimasukkan tidak Minus.')

                    except ValueError:
                        print('Input tidak valid. Pastikan memasukkan Angka untuk Gaji Bulanan.')

            else:
                print('Tidak ada Data Karyawan yang tersedia.')



        elif read == '7':
            break
        else:
            print('Pilihan tidak valid, Silakan input dengan Benar.')



# Fungsi Untuk Menambahkan Data Karyawan Perusahaan (CREATE)
def CREATEData(karyawan):
    while True :
        print('\n\n\t========= CREATEData =========')
        print('----------------------------------------------')
        print('\t   1. Tambah Data Karyawan')
        print('\t   2. Kembali ke Menu Utama')
        print('----------------------------------------------\n')
        read = input('Masukkan Pilihan Submenu Anda (1-2):')



        if read == '1':
            try:
                while True:
                    id_karyawan = input('Masukkan ID Karyawan (format : ID-000) : ').upper()
                    if len(id_karyawan) == 6 and id_karyawan[:3] == 'ID-' and id_karyawan[3:].isdigit():


                        if id_karyawan == 'ID-000':
                            print('ID Karyawan tidak boleh ID-000. Silakan input ID yang lain...')
                            continue
                        # Menghindari ID Karyawan ID-000


                        id_jika_ada = False
                        for i in karyawan:
                            if i ['ID_Karyawan'] == id_karyawan:
                                id_jika_ada = True
                                break
                        # Memeriksa apakah ID karyawan sudah ada dengan menggunakan for loop


                        if id_jika_ada:
                            print('ID Karyawan sudah ada. Silakan input ID yang lain...')
                        else:
                            break
                    else:
                        print('ID Karyawan tidak sesuai Format. (format : ID-000). Silakan input kembali...')


                nama = input('Masukkan Nama Karyawan : ')
                departemen = input('Masukkan Departemen : ')
                jabatan = input('Masukkan Jabatan  : ')
                tanggal_bergabung = input('Masukkan Tanggal Bergabung (format : 1 Januari 2024): ')


                while True:
                    try:
                        gaji_bulanan = int(input('Masukkan Gaji Bulanan (RP): '))
                        if gaji_bulanan > 0:
                            break
                        else:
                            print('Gaji Bulanan harus lebih dari 0 tidak boleh minus. Silakan input kembali...')

                    except ValueError:
                        print('Input tidak valid. Pastikan memasukkan angka untuk Gaji Bulanan.')


                print('\nData Karyawan Berhasil di Tambahkan!\n')
                table = PrettyTable()
                table.field_names = ['Nama', 'ID_Karyawan', 'Departemen', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']
                table.add_row([nama, id_karyawan, departemen, jabatan, tanggal_bergabung, gaji_bulanan])
                print(table)


                confirm = input('Apakah Anda ingin Menyimpan Data ini? (Y/N)').upper()
                if confirm == 'Y':
                    karyawan.append({
                        'Nama': nama,
                        'ID_Karyawan': id_karyawan,
                        'Departemen': departemen,
                        'Jabatan': jabatan,
                        'Tanggal_Bergabung': tanggal_bergabung,
                        'Gaji_Bulanan(RP)': gaji_bulanan
                    })
                    print('\nData Karyawan berhasil ditambahkan!\n')
                else:
                    print('\nData Karyawan tidak berhasil disimpan!\n')


            except ValueError:
                print("\nInput tidak valid. Pastikan memasukkan angka untuk Gaji Bulanan.")



        elif read == '2':
            break
        else:
            print('Pilihan tidak valid, silakan masukkan pilihan yang benar.')



# Fungsi Untuk Menghapus Data Karyawan Perusahaan (DELETE)
def DELETEData(karyawan):
    while True:
        print('\n\n\t========= DELETEData =========')
        print('----------------------------------------------')
        print('\t 1. Hapus Data Karyawan')
        print('\t 2. Hapus Semua Data Karyawan')
        print('\t 3. Kembali ke Menu Utama')
        print('----------------------------------------------\n')
        read = input('Masukkan Pilihan Submenu Anda (1-3):')



        if read == '1':
            while True:
                id_karyawan = input('Masukkan ID_Karyawan yang ingin dihapus (format : ID-000): ').upper()
                if len(id_karyawan) == 6 and id_karyawan[:3] == 'ID-'  and id_karyawan[3:].isdigit():
                    break
                else:
                    print('ID Karyawan tidak sesuai Format. (format : ID-000). Silakan input kembali...')


            detail = next((item for item in karyawan if item['ID_Karyawan'].upper() == id_karyawan), None)
            if detail:
                print('\nData Karyawan yang ingin dihapus:')
                table = PrettyTable()
                table.field_names = ['Nama', 'ID_Karyawan', 'Departemen', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']
                table.add_row([detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                print(table)


                confirm = input("Apakah Anda Yakin ingin Menghapus data ini? (Y/N): ").upper()
                if confirm == 'Y':
                    karyawan.remove(detail)
                    print('\nData Karyawan berhasil dihapus!\n')
                else:
                    print('\nData Karyawan tidak dihapus...\n')
            else:
                print('\nData yang dicari tidak ada. Kembali ke menu...\n')



        elif read == '2':
            confirm = input("Apakah Anda Yakin ingin Menghapus semua data karyawan? (Y/N): ").upper()
            if confirm == 'Y':
                karyawan.clear()
                print('\nSemua Data Karyawan berhasil dihapus!\n')
            else:
                print('\nData Karyawan tidak dihapus...\n')



        elif read == '3':
            break
        else:
            print('Pilihan tidak valid, silakan masukkan pilihan yang benar...')



# Fungsi Untuk Menambahkan Data Karyawan Perusahaan (UPDATE)
def UPDATEData(karyawan):
    while True:
        print('\n\n\t========= UPDATEData =========')
        print('----------------------------------------------')
        print('\t 1. Mengupdate Data Karyawan')
        print('\t 2. Kembali ke Menu Utama')
        print('----------------------------------------------\n')
        read = input('Masukkan Pilihan Submenu Anda (1-2):')



        if read == '1':
            id_karyawan = input('Masukkan ID Karyawan yang ingin diupdate: ').upper()
            karyawan_found = False
            for detail in karyawan:
                if detail['ID_Karyawan'] == id_karyawan:
                    karyawan_found = True
                    print('Data Karyawan ditemukan:')


                    table = PrettyTable()
                    table.field_names = ['Nama', 'ID_Karyawan', 'Departemen', 'Jabatan', 'Tanggal_Bergabung', 'Gaji_Bulanan(RP)']
                    table.add_row([detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                    print(table)


                    while True:
                        confirm_update = input('Apakah Anda ingin melanjutkan update data ini? (Y/N): ').upper()
                        if confirm_update in ['Y', 'N']:
                            break
                        else:
                            print('Input tidak valid. Silakan masukkan Y/N...')


                    if confirm_update == 'Y':
                        while True:
                            print('\nPilih data yang ingin diupdate:')
                            print('1. Departemen')
                            print('2. Jabatan')
                            print('3. Gaji Bulanan')
                            pilihan = input('Masukkan pilihan anda (1-3): ')


                            if pilihan == '1':
                                detail['Departemen'] = input('Masukkan Departemen baru: ')
                                break
                            elif pilihan == '2':
                                detail['Jabatan'] = input('Masukkan Jabatan baru: ')
                                break
                            elif pilihan == '3':
                                while True:
                                    try:
                                        gaji_bulanan = int(input('Masukkan Gaji Bulanan baru (RP): '))
                                        if gaji_bulanan > 0:
                                            detail['Gaji_Bulanan(RP)'] = gaji_bulanan
                                            break
                                        else:
                                            print("Gaji bulanan harus lebih besar dari nol. Silakan masukkan kembali.")
                                    except ValueError:
                                        print("\nInput tidak valid. Pastikan memasukkan angka untuk Gaji Bulanan.")
                                break
                            else:
                                print('Pilihan tidak valid, silakan masukkan pilihan yang benar...')


                        print('\nData Karyawan Berhasil di Update!\n')
                        table.clear_rows()
                        table.add_row([detail['Nama'], detail['ID_Karyawan'], detail['Departemen'], detail['Jabatan'], detail['Tanggal_Bergabung'], detail['Gaji_Bulanan(RP)']])
                        print(table)

                    else:
                        print('Update Data dibatalkan...')
                    break

            if not karyawan_found:
                print('\nID Karyawan tidak ditemukan.\n')



        elif read == '2':
            break
        else:
            print('Pilihan tidak valid, Silakan masukkan pilihan yang benar...')



# Fungsi Untuk Melihat Total Gaji Data Karyawan Perusahaan (CALCULATED)
def CALCULATEData(karyawan):
    while True:
        print('\n\n\t========= CALCULATEData =========')
        print('-----------------------------------------------------')
        print('\t 1. Total Gaji Seluruh Karyawan')
        print('\t 2. Total Gaji Departemen Data Karyawan')
        print('\t 3. Kembali ke Menu Utama')
        print('-----------------------------------------------------\n')
        read = input('Masukkan Pilihan Submenu Anda (1-3):')



        if read == '1':
            if len(karyawan) != 0:
                total_gaji = 0
                
                
                for i in karyawan:
                    total_gaji += i ['Gaji_Bulanan(RP)']
                print(f'\nTotal Gaji Seluruh Karyawan: Rp {total_gaji:,}')
            else:
                print('Tidak ada Data Karyawan yang tersedia...')



        elif read == '2':
            if len(karyawan) != 0:
                departemen = input('Masukkan Departemen yang ingin dihitung Total Gajinya: ')
                total_gaji_departemen = 0
                found = False
                
                
                for i in karyawan:
                    if i ['Departemen'].lower() == departemen.lower():
                        total_gaji_departemen += i ['Gaji_Bulanan(RP)']
                        found = True
                
                
                if found:
                    print(f'\nTotal Gaji Karyawan di Departemen {departemen}: Rp {total_gaji_departemen:,}')
                else:
                    print(f'Tidak ada Karyawan dengan Departemen {departemen}. Silakan Input Kembali...')
            else:
                print('Tidak ada Data Karyawan yang tersedia...')



        elif read == '3':
            break
        else:
            print('Pilihan tidak valid. Silakan input dengan Benar...')



# Fungsi utama
def main():
    while True:
        print('\n==============================================')
        print('\t   Data Karyawan Perusahaan')
        print('==============================================')
        print('          Selamat Datang di Sistem \n      Manajemen Data Karyawan Perusahaan')
        print('----------------------------------------------')
        print('List Menu Utama Data Karyawan Perusahaan :')
        print('1. Menampilkan Data Karyawan ')
        print('2. Menambahkan Data Karyawan ')
        print('3. Menghapus Data Karyawan ')
        print('4. Mengupdate Data Karyawan ')
        print('5. Hitung Total Gaji Karyawan')
        print('6. Keluar Program')
        print('==============================================')

        try:
            pilih = int(input('Masukan Pilihan (1-6) : '))
        except ValueError :
            print('Pilihan tidak valid. Masukkkan Angka 1-6.')
            continue

        if pilih == 1 :
            READData(karyawan)
        elif pilih == 2 :
            CREATEData(karyawan)
        elif pilih == 3 :
            DELETEData(karyawan)
        elif pilih == 4 :
            UPDATEData(karyawan)
        elif pilih == 5 :
            CALCULATEData(karyawan)
        elif pilih == 6 :
            while True :
                keluar = input('Ingin keluar ? (Y/N)').upper()
                if keluar == 'Y':
                    print('\nSampai Jumpa Kembali! (APP CLOSE)')
                    return
                elif keluar == 'N':
                    print('Anda Memilih untuk tetap berada di Aplikasi.')
                    break
                else:
                    print('Pilihan Tidak Valid, Silakan Coba Lagi.')
        else:
            print('\nPilihan tidak tersedia')



# Jalankan Fungsi utama
# Pada saat mengimport modul Jika dipanggil sebagai libary maka fungsi main tidak langsung dijalankan
if __name__ == '__main__':
    main()
