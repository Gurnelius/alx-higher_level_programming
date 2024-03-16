#!/usr/bin/python3
'''
    lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
'''
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
        )
    cur = conn.cursor()

    query = '''
    SELECT *
    FROM states
    WHERE name like BINARY "N%"
    ORDER BY id ASC
    '''

    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
