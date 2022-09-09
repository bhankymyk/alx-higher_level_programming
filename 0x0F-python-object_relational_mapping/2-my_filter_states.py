#!/usr/bin/python3
"""This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usas where name matches the argument."""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC".format(argv[4]))
    allStates = cur.fetchall()

    for state in allStates:
        print(state)
