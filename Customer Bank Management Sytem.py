from tabulate import tabulate 
#  Dataset pelanggan menggunakan dictionary
data_pelanggan = {
    101: {
        'Nomor Rekening': '1234567890',
        'Nama': 'Budi',
        'Tanggal Pembukaan Akun': '2020-01-15',
        'Nomor Telepon': '081234567890',
        'Jenis Kelamin': 'Laki-laki',
        'Pin' : '123456',
        'Saldo': 12000000
    },
    102: {
        'Nomor Rekening': '0987654321',
        'Nama': 'Rina',
        'Tanggal Pembukaan Akun': '2019-03-22',
        'Nomor Telepon': '082345678901',
        'Jenis Kelamin': 'Perempuan',
        'Pin' : '654321',
        'Saldo': 4500000
    },
    103: {
        'Nomor Rekening': '2345678901',
        'Nama': 'Tono',
        'Tanggal Pembukaan Akun': '2021-07-08',
        'Nomor Telepon': '083456789012',
        'Jenis Kelamin': 'Laki-laki',
        'Pin' : '456789',
        'Saldo': 8000000
    },
    104: {
        'Nomor Rekening': '8765432109',
        'Nama': 'Siti',
        'Tanggal Pembukaan Akun': '2018-10-30',
        'Nomor Telepon': '084567890123',
        'Jenis Kelamin': 'Perempuan',
        'Pin' : '654123',
        'Saldo': 15000000
    },
    105: {
        'Nomor Rekening': '3456789012',
        'Nama': 'Agus',
        'Tanggal Pembukaan Akun': '2022-05-14',
        'Nomor Telepon': '085678901234',
        'Jenis Kelamin': 'Laki-laki',
        'Pin' : '321456',
        'Saldo': 5000000
    }
}

# CREATE

def tambah_akun():
    print('+','-'*45,'+')
    print('|', 'Menu Buat Akun'.center(45), '|')
    print('+','-'*45,'+')
    print('''List Menu:
1. Tambah Akun
2. Kembali Menu
''')
    menu_tambah = int(input('Masukkan Nomor yang ingin anda pilih: '))
    if menu_tambah == 1:
        no_pelanggan = int(input("Masukkan Nomor Pelanggan: ")) 
        if no_pelanggan in data_pelanggan.keys():
            print('Nomor Pelanggan Sudah Ada, Silahkan Masukkan Nomor Pelanggan Lain')
            tambah_akun()
        else:
            no_rek = input('Masukkan Nomor Rekening pemilik akun: ')
            nama = input('Masukkan Nama pemilik akun: ')
            tgl_pembukaan_akun = input('Masukkan Tanggal Pembukaan Akun pemilik akun: ')
            no_hp = input('Masukkan Nomer Telepon pemilik akun: ')
            gender = input('Masukkan Jenis Kelamin pemilik akun (pria/wanita): ')
            pin = input('Masukkan Pin pemilik akun: ')
            saldo = 0
            verif_tambah_akun = input('Apakah anda yakin akan menambah akun ini? (ya/tidak): ')
            if verif_tambah_akun == 'ya':
                data_pelanggan[no_pelanggan] = {'Nomor Rekening': no_rek, 'Nama': nama, 
                                            'Tanggal Pembukaan Akun': tgl_pembukaan_akun, 
                                            'Nomor Telepon': no_hp, 'Jenis Kelamin': gender, 
                                            'Pin' : pin, 'Saldo': saldo} 

                print ('Akun Berhasil Dibuat')
                tambah_akun()
            else: 
                print ('Akun tidak jadi dibuat')
                tambah_akun()        

    elif menu_tambah == 2:
        admin_menu()

    else:
        print('Nomor yang anda masukkan tidak ada dalam menu, Silahkan coba lagi')
        tambah_akun()

# DELETE

def hapus_akun(): 
    print('+','-'*45,'+')
    print('|', 'Menu Hapus Akun'.center(45), '|')
    print('+','-'*45,'+')
    print('''List Menu:
1. Hapus Akun
2. Kembali Menu
''') 
    menu_hapus = int(input('Masukkan Nomor yang ingin anda pilih: '))
    if menu_hapus == 1:
        no_pelanggan = int(input("Masukkan Nomor Pelanggan: "))
        if no_pelanggan in data_pelanggan.keys():
            verif_hapus_akun = input('Apakah anda yakin akan menghapus akun ini? (ya/tidak): ')
            if verif_hapus_akun == 'ya':
                del data_pelanggan[no_pelanggan]
                print('Akun berhasil dihapus')
                hapus_akun() 
            else:
                hapus_akun()
        else:
            print('Nomor Pelanggan Tersebut Tidak Ditemukan')
            hapus_akun()
    elif menu_hapus == 2: 
        admin_menu()
    else:
        print('Nomor yang anda masukkan tidak ada dalam menu, Silahkan coba lagi')
        hapus_akun()

# UPDATE

def ubah_akun():
    print('+','-'*45,'+')
    print('|', 'Menu Edit Akun'.center(45), '|')
    print('+','-'*45,'+')
    print('''List Menu:
1. Edit Akun
2. Kembali Menu
''')
    menu_ubah = int(input('Masukkan Nomor yang ingin anda pilih: '))
    if menu_ubah == 1:
        data_pelanggan 
        no_pelanggan = int(input("Masukkan Nomor Pelanggan: "))
        if no_pelanggan in data_pelanggan.keys():
            hasil_cari_akun(data_pelanggan[no_pelanggan])
            verif_lanjut = input('Apakah anda ingin melanjutkan Edit Akun? (ya/tidak): ')
            if verif_lanjut == 'ya': # masih belum nentuin apa aja yang ingin diubah
                print('-'*45)
                print ('''Data apa yang ingi diubah: 
1. Nama
2. Nomor Telepon
3. Pin 
''')
                pilihan = int(input('Masukkan Index yang ingin di ubah: '))
                if pilihan == 1:
                    data_baru = input ('Masukkan Data Baru: ')
                    if data_baru == '':
                        print ('Ulangi')
                    else:
                        verif_save = input('Apakah anda ingin Menyimpan akun ini? (ya/tidak): ')
                        if verif_save == 'ya':
                            data_pelanggan[no_pelanggan]['Nama'] = data_baru
                            print('Data Berhasil Disimpan')
                            ubah_akun()
                        else:
                            ubah_akun()
                elif pilihan == 2:
                    data_baru = input ('Masukkan Data Baru: ')
                    if data_baru == '':
                        print ('Ulangi')
                    else:
                        verif_save = input('Apakah anda ingin Menyimpan akun ini? (ya/tidak): ')
                        if verif_save == 'ya':
                            data_pelanggan[no_pelanggan]['Nomor Telepon'] = data_baru
                            print('Data Berhasil Disimpan')
                            ubah_akun()
                        else:
                            ubah_akun()
                elif pilihan == 3:
                    data_baru = input ('Masukkan Data Baru: ')
                    if data_baru == '':
                        print ('Ulangi')
                    else:
                        verif_save = input('Apakah anda ingin Menyimpan akun ini? (ya/tidak): ')
                        if verif_save == 'ya':
                            data_pelanggan[no_pelanggan]['Pin'] = data_baru
                            print('Data Berhasil Disimpan')
                            ubah_akun()
                        else:
                            ubah_akun()
                else:
                    print ('Pilihan Salah!!')
                    ubah_akun()
            else:
                ubah_akun()
        else:
            print('Nomor Pelanggan Tersebut Tidak Ditemukan')
            ubah_akun()
    elif menu_ubah == 2:
        admin_menu()
    else:
        print('Nomor yang anda masukkan tidak ada dalam menu, Silahkan coba lagi')
        ubah_akun()

# READ

def semua_akun():
    if len(data_pelanggan) > 0:
        list_data_pelanggan = []
        for no_customer, info in data_pelanggan.items():
            baris = [no_customer] + list(info.values())
            list_data_pelanggan.append(baris)
        header = ['No. Rekening', 'Nama', 'Tanggal Pembukaan Akun', 'Nomor Telepon', 'Jenis Kelamin', 'Pin', 'Saldo']
        print(tabulate(list_data_pelanggan, headers=header, tablefmt='grid'))
        info_akun()
    else:
        print ('Data tidak ditemukan')
        info_akun()

def cari_akun(): # HASIL CARI AKUN MAU BERBENTUK TABULATE?
    while True:    
        print('-'*45)
        print('''Cari Sesuai Kata Kunci:
1. Nomor Pelanggan
2. Nama
3. Nomor Rekening
4. Kembali Menu Daftar Akun
        ''')
        menu_cari = int(input("Masukkan Nomor Yang Anda Ingin Cari: "))
        if menu_cari == 1:
            no_pelanggan = int(input("Masukkan Nomor Pelanggan: "))
            if no_pelanggan in data_pelanggan:
                hasil_cari_akun(data_pelanggan[no_pelanggan])
                continue
            else:
                print("Nomor Pelanggan tidak ditemukan.")
                continue
        elif menu_cari == 2:
            nama = input('Masukkan Nama Pelanggan Yang Ingin Anda Cari: ')
            found = False
            for pelanggan in data_pelanggan.values():
                if pelanggan['Nama'].lower() == nama.lower():  # Mencari nama dengan case insensitive
                    hasil_cari_akun(pelanggan)
                    found = True
                    break
            if found == False:
                    print ('Nama Tidak Ditemukan, Silahkan Coba Lagi')
                    continue    
        elif menu_cari == 3:
            no_rek = input('Masukkan Nomor Rekening Yang Ingin Anda Cari: ')
            found = False
            for pelanggan in data_pelanggan.values():
                if pelanggan['Nomor Rekening'] == no_rek:
                    hasil_cari_akun(pelanggan)
                    found = True
                    break
            if found == False:
                print ('Nama Tidak Ditemukan, Silahkan Coba Lagi')
                continue
        elif menu_cari== 4:
            info_akun()
        else:
            print('Nomor yang anda masukkan tidak ada dalam menu, Silahkan coba lagi')
            continue

def hasil_cari_akun(hca): # HASIL CARI AKUN MAU BERBENTUK TABULATE
    data_pelanggan
    print ('Nama: ', hca['Nama'])
    print ('Tanggal Pembukaan Akun: ', hca['Tanggal Pembukaan Akun'])
    print ('Nomor Rekening: ', hca['Nomor Rekening'])
    print ('Nomor Telepon: ', hca['Nomor Telepon'])
    print ('Jenis Kelamin: ', hca['Jenis Kelamin'])
    print ('Pin: ', hca['Pin'])
    print ('Saldo: ', hca['Saldo'])

def info_akun(): 
    print('+','-'*45,'+')
    print('|', 'Menu Daftar Akun'.center(45), '|')
    print('+','-'*45,'+')
    print('''List Menu:
1. Daftar Semua Akun
2. Cari Akun
3. Kembali Ke Menu Admin
''')
    menu_info = int(input("Masukkan Nomor yang ingin anda pilih: "))
    if menu_info == 1: 
        semua_akun()
    elif menu_info == 2: 
        cari_akun()
    elif menu_info == 3: 
        admin_menu()
    else: 
        print('Nomor yang anda masukkan tidak ada dalam menu, Silahkan coba lagi')
        info_akun()

# MENU ADMIN

def admin_menu():
    print('+','-'*45,'+')
    print('|', 'Admin Panel'.center(45), '|')
    print('+','-'*45,'+')
    print('''List Menu:
1. Menampilkan Daftar Akun Customer
2. Menambah Akun Customer
3. Menghapus Akun Customer
4. Mengubah Akun Customer
5. Exit Panel
''')
    menu_admin = int(input("Masukkan angka menu yang ingin dijalankan: "))
    if menu_admin == 1:
        info_akun()
    elif menu_admin == 2:
        tambah_akun()
    elif menu_admin == 3:
        hapus_akun()
    elif menu_admin == 4:
        ubah_akun()
    elif menu_admin == 5:
        main_menu()
    else:
        print('Nomor yang anda masukkan tidak ada dalam menu, Silahkan coba lagi')
        admin_menu()

# MENU CUSTOMER 

# Variabel global untuk menyimpan pelanggan yang sedang login
customer_yang_login = None


def lihat_saldo():
    global customer_yang_login
    if customer_yang_login:
        saldo = customer_yang_login['Saldo']
        print (f'Saldo Anda Sebesar \nRp. {saldo}')
        customer_menu()
    else:
        print ('Tidak Ada Akun Yang Login')
        customer_menu()

def setor_tunai(): 
    global customer_yang_login
    if customer_yang_login:
        setor = int(input('Masukkan Jumlah Yang Ingin Anda Setor (Minimal Rp. 50.000): Rp. '))
        if setor >= 50000: # tanya kalo setor tuh harus > 50k?
            customer_yang_login['Saldo'] += setor
            print (f'''Transaksi Berhasil
Saldo Anda Sekaranng Adalah Rp. {customer_yang_login['Saldo']}''')
            customer_menu()
        else:
            print ('Jumlah setor tunai harus lebih besar dari Rp. 50.000')
            customer_menu()

def tarik_tunai(): 
    global customer_yang_login
    if customer_yang_login:
        setor = int(input('Masukkan Jumlah Yang Ingin Anda Tarik (Minimal Rp. 50.000): Rp. '))
        if setor >= 50000 and setor <= customer_yang_login['Saldo']: # tanya kalo setor tuh harus > 50k?
            customer_yang_login['Saldo'] -= setor
            print (f'''Transaksi Berhasil
Saldo Anda Sekaranng Adalah Rp. {customer_yang_login['Saldo']}''')
            customer_menu()
        elif setor > customer_yang_login['Saldo']:
            print ('Jumlah Yang Anda Masukkan Terlalu Besar')
            customer_menu()
        else:
            print ('Jumlah Tarik tunai harus lebih besar dari Rp. 50.000')
            customer_menu()

def customer_menu():
    global customer_yang_login
    print('+','-'*45,'+')
    print('|', 'Customer Panel'.center(45), '|')
    print('+','-'*45,'+')
    print('''List Menu:
1. Lihat Saldo
2. Setor Tunai
3. Tarik Tunai
4. Exit Panel
''')
    menu_customer = int(input("Masukkan angka menu yang ingin dijalankan: "))
    if menu_customer == 1:
        lihat_saldo() 
    elif menu_customer == 2:
        setor_tunai()
    elif menu_customer == 3:
        tarik_tunai()
    elif menu_customer == 4:
        customer_yang_login = None
        main_menu()
    else: 
        print('Nomor yang anda masukkan tidak ada dalam menu, Silahkan coba lagi')
        customer_menu()

# MENU UTAMA

def main_menu():
    global customer_yang_login
    while True:
        print('+','-'*45,'+')
        print('|', 'Selamat Datang Di Bank Rafi'.center(45), '|')
        print('+','-'*45,'+')
        print('''List Menu:
1. Admin Login
2. Customer Login
3. Exit Program
''')
        menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
        if menu == 1: 
            id_admin = input ('Masukkan ID admin: ')
            password_admin = input ('Masukkan Password: ')
            if id_admin == 'admin' and password_admin == 'admin ganteng':
                admin_menu()
            else:
                print ('ID/Password yang anda masukkan salah')
                main_menu()
        elif menu == 2:
            nama_pelanggan = input('Masukkan Nama Anda: ')
            nama_ditemukan = False 
            for key, value in data_pelanggan.items():
                if value['Nama'] == nama_pelanggan:
                    nama_ditemukan = True
                    pin = input('Masukkan Pin Anda: ')
                    if value['Pin'] == pin:
                        print('-'*45)
                        print("Login berhasil!")
                        customer_yang_login = value  # untuk menyimpan pelanggan yang login
                        customer_menu()
                    else:
                        print('Pin yang Anda masukkan salah. Silakan coba lagi.')
                    break
            else:
                print ('Nama Anda Tidak Terdaftar')
                main_menu()
        elif menu == 3: 
            exit_program = input('Apakah Anda Yakin Ingin Keluar Program? (ya/tidak): ')
            if exit_program == 'ya':
                break
            else:
                continue
        else:
            print ('Angka Yang Anda Masukkan Tidak Valid, Silahkan Coba Lagi!!')
            continue
main_menu()