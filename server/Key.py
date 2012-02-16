import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)

class Key:
	batchsize = 1000000

	def getStaleKey(self):
		d = r.zrange("key:out", 0, 0, False, True)
		
		if (len(d)>0): d = d[0]
		else: return (False, 0) 

		return (((time.time()-d[1])>100), d[0])
	

 	def get(self):
		q = self.getStaleKey()
 		stale = q[0]
 		if stale: 
	 		i = q[1]
	 	else:
	 		i = r.get("key:curr")
	 		if (not i): i=0
	 	
 		out = int(i)+self.batchsize
 		if (not stale): r.set("key:curr", out)
 		
 		r.zadd("key:out", time.time(), i)

 		return str(out)+","+str(self.batchsize)
		

	def report(self, range, result, key=0):
		r.zrem("key:out", range)
		r.zadd("key:checked", time.time(), range)

		if (result):
			r.lpush("key:found", key)
			return str(range)+","+str(key)
		else:
			return range
