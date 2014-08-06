# -*- coding: utf-8 -*-
import json
import sys

import db

def get_person_info():
	sql = "select * from person_info"
	result = db.execute_sql(sql)[0]
	info = { "photo_addr" : result[0], "name" : result[1], "en_name" : result[2], "age" : result[3], "email" : result[4] }
	return json.dumps(info, ensure_ascii = False)

def get_nav_info():
	types_sql = "select * from types"
	types = db.execute_sql(types_sql)
	result = []
	for nav_type in types:
		type_id = nav_type[0]
		type_name = nav_type[1]
		tags_sql = "select * from tags where type_id = %s" % type_id
		tags = db.execute_sql(tags_sql)
		tag_names = []
		for tag in tags:
			tag_names.append(tag[2])
		nav = { "id" : type_id, "name" : type_name, "tags" : tag_names }
		result.append(nav)
	return json.dumps(result, ensure_ascii = False)

def get_blog_num(sql):
	num = db.execute_sql(sql)[0][0]
	result = { "num" : num }
	return json.dumps(result, ensure_ascii = False)

def get_state_num():
	sql = "select count(*) from state"
	return get_blog_num(sql)

def get_lite_blog_num(tag):
	if tag == "全部":
		sql = "select count(*) from lite_blogs"
	else:
		sql = "select count(*) from lite_blogs as l, tags as t where l.tag_id = t.id and t.tag_name = '%s'" % tag
	return get_blog_num(sql)

def get_tech_blog_num(tag):
	if tag == "全部":
		sql = "select count(*) from tech_blogs"
	else:
		sql = "select count(*) from tech_blogs as te, tags as t where te.tag_id = t.id and t.tag_name = '%s'" % tag
	return get_blog_num(sql)

def get_song_blog_num(tag):
	if tag == "全部":
		sql = "select count(*) from songs"
	else:
		sql = "select count(*) from songs as s, tags as t where s.tag_id = t.id and t.tag_name = '%s'" % tag
	return get_blog_num(sql)

def get_album_num(tag):
	if tag == "全部":
		sql = "select count(*) from album"
	else:
		sql = "select count(*) from album as a, tags as t where a.tag_id = t.id and t.tag_name = '%s'" % tag
	return get_blog_num(sql)

def get_album_picture_num(album):
	sql = "select count(*) from pictures as p, album as a where p.album_id = a. id and a.name = '%s'" % album
	return get_blog_num(sql)

def get_state(start, count = 5):
	sql = "select * from state order by time desc limit %d, %d" % (start, count)
	state = db.execute_sql(sql)
	result = []
	for one_state in state:
		content = one_state[1]
		date = str(one_state[2])
		result.append({ "content" : content, "date" : date })
	return json.dumps(result, ensure_ascii = False)

def get_lite_blog_summary(start, tag, count = 5):
	if tag == "全部":
		sql = "select id, tag_id, title, summary, time from lite_blogs order by time desc limit %d, %d" % (start, count)
	else:
		sql = "select l.id, l.tag_id, l.title, l.summary, l.time from lite_blogs as l, tags as t where l.tag_id = t.id and t.tag_name = '%s' order by l.time desc limit %d, %d" % (tag, start, count)
	lite_blogs = db.execute_sql(sql)
	result = []
	for one_lite in lite_blogs:
		result.append({ "id" : one_lite[0], "tag_id" : one_lite[1], "title" : one_lite[2], "summary" : one_lite[3], "date" : str(one_lite[4]) })
	return json.dumps(result, ensure_ascii = False)

def get_lite_blog(blog_id):
	sql = "select title, content, time from lite_blogs where id = '%d'" % blog_id
	lite_blog = db.execute_sql(sql)[0]
	result = { "title" : lite_blog[0], "content" : lite_blog[1], "date" : str(lite_blog[2]) }
	return json.dumps(result, ensure_ascii = False)

def get_tech_blog_summary(start, tag, count = 5):
	if tag == "全部":
		sql = "select id, tag_id, title, summary, time from tech_blogs order by time desc limit %d, %d" % (start, count)
	else:
		sql = "select te.id, te.tag_id, te.title, te.summary, te.time from tech_blogs as te, tags as t where te.tag_id = t.id and t.tag_name = '%s' order by te.time desc limit %d, %d" % (tag, start, count)
	lite_blogs = db.execute_sql(sql)
	result = []
	for one_lite in lite_blogs:
		result.append({ "id" : one_lite[0], "tag_id" : one_lite[1], "title" : one_lite[2], "summary" : one_lite[3], "date" : str(one_lite[4]) })
	return json.dumps(result, ensure_ascii = False)

def get_tech_blog(blog_id):
	sql = "select title, content, time from tech_blogs where id = '%d'" % blog_id
	lite_blog = db.execute_sql(sql)[0]
	result = { "title" : lite_blog[0], "content" : lite_blog[1], "date" : str(lite_blog[2]) }
	return json.dumps(result, ensure_ascii = False)

def get_song_blog(start, tag, count = 5):
	if tag == "全部":
		sql = "select title, src, time from songs order by time desc limit %d, %d" % (start, count)
	else:
		sql = "select s.title, s.src, s.time from songs as s, tags as t where s.tag_id = t.id and t.tag_name = '%s' order by s.time desc limit %d, %d" % (tag, start, count)
	songs = db.execute_sql(sql)
	result = []
	for one_song in songs:
		result.append({ "title" : one_song[0], "src" : one_song[1], "date" : str(one_song[2]) })
	return json.dumps(result, ensure_ascii = False)

def get_album_summary(start, tag, count = 5):
	if tag == "全部":
		sql = "select * from album limit %d, %d" % (start, count)
	else:
		sql = "select a.* from album as a, tags as t where a.tag_id = t.id and t.tag_name = '%s' limit %d, %d" % (tag, start, count)
	albums = db.execute_sql(sql)
	result = []
	for album in albums:
		album_id = int(album[0])
		album_name = album[2]
		sql = "select src, time from pictures where album_id = %d order by time desc limit 3" % album_id
		summary = db.execute_sql(sql)
		pictures = []
		for picture in summary:
			pictures.append({ "src" : picture[0], "date" : str(picture[1]) })
		result.append({ "album" : album_name, "summary" : pictures })
	return json.dumps(result, ensure_ascii = False)

def get_album_picture(start, album, count = 5):
	sql = "select p.src, p.time from pictures as p, album as a where p.album_id = a.id and a.name = '%s' order by p.time desc limit %d, %d" % (album, start, count)
	pictures = db.execute_sql(sql)
	result = []
	for picture in pictures:
		result.append({ "src" : picture[0], "date" : str(picture[1]) })
	return json.dumps(result, ensure_ascii = False)
