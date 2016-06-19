import sys

sys.path.insert(0, 'requests/')

from requestHandle import *
from jsonHandle import *
from csvHandle import *
r = getRequest("http://jsonplaceholder.typicode.com/posts")
# r = getRequest("https://api.github.com/events")
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
dlistt = getHeaders(dlist)
print len(dlistt)
p = []
c = getData(dlist, dlistt)
writeCSV("test.csv", dlistt, c)