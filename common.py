# -*- coding: utf-8 -*-
import MySQLdb

def execute_sql(sql):
	conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'myblog', port = 3306, charset = "utf8")
	cursor = conn.cursor()
	cursor.execute(sql)
	result = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return result