import cx_Oracle

username = "jmckinstry3"
password = ""
dsn = 'localhost'
port = 8080
encoding = 'UTF-8'

conn = None
sql = 'INSERT INTO GOOG(date, open, high, low, close, volume) ' \
      'VALUES("2012-01-01", 10.2, 10.3, 10.2, 10.25, 10000);'
try:
    connection = cx_Oracle.connect(
        username,
        password,
        dsn,
        encoding)

    print(conn.version)

    with conn.cursor() as cursor:
        cursor.execute(sql)
        cursor.commit()
except cx_Oracle.Error as e:
    print(e)
finally:
    if conn:
        conn.close()