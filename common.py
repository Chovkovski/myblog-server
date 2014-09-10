# -*- coding: utf-8 -*-

def jsonp(func):
	def wrapper(self):
		jsonp = self.get_argument("callback", "")
		if jsonp != "":
			result = jsonp + "(" + func(self) + ")"
		else:
			result = func(self)
		return result
	return wrapper