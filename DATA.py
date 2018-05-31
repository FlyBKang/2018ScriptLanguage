import urllib
import urllib.request
import urllib.parse
import xml.parsers.expat
#key = 'cZhMcv5t%2B%2FBfr0VI%2BGLEMg7ByYojH2Y0%2FmH1yJXM0bgLBcO20YW0ett4Rlply3VMweUQ142UAwAFX9ko0eEu9Q%3D%3D'
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
city = u'광주'
num = 500
queryParams = '?' +'serviceKey=cZhMcv5t%2B%2FBfr0VI%2BGLEMg7ByYojH2Y0%2FmH1yJXM0bgLBcO20YW0ett4Rlply3VMweUQ142UAwAFX9ko0eEu9Q%3D%3D&' +urllib.parse.urlencode({ urllib.parse.quote_plus('numOfRows') : num, urllib.parse.quote_plus('pageNo') : 1, urllib.parse.quote_plus('sidoName') : city, urllib.parse.quote_plus('ver') : '1.3' })
addr = url + queryParams
#Request = urllib.request.Request('http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=cZhMcv5t%2B%2FBfr0VI%2BGLEMg7ByYojH2Y0%2FmH1yJXM0bgLBcO20YW0ett4Rlply3VMweUQ142UAwAFX9ko0eEu9Q%3D%3D&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.3')

Request = urllib.request.Request(addr)
Request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(Request).read()
#print(response_body)
#자세한 주소 찍기

class Handler():
   def __init__(self):
        self.stationName = 'stationName'
        self.mangName = 'mangName'
        self.dataTime = 'dataTime'
        self.so2value = 'so2Value'
        self.coValue = 'coValue'
        self.o3Value = 'o3Value'
        self.no2Value = 'no2Value'
        self.pm10Value = 'pm10Value'
    #    self.pm10Value24 = 'pm10Value24'
        self.pm25Value = 'pm25Value'
    #    self.pm25Value24 = 'pm25Value24'
    #    self.khaiValue = 'khaiValue'
    #    self.khaiGrade = 'khaiGrade'
    #    self.so2Grade = 'so2Grade'
    #    self.coGrade = 'coGrade'
    #    self.o3Grade = 'o3Grade'
    #    self.no2Grade = 'no2Grade'
    #    self.pm10Grade = 'pm10Grade'
    #    self.pm25Grade = 'pm25Grade'
    #    self.pm10Grade1h = 'pm10Grade1h'
    #    self.pm25Grade1h = 'pm25Grade1h'

handle = Handler()
dic = {}
index = 0

check = 0
def start_element(name,attrs):
    global check
    if( name == 'stationName'):
        check = 1
    if (name == 'mangName'):
        check = 2
    if (name == 'dataTime'):
        check = 3
    if (name == 'so2Value'):
        check = 4
    if (name == 'coValue'):
        check = 5
    if (name == 'o3Value'):
        check = 6
    if (name == 'no2Value'):
        check = 7

    if (name == 'pm10Value'):
        check = 8

    if (name == 'pm25Value'):
        check = 9

def char_data(data):
    global check
    global handle
    if(check == 1):
        handle = Handler()
        handle.stationName=repr(data)
        check = 0

    if(check == 2):
        handle.mangName=repr(data)
        check = 0

    if (check == 3):
        handle.dataTime = repr(data)
        check = 0

    if (check == 4):
        handle.so2Value = repr(data)
        check = 0

    if (check == 5):
        handle.coValue = repr(data)
        check = 0

    if (check == 6):
        handle.o3Value = repr(data)
        check = 0

    if (check == 7):
        handle.no2Value = repr(data)
        check = 0
    if (check == 8):
        handle.pm10Value = repr(data)
        check = 0
    if (check == 9):
        handle.pm25Value = repr(data)
        dic.update({handle.stationName: [handle.mangName, handle.dataTime, handle.so2Value, handle.coValue,
                                         handle.o3Value, handle.no2Value,handle.pm10Value,handle.pm25Value]})
        check = 0
pa = xml.parsers.expat.ParserCreate()
pa.StartElementHandler = start_element
pa.CharacterDataHandler = char_data
pa.Parse(response_body)
for key,value in dic.items():
    print("NAME(key): " + key + " - ")
    print("Locate: " + value[0] + ", Date " + value[1] +  ", 이산화황: " + value[2] +", 일산화탄소: " + value[3] +", 오존: " + value[4] +", 이산화질소: " + value[5]+", 미세먼지: " + value[6]+", 초미세먼지: " + value[7])

