# -*- coding: utf-8 -*-
import json
import sys

import common

def get_person_info():
	sql = "select * from person_info"
	result = common.execute_sql(sql)[0]
	info = { "photo_addr" : result[0], "name" : result[1], "en_name" : result[2], "age" : result[3], "email" : result[4] }
	return json.dumps(info, ensure_ascii = False)

def get_nav_info():
	types_sql = "select * from types"
	types = common.execute_sql(types_sql)
	result = []
	for nav_type in types:
		type_id = nav_type[0]
		type_name = nav_type[1]
		tags_sql = "select * from tags where type_id = %s" % type_id
		tags = common.execute_sql(tags_sql)
		tag_names = []
		for tag in tags:
			tag_names.append(tag[2])
		nav = { "id" : type_id, "name" : type_name, "tags" : tag_names }
		result.append(nav)
	return json.dumps(result, ensure_ascii = False)

def get_state_num():
	sql = "select count(*) from state"
	num = common.execute_sql(sql)[0][0]
	result = { "num" : num }
	return json.dumps(result, ensure_ascii = False)

def get_state(start, count = 5):
	sql = "select * from state order by time desc limit %d, %d" % (start, count)
	state = common.execute_sql(sql)
	result = []
	for one_state in state:
		content = one_state[1]
		date = str(one_state[2])
		result.append({ "content" : content, "date" : date })
	return json.dumps(result, ensure_ascii = False)


