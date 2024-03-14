#!/usr/bin/python3
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
            SELECT c.id, c.name, s.name
            FROM cities AS c
            JOIN states AS s
            ON s.id = c.state_id
            ORDER BY c.id ASC

            '''
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
