# -*- coding: utf-8 -*-

import MySQLdb

def insert_pictures(album_id, src, date):
	sql = "insert into pictures (album_id, src, time) values(%d, '%s', '%s')" % (album_id, src, date)
	conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'myblog', port = 3306, charset = "utf8")
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()

if __name__ == "__main__":
	count = 1
	while count < 81:
		src = r"http://pavelblog.oss-cn-hangzhou.aliyuncs.com/pictures/%E5%A4%A7%E5%8D%83%E4%B8%96%E7%95%8C/%E8%A7%82%E7%9E%BB%E6%80%BB%E7%BB%9F%E5%BA%9C/" + str(count) + ".jpg"
		insert_pictures(11, src, "2011-02-27")
		count += 1
