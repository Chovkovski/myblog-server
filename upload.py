# -*- coding: utf-8 -*-

import json
import MySQLdb

import db

def upload_story(tag_id, title, summary, content, date):
	sql = "insert into lite_blogs (tag_id, title, summary, content, time) values(%s, '%s', '%s', '%s', '%s')" % (tag_id, title, MySQLdb.escape_string(summary), MySQLdb.escape_string(content), date)
	result = db.execute_sql(sql)
	return json.dumps(result, ensure_ascii = False)

def upload_tech(tag_id, title, summary, content, date):
	sql = "insert into tech_blogs (tag_id, title, summary, content, time) values(%s, '%s', '%s', '%s', '%s')" % (tag_id, title, MySQLdb.escape_string(summary), MySQLdb.escape_string(content), date)
	result = db.execute_sql(sql)
	return json.dumps(result, ensure_ascii = False)