import sys

sys.path.insert(0, 'requests/')

from requestHandle import *
from jsonHandle import *

r = getRequest("http://jsonplaceholder.typicode.com/posts")
printCode(r)
printURL(r)

j = getContent(r)
#s = jsonToString(j)
d = stringToJSON(j)
#print type(flattenJSON(d[0], "__"))
dlist = []
for item in d:
	x = flattenJSON(item)
	dlist.append(x)
print checkSize(dlist)
