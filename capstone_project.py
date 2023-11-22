uname = input('Masukan username : ')
upass = input('Masukan password : ')
granted = False

stock_barang = [
    {
        "id": 100,
        "nama": "Shampoo",
        "harga": 1000,
        "jenis": "Alat Mandi",
        "stock_in": 30,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 101,
        "nama": "Sabun",
        "harga": 500,
        "jenis": "Alat Mandi",
        "stock_in": 25,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 102,
        "nama": "Chiki",
        "harga": 2000,
        "jenis": "Cemilan",
        "stock_in": 60,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 103,
        "nama": "Garam",
        "harga": 800,
        "jenis": "Bumbu Dapur",
        "stock_in": 20,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 104,
        "nama": "Kecap",
        "harga": 1200,
        "jenis": "Bumbu Dapur",
        "stock_in": 35,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 113,
        "nama": "Sereal",
        "harga": 2500,
        "jenis": "Cemilan",
        "stock_in": 20,
        "stock_out": 8,
        "status_barang": "Tersedia"
    },
    {
        "id": 106,
        "nama": "Tepung",
        "harga": 1000,
        "jenis": "Bahan Dasar",
        "stock_in": 50,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 107,
        "nama": "Terigu",
        "harga": 900,
        "jenis": "Bahan Dasar",
        "stock_in": 40,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 108,
        "nama": "Kacang",
        "harga": 1800,
        "jenis": "Cemilan",
        "stock_in": 30,
        "stock_out": 10,
        "status_barang": "Tersedia"
    },
    {
        "id": 109,
        "nama": "Bawang",
        "harga": 700,
        "jenis": "Bumbu Dapur",
        "stock_in": 25,
        "stock_out": 10,
        "status_barang": "Tidak Tersedia"
    }

]

if uname == 'admin' and upass == 'admin' :
    granted = True
    print("\033[H\033[J", end="")
else :
    print('Username / password salah!')

def table_data_all():
    print('__________________________________________________________________________________________________________________')
    print('ID\t |Nama Barang\t |Jumlah\t |Jenis\t\t |Stock In\t |Stock Out\t |Harga\t\t |Status')
    print('---------|---------------|---------------|---------------|---------------|---------------|---------------|--------')
    
    for i in range(len(stock_barang)) :
        print("{}\t |{} \t |{} \t\t |{} \t |{} \t\t |{} \t\t |{} \t\t |{}".format(stock_barang[i]["id"], stock_barang[i]["nama"], stock_barang[i]["stock_in"] - stock_barang[i]["stock_out"], stock_barang[i]["jenis"], stock_barang[i]["stock_in"], stock_barang[i]["stock_out"], stock_barang[i]["harga"], stock_barang[i]["status_barang"]))
    
    print('------------------------------------------------------------------------------------------------------------------')

def table_data_filter_byId(id) : 
    filter_result = [i for i in stock_barang if i['id']== int(id)]
    if len(filter_result) > 0 :
        print('__________________________________________________________________________________________________________________')
        print('ID\t |Nama Barang\t |Jumlah\t |Jenis\t\t |Stock In\t |Stock Out\t |Harga\t\t |Status')
        print('---------|---------------|---------------|---------------|---------------|---------------|---------------|--------')
        for i in range(len(filter_result)):
            print("{}\t |{} \t |{} \t\t |{} \t |{} \t\t |{} \t\t |{} \t\t |{}".format(filter_result[i]["id"], filter_result[i]["nama"], filter_result[i]["stock_in"] - filter_result[i]["stock_out"], filter_result[i]["jenis"], filter_result[i]["stock_in"], filter_result[i]["stock_out"], filter_result[i]["harga"], filter_result[i]["status_barang"]))
        print('------------------------------------------------------------------------------------------------------------')
    else:
        print('Data tidak ditemukan')

def table_data_filter_byJenis(jenis) :
    filter_result = [i for i in stock_barang if i['jenis']== jenis]
    if len(filter_result) > 0 :
        print('__________________________________________________________________________________________________________________')
        print('ID\t |Nama Barang\t |Jumlah\t |Jenis\t\t |Stock In\t |Stock Out\t |Harga\t\t |Status')
        print('---------|---------------|---------------|---------------|---------------|---------------|---------------|--------')
        for i in range(len(filter_result)):
            print("{}\t |{} \t |{} \t\t |{} \t |{} \t\t |{} \t\t |{} \t\t |{}".format(filter_result[i]["id"], filter_result[i]["nama"], filter_result[i]["stock_in"] - filter_result[i]["stock_out"], filter_result[i]["jenis"], filter_result[i]["stock_in"], filter_result[i]["stock_out"], filter_result[i]["harga"], filter_result[i]["status_barang"]))
        print('------------------------------------------------------------------------------------------------------------------')
    else:
        print('Data tidak ditemukan')

def table_data_filter_byStatus(status) :
    filter_result = [i for i in stock_barang if i['status_barang']== status]
    if len(filter_result) > 0 :
        print('__________________________________________________________________________________________________________________')
        print('ID\t |Nama Barang\t |Jumlah\t |Jenis\t\t |Stock In\t |Stock Out\t |Harga\t\t |Status')
        print('---------|---------------|---------------|---------------|---------------|---------------|---------------|--------')
        for i in range(len(filter_result)):
            print("{}\t |{} \t |{} \t\t |{} \t |{} \t\t |{} \t\t |{} \t\t |{}".format(filter_result[i]["id"], filter_result[i]["nama"], filter_result[i]["stock_in"] - filter_result[i]["stock_out"], filter_result[i]["jenis"], filter_result[i]["stock_in"], filter_result[i]["stock_out"], filter_result[i]["harga"], filter_result[i]["status_barang"]))
        print('------------------------------------------------------------------------------------------------------------------')
    else:
        print('Data tidak ditemukan')

def menu(select) :
    print("\033[H\033[J", end="")
    if select == '1' :
        while True :
            print("\033[H\033[J", end="")
            print('1. Menampilkan Stock gudang\r\n===============\r\n')
            table_data_all()
            u_input = input('\r\nMenu : \r\n1. Tampilkan data berdasarkan ID barang\r\n0. Kembali ke menu utama\r\n\r\nPilih Menu : ')

            if u_input == '1' :
                print("\033[H\033[J", end="")
                print('1. Menampilkan Stock gudang\r\n===============\r\n')
                table_data_all()
                id_barang = input("\r\nMasukan ID barang : ")
                
                print("\033[H\033[J", end="")
                print('1. Menampilkan Stock gudang\r\n===============\r\n')
                table_data_filter_byId(int(id_barang))
                input('\r\nTekan Enter Untuk kembali ke menu sebelumnya.')
            elif u_input == '0' :
                break
        # input('\r\nTekan Enter Untuk kembali ke menu utama.')  
    elif select == '2' :
        print("\033[H\033[J", end="")
        print('2. Menambahkan Stock gudang\r\n===============\r\n')
        # table_data_all()
        id_barang_baru = int(input("\r\nMasukan ID barang : "))
        nama_barang_baru = input("Masukan nama barang : ")
        jumlah_barang_baru = int(input("Masukan jumlah barang : "))
        jenis_barang_baru = input("Masukan jenis barang : ")
        harga_barang_baru = int(input("Masukan harga barang : "))
        status_barang_baru = input("Masukan status barang : ")

        filter_result = [i for i in stock_barang if i['id']== int(id_barang_baru)]
        if len(filter_result) > 0 :
            print("\r\nID barang tidak boleh sama!")
        else :
            print("\033[H\033[J", end="")
            print('2. Menambahkan Stock gudang\r\n===============\r\n')

            stock_barang.append({
                "id": id_barang_baru,
                "nama": nama_barang_baru,
                # "jumlah": jumlah_barang_baru,
                "harga": harga_barang_baru,
                "jenis": jenis_barang_baru,
                "stock_in": jumlah_barang_baru,
                "stock_out": 0,
                "status_barang": status_barang_baru
            })

            filter_result = stock_barang[len(stock_barang) - 1]
            print('__________________________________________________________________________________________________________________')
            print('ID\t |Nama Barang\t |Jumlah\t |Jenis\t\t |Stock In\t |Stock Out\t |Harga\t\t |Status')
            print('---------|---------------|---------------|---------------|---------------|---------------|---------------|--------')
            print("{}\t |{} \t |{} \t\t |{} \t |{} \t\t |{} \t\t |{} \t\t |{}".format(filter_result["id"], filter_result["nama"], filter_result["stock_in"] - filter_result["stock_out"], filter_result["jenis"], filter_result["stock_in"], filter_result["stock_out"], filter_result["harga"], filter_result["status_barang"]))
            print('------------------------------------------------------------------------------------------------------------------')
            print('\r\nMenambahkan data berhasil!')

        input('\r\nTekan Enter Untuk kembali ke menu utama.')
    elif select == '3' :
        print("\033[H\033[J", end="")
        print('3. Mengupdate Stock gudang\r\n===============\r\n')
        table_data_all()
        id_barang = input("\r\nMasukan ID barang yang ingin diupdate : ")

        filter_result = [i for i in stock_barang if i['id']== int(id_barang)]
        if len(filter_result) > 0 :
            id_barang_update = int(input("Masukan ID barang baru : "))
            nama_barang_update = input("Masukan nama barang baru : ")
            # jumlah_barang_update = int(input("Masukan jumlah barang baru : "))
            jenis_barang_update = input("Masukan jenis barang baru : ")
            stockin_barang_update = int(input("Masukan stock in barang baru : "))
            stockout_barang_update = int(input("Masukan stock out barang baru : "))
            harga_barang_update = int(input("Masukan harga barang baru : "))
            status_barang_update = input("Masukan status barang baru : ")
            for i in range(len(stock_barang)):
                if stock_barang[i]['id'] == int(id_barang) :
                    stock_barang[i] = {
                        "id": id_barang_update,
                        "nama": nama_barang_update,
                        "jumlah": stockin_barang_update - stockout_barang_update,
                        "harga": harga_barang_update,
                        "jenis": jenis_barang_update,
                        "stock_in": stockin_barang_update,
                        "stock_out": stockout_barang_update,
                        "status_barang": status_barang_update
                    }

                    print("\033[H\033[J", end="")
                    print('3. Mengupdate Stock gudang\r\n===============\r\n')
                    print('__________________________________________________________________________________________________________________')
                    print('ID\t |Nama Barang\t |Jumlah\t |Jenis\t\t |Stock In\t |Stock Out\t |Harga\t\t |Status')
                    # print('------------------------------------------------------------------------------------------------------------')
                    print('---------|---------------|---------------|---------------|---------------|---------------|---------------|--------')
                    print("{}\t |{} \t |{} \t\t |{} \t |{} \t\t |{} \t\t |{} \t\t |{}".format(stock_barang[i]["id"], stock_barang[i]["nama"], stock_barang[i]["stock_in"] - stock_barang[i]["stock_out"], stock_barang[i]["jenis"], stock_barang[i]["stock_in"], stock_barang[i]["stock_out"], stock_barang[i]["harga"], stock_barang[i]["status_barang"]))
                    print('------------------------------------------------------------------------------------------------------------------')
                    print('\r\nUpdate data berhasil!')
                    
                    break
        else:
            print("ID tidak ditemukan!")

        input('\r\nTekan Enter Untuk kembali ke menu utama.')
    elif select == '4' :
        print("\033[H\033[J", end="")
        print('4. Menghapus stock gudang\r\n===============\r\n')
        table_data_all()
        id_barang = int(input("\r\nMasukan ID barang yang ingin dihapus : "))

        for i in range(len(stock_barang)):
            if stock_barang[i]['id'] == id_barang :
                del stock_barang[i]
                print("\033[H\033[J", end="")
                print('4. Menghapus stock gudang\r\n===============\r\n')
                table_data_all()
                print('\r\nHapus data berhasil!')
                break
            else:
                print("\033[H\033[J", end="")
                print('4. Menghapus stock gudang\r\n===============\r\n')
                print("ID tidak ditemukan!")
        input('\r\nTekan Enter Untuk kembali ke menu utama.')
    elif select == '5' :
        while True :
            print("\033[H\033[J", end="")
            print('5. Memfilter barang stock gudang\r\n===============\r\n')
            table_data_all()
            u_input = input('\r\nMenu : \r\n1. Filter berdasarkan jenis barang\r\n2. Filter berdasarkan status barang\r\n0. Kembali ke menu utama\r\n\r\nPilih Menu : ')

            if u_input == '1' : 
                jenis_barang = input("Masukan jenis barang : ")
                print("\033[H\033[J", end="")
                print('5. Memfilter barang stock gudang\r\n===============\r\n')
                table_data_filter_byJenis(jenis_barang)
                input('\r\nTekan Enter Untuk kembali ke menu sebelumnya.')

            elif u_input == '2' :
                status_barang = input("Masukan status barang : ")
                print("\033[H\033[J", end="")
                print('5. Memfilter barang stock gudang\r\n===============\r\n')
                table_data_filter_byStatus(status_barang)
                input('\r\nTekan Enter Untuk kembali ke menu sebelumnya.')
                
            elif u_input == '0' :
                break

while granted :
    print("\033[H\033[J", end="")
    print('Selamat datang di Stock Gudang Berkah\r\n====================================\r\n\r\nList menu :\r\n1. Menampilkan Stock gudang\r\n2. Menambahkan Stock gudang\r\n3. Mengupdate Stock gudang\r\n4. Menghapus stock gudang\r\n5. Memfilter barang stock gudang\r\n0. Exit program\r\n\r\n')
    user_input = input('Masukkan angka list yang ingin dijalankan : ')

    if user_input == '0' :
        break
    else :
        menu(user_input)