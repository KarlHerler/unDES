import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

class Metrics:
	def current(self):
		i = r.get("key:curr")
	 	if (not i): i=0
	 	
 		return i