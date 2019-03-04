#!/usr/bin/python

import sqlite3
import os
conn = sqlite3.connect('books.db')
c = conn.cursor()
rootdir="中文书库"
for root, dirs, files in os.walk(rootdir, topdown=False):
    for filename in files:
        name=filename.split('.')[0]
        path=(os.path.join(root, filename))
        sql='INSERT INTO PathInfo (name,path) VALUES ("{0}","{1}" );'.format(name,path)
        print (sql)
        c.execute(sql);
        conn.commit()
conn.close()
