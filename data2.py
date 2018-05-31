import urllib
import urllib.request
import urllib.parse
import xml.parsers.expat
key = 'iaMcZcv8cEqBQSsB%2FsY7%2BbknDG3FD6dPJsqNMSkDMpHFgMwywZZd5wcu85XPZi4jAUFmS9x7bLcmgoccWHVsUQ%3D%3D&'
url = 'https://www.kdhc.co.kr/openapi-data/service/kdhcWeatherObser/weatherObser'
num = 22
queryParams = '?' +'serviceKey=iaMcZcv8cEqBQSsB%2FsY7%2BbknDG3FD6dPJsqNMSkDMpHFgMwywZZd5wcu85XPZi4jAUFmS9x7bLcmgoccWHVsUQ%3D%3D&' +urllib.parse.urlencode({ urllib.parse.quote_plus('pageNo') : 1,urllib.parse.quote_plus('numOfRows') : num, urllib.parse.quote_plus('startDate') : 20180531,  urllib.parse.quote_plus('endDate') : 20180531})
addr = url + queryParams
print(addr)
Request = urllib.request.Request(addr)
Request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(Request).read()
#print(response_body)

class Handler():
   def __init__(self):
        self.plantId = 'plantId'
        self.wthr06h = 'wthr06h'
        self.wthr12h = 'wthr12h'
        self.wthrAvg = 'wthrAvg'
        self.whtrMax = 'wthrMax'
        self.wthrMin = 'wthrMin'
       #self.wthr01h
       #self.wthr02h
       #self.wthr03h
       #self.wthr04h
       #self.wthr05h
       #self.wthr06h
       #self.wthr07h
       #self.wthr08h
       #self.wthr09h
       #self.wthr10h
       #self.wthr11h
       #self.wthr13h
       #self.wthr14h
       #self.wthr15h
       #self.wthr16h
       #self.wthr17h
       #self.wthr18h
       #self.wthr19h
       #self.wthr20h
       #self.wthr21h
       #self.wthr22h
       #self.wthr23h

handle = Handler()
dic = {}
index = 0

check = 0





def start_element(name,attrs):
    global check
    if( name == 'plantId'):
        check = 1
    if (name == 'wthr06h'):
        check = 2
    if (name == 'wthr12h'):
        check = 3
    if (name == 'wthrAvg'):
        check = 4
    if (name == 'wthrMax'):
        check = 5
    if (name == 'wthrMin'):
        check = 6

def char_data(data):
    global check
    global handle
    if(check == 1):
        handle = Handler()
        handle.plantId=repr(data)
        check = 0

    if(check == 2):
        handle.wthr06h=repr(data)
        check = 0

    if (check == 3):
        handle.wthr12h = repr(data)
        check = 0

    if (check == 4):
        handle.wthrAvg = repr(data)
        check = 0

    if (check == 5):
        handle.wthrMax = repr(data)
        check = 0

    if (check == 6):
        handle.wthrMin = repr(data)
        dic.update({handle.plantId : [ handle.wthr06h,handle.wthr12h, handle.wthrAvg,handle.wthrMax,handle.wthrMin]})
        check = 0


pa = xml.parsers.expat.ParserCreate()
pa.StartElementHandler = start_element
pa.CharacterDataHandler = char_data
pa.Parse(response_body)


for key,value in dic.items():
    print("NAME(key): " + key + " - ")
    print(' wthr06  ' + value[0] + 'wthr12 ' +value[1] + ' wthravg ' + value[2] + ' wthrMax ' + value[3] + ' wthrMin ' + value[4])