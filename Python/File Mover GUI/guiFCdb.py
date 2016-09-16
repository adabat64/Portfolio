import sqlite3

# Connect to simpsons database
conn = sqlite3.connect('folderChooser.db')

def createTable():
    conn.execute("CREATE TABLE if not exists BTN_PRESSTIMES( \
        PRESSTIMES TEXT PRIMARY KEY);")

def newPressTime(presstime):
    # Create values part of sql command
    val_str = "'{}'".format(presstime)

    sql_str = "INSERT INTO BTN_PRESSTIMES \
        (PRESSTIMES) \
        VALUES ({});".format(val_str)
    print (sql_str)

    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def viewAll():
    # Create sql string
    sql_str = "SELECT * from BTN_PRESSTIMES"
    cursor = conn.execute(sql_str)

    # Get data from cursor in array
    rows = cursor.fetchall()
    return rows

createTable()
