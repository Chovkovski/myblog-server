# -*- coding: utf-8 -*-
import sys

import tornado.ioloop
import tornado.web

import basic_info
import upload

from common import jsonp

class MainHandler(tornado.web.RequestHandler):
	
	def get(self):
		task_name = self.get_argument("task_name", None)
		tasks = {
			"get_person_info" : lambda : self.get_person_info(),
			"get_nav_info" : lambda : self.get_nav_info(),
			"get_state_num" : lambda : self.get_state_num(),
			"get_state" : lambda : self.get_state(),
			"get_lite_blog_num" : lambda : self.get_lite_blog_num(),
			"get_lite_blog_summary" : lambda : self.get_lite_blog_summary(),
			"get_lite_blog" : lambda : self.get_lite_blog(),
			"get_tech_blog_num" : lambda : self.get_tech_blog_num(),
			"get_tech_blog_summary" : lambda : self.get_tech_blog_summary(),
			"get_tech_blog" : lambda : self.get_tech_blog(),
			"get_song_blog_num" : lambda : self.get_song_blog_num(),
			"get_song_blog" : lambda : self.get_song_blog(),
			"get_album_num" : lambda : self.get_album_num(),
			"get_album_summary" : lambda : self.get_album_summary(),
			"get_album_picture_num" : lambda : self.get_album_picture_num(),
			"get_album_picture" : lambda : self.get_album_picture()
		}
		if task_name != None:
			result = tasks[task_name]()
		else:
			result = "invalid task_name"
		self.write(result)

	@jsonp
	def get_person_info(self):
		return basic_info.get_person_info()

	@jsonp
	def get_nav_info(self):
		return basic_info.get_nav_info()

	@jsonp
	def get_state_num(self):
		return basic_info.get_state_num()

	@jsonp
	def get_state(self):
		start = self.get_argument("start", 0)
		return basic_info.get_state(int(start))

	@jsonp
	def get_lite_blog_num(self):
		tag = self.get_argument("tag", "全部")
		return basic_info.get_lite_blog_num(tag)

	@jsonp
	def get_lite_blog_summary(self):
		start = self.get_argument("start", 0)
		tag = self.get_argument("tag", "全部")
		return basic_info.get_lite_blog_summary(int(start), tag)

	@jsonp
	def get_lite_blog(self):
		blog_id = self.get_argument("id", "")
		if blog_id == "":
			return ""
		else:
			return basic_info.get_lite_blog(int(blog_id))

	@jsonp
	def get_tech_blog_num(self):
		tag = self.get_argument("tag", "全部")
		return basic_info.get_tech_blog_num(tag)

	@jsonp
	def get_tech_blog_summary(self):
		start = self.get_argument("start", 0)
		tag = self.get_argument("tag", "全部")
		return basic_info.get_tech_blog_summary(int(start), tag)

	@jsonp
	def get_tech_blog(self):
		blog_id = self.get_argument("id", "")
		if blog_id == "":
			return ""
		else:
			return basic_info.get_tech_blog(int(blog_id))

	@jsonp
	def get_song_blog_num(self):
		tag = self.get_argument("tag", "全部")
		return basic_info.get_song_blog_num(tag)

	@jsonp
	def get_song_blog(self):
		start = self.get_argument("start", 0)
		tag = self.get_argument("tag", "全部")
		return basic_info.get_song_blog(start, tag)

	@jsonp
	def get_album_num(self):
		tag = self.get_argument("tag", "全部")
		return basic_info.get_album_num(tag)

	@jsonp
	def get_album_summary(self):
		tag = self.get_argument("tag", "全部")
		start = self.get_argument("start", 0)
		return basic_info.get_album_summary(int(start), tag)

	@jsonp
	def get_album_picture_num(self):
		album = self.get_argument("album")
		return basic_info.get_album_picture_num(album)

	@jsonp
	def get_album_picture(self):
		album = self.get_argument("album")
		start = self.get_argument("start", 0)
		return basic_info.get_album_picture(int(start), album)

class UploadHandler(tornado.web.RequestHandler):

	def post(self):
		task_name = self.get_argument("task_name", None)
		tasks = {
			"upload_story" : lambda : self.upload_story(),
			"upload_tech" : lambda : self.upload_tech(),
			"upload_songs" : lambda : self.upload_songs(),
			"upload_pictures" : lambda : self.upload_pictures()
		}
		if task_name != None:
			result = tasks[task_name]()
		else:
			result = "invalid task_name"
		self.write(result)

	@jsonp
	def upload_story(self):
		tag_id = self.get_argument("tag_id")
		title = self.get_argument("title")
		summary = self.get_argument("summary")
		content = self.get_argument("content")
		date = self.get_argument("date")
		return upload.upload_story(tag_id, title, summary, content, date)

	@jsonp
	def upload_tech(self):
		tag_id = self.get_argument("tag_id")
		title = self.get_argument("title")
		summary = self.get_argument("summary")
		content = self.get_argument("content")
		date = self.get_argument("date")
		return upload.upload_tech(tag_id, title, summary, content, date)

	@jsonp
	def upload_songs(self):
		pass

	@jsonp
	def upload_pictures(self):
		pass

application = tornado.web.Application([(r"/", MainHandler), (r"/upload", UploadHandler)], debug=True)

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding('utf-8')
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
