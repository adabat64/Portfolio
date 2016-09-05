import sqlite3

c = sqlite3.connect('bd.db')

def createTables():
    c.execute("CREATE TABLE if not exists BD(\
    TITLE TEXT PRIMARY KEY, \
    AUTHOR TEXT, \
    PUBLISHER TEXT );")

    c.execute("CREATE TABLE if not exists BD_ISSUE(\
    BD_TITLE TEXT,\
    ISSUE_NUM INTEGER,\
    ISSUE_TITLE TEXT,\
    PRIMARY KEY(BD_TITLE, ISSUE_NUM),\
    FOREIGN KEY(BD_TITLE) REFERENCES BD(TITLE));")

def newBD(title, author, publisher):
    #SQL command values
    val_str = "'{}', '{}', '{}'".format(title, author, publisher)

    sql_str = "INSERT INTO BD \
        (TITLE, AUTHOR, PUBLISHER) \
        VALUES ({});".format(val_str)

    c.execute(sql_str)
    c.commit()
    return c.total_changes

def newIssue(bd_title, issue_num, issue_title):
    val_str = "'{}', '{}', '{}'".format(bd_title, issue_num, issue_title)

    sql_str = "INSERT INTO BD_ISSUE \
        (BD_TITLE, ISSUE_NUM, ISSUE_TITLE) \
        VALUES ({});".format(val_str)

    c.execute(sql_str)
    c.commit()
    return c.total_changes

def viewAll_BD():
    # Create sql string
    sql_str = "SELECT * from BD"
    cursor = c.execute(sql_str)

    # Get data from cursor in array
    rows = cursor.fetchall()
    return rows

def viewAll_Issues(title):
    val_str = "'{}'".format(title)

    sql_str = "SELECT * FROM BD_ISSUE WHERE BD_ISSUE.BD_TITLE == ({});".format(val_str)
    cursor = c.execute(sql_str)

    rows = cursor.fetchall()
    return rows


# def updateBD(change_id, title, author, publisher):
#     # Create values part of sql command
#     val_str = "TITLE='{}', AUTHOR='{}', PUBLISHER={}".format(\
#               title, author, publisher)
#
#     sql_str = "UPDATE BD set {} where BD(BD_ID)={};".format(\
#         val_str, change_id)
#     print (sql_str)
#
#     c.execute(sql_str)
#     c.commit()
#     return c.total_changes
#
# def updateIssue(change_id, issue_num, issue_title):
#     # Create values part of sql command
#     val_str = "ISSUE_NUM='{}', ISSUE_TITLE='{}'".format(\
#               issue_num, issue_title)
#
#     sql_str = "UPDATE ISSUE set {} where ISSUE(BD_ID)={};".format(\
#         val_str, change_id)
#     print (sql_str)
#
#     c.execute(sql_str)
#     c.commit()
#     return c.total_changes
#
def deleteBD(title):
    i=0
    all_issues = viewAll_Issues(title)
    for row in all_issues:
        deleteIssue(title,i)
        i+=1

    val_str = "'{}'".format(title)
    # Create sql string
    sql_str = "DELETE from BD where TITLE= {};".format(val_str)

    c.execute(sql_str)
    c.commit()
    return c.total_changes

def deleteIssue(title, issue_num):
    val_str = "'{}'".format(title)
    sql_str ="DELETE FROM BD_ISSUE WHERE BD_TITLE == {} AND ISSUE_NUM == {};".format(val_str,issue_num)

    c.execute(sql_str)
    c.commit()
    return c.total_changes

createTables()
