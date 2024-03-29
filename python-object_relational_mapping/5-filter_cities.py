#!/usr/bin/python3

"""script that takes in the name of a state as an argument and lists all \
        cities of that state, using the database hbtn_0e_4_usa."""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
                 ON cities.state_id = states.id WHERE \
                BINARY states.name = %(name)s", {'name': sys.argv[4]})
    rows = cur.fetchall()
    numlist = len(rows)
    count = 1
    for row in rows:
        print("{}{}".format(row[0],
                            (', ' if count < numlist else '')), end="")
        count = count + 1
    print()
