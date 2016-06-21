import sys

sys.path.insert(0, 'requests/')

from requestHandle import *
from jsonHandle import *
from csvHandle import *
r = getRequest("http://jsonplaceholder.typicode.com/photos")
# r = getRequest("https://api.github.com/events")
# r = getRequest("http://www.json-generator.com/api/json/get/cfXfjCmEuq?indent=2")
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
# print dlistt
p = []
c = getData(dlist, dlistt)
#print c
writeCSV("test.csv", dlistt, c)



# node = ''
# processed_data = []
# header = []
# for item in d:
#     reducedElement = {}
#     reduceElement(node, item)
#     header += reducedElement.keys()
#     processed_data.append(reducedElement)

# header = list(set(header))
# header.sort()
# writeCSV("test.csv", header, processed_data)