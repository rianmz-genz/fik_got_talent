def fetchall(cursor):
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Data kosong")
    for row in rows:
        print(row)