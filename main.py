# -*- coding: utf-8 -*-
import sys

import tornado.ioloop
import tornado.web

import basic_info

def jsonp(func):
	def wrapper(self):
		jsonp = self.get_argument("callback", "")
		if jsonp != "":
			result = jsonp + "(" + func(self) + ")"
		else:
			result = func(self)
		return result
	return wrapper

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
			"get_song_blog" : lambda : self.get_song_blog()
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

application = tornado.web.Application([(r"/", MainHandler),], debug=True)

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding('utf-8')
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
