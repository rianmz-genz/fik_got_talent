from . import helper
def get_all(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM transactions")
    
    helper.fetchall(cursor)

def create_incoming_transaction(conn, description, nominal):
    cursor = conn.cursor()
    data_to_insert = [
        (description, nominal, "masuk"),
    ]
    cursor.executemany("INSERT INTO transactions (description,nominal,type) VALUES (?,?,?)", data_to_insert)
    conn.commit()
    print("Berhasil menambahkan transaksi masuk")
    # get_all(conn)

def create_outbound_transaction(conn, description, nominal):
    cursor = conn.cursor()
    data_to_insert = [
        (description, nominal, "keluar"),
    ]
    cursor.executemany("INSERT INTO transactions (description,nominal,type) VALUES (?,?,?)", data_to_insert)
    conn.commit()
    print("Berhasil menambahkan transaksi keluar")
    # get_all(conn)

def show_saldo(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT (SELECT SUM(nominal) FROM transactions WHERE type = 'masuk'), (SELECT SUM(nominal) FROM transactions WHERE type = 'keluar')")
    data_incoming = cursor.fetchone()
    saldo_now = data_incoming[0] - data_incoming[1]
    print(f"Saldo anda sekarang Rp. {saldo_now}")