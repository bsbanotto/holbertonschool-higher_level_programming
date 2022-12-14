#!/usr/bin/python3
"""
This python script lists all states from the database hbtn_0e_0_usa
that equal the state name that was passed
"""


import MySQLdb


def select_state():
    """
    This method lists all the states in the table that start with
    the given state name
    """
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    state = sys.argv[4]

    cur.execute("SELECT * FROM states WHERE name LIKE binary\
                %(name)s ORDER BY id", {'name': state})
    rows = cur.fetchall()
    if rows is None:
        return False
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_state()
