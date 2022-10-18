#!/usr/bin/python3
"""This python script lists all states from the database hbtn_0e_0_usa"""


import MySQLdb


def filter_states():
    """This method lists all the states in the table"""
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE ASCII(name)=78 ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
