from controller import contact_controller
from . import home_menu
def run(conn):
    print("Selamat datang di program kontak, pilih menu anda: ")
    print("1. Menampilkan semua kontak yang tersimpan")
    print("2. Menambahkan kontak baru")
    print("3. Mencari kontak berdasarkan nama")
    print("4. Menghapus kontak berdasarkan nama")
    print("5. Kembali")

    input_menu = int(input("Masukan nomor menu (1/2/3/4/5): "))

    if input_menu == 1:
        contact_controller.get_all(conn=conn)
        run(conn)
    elif input_menu == 2:
        print("Silahkan mengisi data yang dibutuhkan")
        name = input("Masukan nama kontak: ")
        phone = input("Masukan nomor kontak: ")
        contact_controller.create(conn, name, phone)
        run(conn)
    elif input_menu == 3:
        name = input("Nama kontak yang dicari: ")
        contact_controller.get_by_name(conn, name)
        run(conn)
    elif input_menu == 4:
        name = input("Nama kontak yang dicari: ")
        contact_controller.delete_by_name(conn, name)
        run(conn)
    elif input_menu == 5:
        home_menu.run()
    else:
        print("menu yang anda pilih salah")