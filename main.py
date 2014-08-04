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
			"get_state" : lambda : self.get_state()
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

application = tornado.web.Application([(r"/", MainHandler),], debug=True)

if __name__ == "__main__":
	reload(sys)
	sys.setdefaultencoding('utf-8')
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
