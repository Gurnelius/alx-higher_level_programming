#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

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
            SELECT c.name
            FROM cities AS c
            JOIN states AS s
            ON s.id = c.state_id
            WHERE s.name = %s
            ORDER BY c.id ASC
            '''
    cur.execute(query, (state,))
    query_rows = cur.fetchall()
    city_names = ""
    for row in query_rows:
        city_names += row[0] + ", "
        city_names = city_names.rstrip(", ")
    print(city_names)

    cur.close()
    conn.close()
