import sqlite3


def database_connect(db_name):
    # will create it automatically if it doesn't exist
    return sqlite3.connect('../{}.sqlite'.format(db_name))


def create_table(conn, table_name, vars):
    print("---SQL COMMAND---")
    name_type = ""
    for v in vars:
        name_type += v[0] + " " + v[1] + ", "
    name_type = name_type[:-2]
    command = "CREATE TABLE IF NOT EXISTS " + table_name \
              + " (" + name_type + ");"
    print(command)
    conn.execute(command)
    conn.commit()


def insert_data(conn, table_name, vars):
    print("---SQL COMMAND---")
    names, values = "", ""
    for key, value in vars.items():
        names += key + ", "
        values += "'" + value + "'" + ", "
    names = names[:-2]
    values = values[:-2]
    command = "INSERT INTO " + table_name + " (" + names \
              + ") VALUES (" + values + ");"
    print(command)
    conn.execute(command)
    conn.commit()


def select_full_data(conn, table_name, vars):
    print("---SQL COMMAND---")
    cols = ""
    for name in vars['column_names']:
        cols += name + ", "
    cols = cols[:-2]
    command = "SELECT " + "*" + " FROM " + "A" + ";"
    print(command)
    conn.execute(command)
    data = conn.cursor().fetchall()
    return data


if __name__ == '__main__':
    conn = database_connect("SPY")
    table_name = "test"

    create_table(conn, table_name, [["first_name", "VARCHAR(20)"],
                                    ["last_name", "VARCHAR(20)"],
                                    ["phone_number", "INT"]])
    insert_data(conn, table_name, {"first_name": "John",
                                   "last_name": "Doe",
                                   "phone_number": "7203038168"})
    data = select_full_data(conn, table_name, {"column_names": ["first_name"]})
    print(data)

    conn.close()