from . import helper
def get_all(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contacts")
    
    helper.fetchall(cursor)

def create(conn, name, phone):
    cursor = conn.cursor()
    data_to_insert = [
        (name, phone),
    ]
    cursor.executemany("INSERT INTO contacts (name,phone) VALUES (?,?)", data_to_insert)
    conn.commit()
    print("Berhasil menambahkan kontak")
    get_all(conn)
    
def get_by_name(conn, name):
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM contacts WHERE name like '%{name}%'"
    cursor.execute(sql_query)
    helper.fetchall(cursor)

def check_data_exists(conn, name):
    cursor = conn.cursor()
    sql_query = f"SELECT * FROM contacts WHERE name = '{name}'"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    return len(rows) > 0

def delete_by_name(conn, name):
    try:
        if(check_data_exists(conn, name)):
            cursor = conn.cursor()
            sql_query_delete = f"DELETE FROM contacts WHERE name = '{name}'"
            cursor.execute(sql_query_delete)
            conn.commit()
            print("Berhasil menghapus kontak")
            get_all(conn)
        else:
            print(f"Data dengan nama {name} tidak bisa dihapus karena tidak ditemukan")
    except Exception as e:
        print(e)

            