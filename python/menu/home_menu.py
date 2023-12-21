import sys
from . import contact_menu, transaction_menu
def run(conn):
    print("Selamat datang di program tim natus vincere")
    print("1. Menu kontak")
    print("2. Menu transaksi")
    print("3. Keluar program")
    input_menu = int(input("Masukan nomor menu (1/2): "))
    
    if input_menu == 1:
        contact_menu.run(conn)
    elif input_menu == 2:
        transaction_menu.run(conn)
    elif input_menu == 3:
        sys.exit(0)
    else:
        print("menu tidak ada")
        run(conn)