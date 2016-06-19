import sys

sys.path.insert(0, 'requests/')

from requestHandle import *
from jsonHandle import *
from csvHandle import *

r = getRequest("https://api.github.com/events")
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
dlist = getHeaders(dlist)
print len(dlist)
#writeCSV("test.csv", dlist)