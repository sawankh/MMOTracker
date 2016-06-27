import sys

sys.path.insert(0, 'requests/')

from requestHandle import *
from jsonHandle import *
from csvHandle import *
# r = getRequest("http://jsonplaceholder.typicode.com/photos")
# print getContent(r)
# # r = getRequest("https://api.github.com/events")
# r = getRequest("http://www.json-generator.com/api/json/get/cfXfjCmEuq?indent=2")
# printCode(r)
# printURL(r)

# j = getContent(r)
fp = open('ex.json', 'r')
json_value = fp.read()
raw_data = json.loads(json_value)
x = getProcessedData(raw_data["items"], 'item')


writeDictCSV("test.csv", x[0], x[1])
# p = getProcessedData(raw_data['items'], 'items')
# writeDictCSV("test.csv", p[0], p[1])
# processed_data = []
# header = []
# for item in raw_data:
#     reducedElement = {}
#     reduceElement('items', item, reducedElement)

#     header += reducedElement.keys()

#     processed_data.append(reducedElement)

# header = list(set(header))
# header.sort()

# s = jsonToString(j)
# d = stringToJSON(j)
# print type(raw_data)
# #print type(flattenJSON(d[0], "__"))
# dlist = []

# x = flattenJSON(raw_data[0])
# dlist.append(x)
# dlistt = getHeaders(dlist)
# # print dlistt
# p = []
# c = getData(dlist, dlistt)
# #print c
# writeCSV("test.csv", dlistt, c)



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