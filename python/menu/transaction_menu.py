from controller import transaction_controller
from . import home_menu
def run(conn):
    print("Selamat datang di program transaksi, pilih menu anda: ")
    print("1. Mencatat transaksi masuk")
    print("2. Mencatat transaksi keluar")
    print("3. Melihat riwayat transaksi")
    print("4. Menampilkan saldo")
    print("5. Kembali")

    input_menu = int(input("Masukan nomor menu (1/2/3/4/5): "))

    if input_menu == 1:
        print("Silahkan mengisi data yang dibutuhkan")
        description = input("Masukan deskripsi transaksi: ")
        nominal = input("Masukan jumlah transaksi: ")
        transaction_controller.create_incoming_transaction(conn=conn, description=description, nominal=nominal)
        print("\n")
        run(conn)
    elif input_menu == 2:
        print("Silahkan mengisi data yang dibutuhkan")
        description = input("Masukan deskripsi transaksi: ")
        nominal = input("Masukan jumlah transaksi: ")
        transaction_controller.create_outbound_transaction(conn=conn, description=description, nominal=nominal)
        print("\n")
        run(conn)
    elif input_menu == 3:
        transaction_controller.get_all(conn)
        print("\n")
        run(conn)
    elif input_menu == 4:
        transaction_controller.show_saldo(conn)
        print("\n")
        run(conn)
    elif input_menu == 5:
        home_menu.run(conn=conn)
    else:
        print("menu yang anda pilih salah")