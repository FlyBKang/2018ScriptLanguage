from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox
import urllib
import urllib.request
import urllib.parse
import xml.parsers.expat



class Handler():
   def __init__(self):
        self.tm= 'tm'
        self.temp = 'temp'
        self.tmx = 'tmx'
        self.tmn = 'tmn'
        self.wfKor = 'wfKor' # 1 맑음 2 구름 조금 3~4 흐림 5~6 비 7눈
        self.r12 = "r12"
        self.hour = 'hour'

handle = Handler()
dic = {}
dic2 = {}
index = 0
check = 0
addr = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000&mode=stdxm'
city ="서울"
clist = ['서울','인천','대전','가평','강릉','독도','대구','부산','제주','광주','전주']
list = ['http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2823764100&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3011062000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4182025000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4215025000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4794033000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2714076000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2644058000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=5013025300&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2920054000&mode=stdxm','http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4511160500&mode=stdxm']



def start_element(name,attrs):
    global check
    if(check == 8):
        return
    if( name == 'tm'):
        check = 1
    if (name == "temp"):
        check = 2
    if (name == 'tmx'):
        check = 3
    if (name == 'tmn'):
        check = 4
    if (name == 'wfKor'):
        check = 5
    if (name == 'r12'):
        check = 6
    if (name == 'hour'):
        check = 7

def char_data(data):
    global check
    global handle
    if(check == 1):
        handle = Handler()
        handle.tm =repr(data)
        check = 0
    if(check == 2):
        handle.temp =repr(data)
        check = 0
    if (check == 3):
        handle.tmx = repr(data)
        check = 0
    if (check == 4):
        handle.tmn = repr(data)
        check = 0
    if (check == 5):
        handle.wfKor = repr(data)
        check = 0
    if (check == 6):
        handle.r12 = repr(data)
        dic.update({ city: [handle.temp,handle.temp,handle.tmx,handle.tmn,handle.wfKor,handle.r12,handle.hour,handle.tm]})
        check = 8
    if (check == 7):
        handle.hour = repr(data)
        check = 0


class Handler2():
    def __init__(self):
        self.stationName = 'stationName'
        self.mangName = 'mangName'
        self.dataTime = 'dataTime'
        self.so2value = 'so2Value'
        self.coValue = 'coValue'
        self.o3Value = 'o3Value'
        self.no2Value = 'no2Value'
        self.pm10Value = 'pm10Value'
        self.pm25Value = 'pm25Value'


handle2 = Handler2()
check2 = 0
url2 = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
city2 = u'서울'


def start_element2(name, attrs):
    global check2
    if (name == 'stationName'):
        check2 = 1
    if (name == 'mangName'):
        check2 = 2
    if (name == 'dataTime'):
        check2 = 3
    if (name == 'so2Value'):
        check2 = 4
    if (name == 'coValue'):
        check2 = 5
    if (name == 'o3Value'):
        check2 = 6
    if (name == 'no2Value'):
        check2 = 7
    if (name == 'pm10Value'):
        check2 = 8
    if (name == 'pm25Value'):
        check2 = 9


def char_data2(data):
    global check2
    global handle2
    ttt = repr(data)
    tt = ttt.replace("'", "")
    if (check2 == 1):
        handle2 = Handler2()
        handle2.stationName = tt
        check2 = 0

    if (check2 == 2):
        handle2.mangName = tt
        check2 = 0

    if (check2 == 3):
        handle2.dataTime = tt
        check2 = 0

    if (check2 == 4):
        handle2.so2Value = tt
        check2 = 0

    if (check2 == 5):
        handle2.coValue = tt
        check2 = 0

    if (check2 == 6):
        handle2.o3Value = tt
        check2 = 0

    if (check2 == 7):
        handle2.no2Value = tt
        check2 = 0
    if (check2 == 8):
        handle2.pm10Value = tt
        check2 = 0
    if (check2 == 9):
        handle2.pm25Value = tt
        dic2.update({handle2.stationName : [handle2.mangName, handle2.dataTime, handle2.so2Value, handle2.coValue,
                                         handle2.o3Value, handle2.no2Value, handle2.pm10Value, handle2.pm25Value]})
        check2 = 0


for i in range(0, 11):
    check = 0
    addr = list[i]
    city = clist[i]
    Request = urllib.request.Request(addr)
    Request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(Request).read()
    pa = xml.parsers.expat.ParserCreate()
    pa.StartElementHandler = start_element
    pa.CharacterDataHandler = char_data
    pa.Parse(response_body)

clist2 = ['서울','인천','대전','경기','강원','경북','대구','부산','제주','광주','전북']
clist3 = ['구로구','부평','둔산동','가평','평창읍','태하리','지산동','대연동','연동','송정1동','중앙동(전주)']
for i in range(0, 11):
    city2 = clist2[i]
    check2 = 0
    queryParams2 = '?' + 'serviceKey=cZhMcv5t%2B%2FBfr0VI%2BGLEMg7ByYojH2Y0%2FmH1yJXM0bgLBcO20YW0ett4Rlply3VMweUQ142UAwAFX9ko0eEu9Q%3D%3D&' + urllib.parse.urlencode(
        {urllib.parse.quote_plus('numOfRows'): 300, urllib.parse.quote_plus('pageNo'): 1,
         urllib.parse.quote_plus('sidoName'): city2, urllib.parse.quote_plus('ver'): '1.3'})
    addr2 = url2 + queryParams2
    Request2 = urllib.request.Request(addr2)
    Request2.get_method = lambda: 'GET'
    response_body2 = urllib.request.urlopen(Request2).read()
    pa2 = xml.parsers.expat.ParserCreate()
    pa2.StartElementHandler = start_element2
    pa2.CharacterDataHandler = char_data2
    pa2.Parse(response_body2)





iSearchIndex = 0


window = Tk()
window.title("날씨 프로그램")
window.resizable(0,0)
photo = PhotoImage(file="map.png").subsample(1,1)
imageLabel = Label(window, image=photo)
imageLabel.pack()

maskLB = {}
whLB = {}

def InitTopText():
    TempFont = font.Font(window, size = 18, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="[전국 날씨 찾기]")
    MainText.pack()
    MainText.place(x = 480, y = 10)
    MainText.configure(background="LightSkyblue")

def drawMask(num,index,w,h,size,color):
    global maskLB
    global window
    maskLB[num] = ttk.Label(window, text=' image place ')
    maskLB[num].pack()
    maskLB[num].config(justify=LEFT)
    if(index == 0):
        img = PhotoImage(file="mask0.png")

    if (index == 1):
        img = PhotoImage(file="mask1.png")

    if (index == 2):
        img = PhotoImage(file="mask2.png")

    img = img.subsample(size,size)
    maskLB[num].img = img
    maskLB[num].config(image=maskLB[num].img)
    maskLB[num].config(justify=LEFT)
    maskLB[num].place(x=w, y=h)
    if(color == 0):
        maskLB[num].configure(background="SystemWindow")
    else:
        maskLB[num].configure(background="azure3")

def drawWh(num,index,w,h,size,color):
    global whLB
    global window
    whLB[num] = ttk.Label(window, text=' image place ')
    whLB[num].pack()
    whLB[num].config(justify=LEFT)
    if(index == 0):
        img = PhotoImage(file="sun.png")
    if (index == 1):
        img = PhotoImage(file="cloud.png")

    if (index == 2):
        img = PhotoImage(file="rain.png")

    img = img.subsample(size,size)
    whLB[num].img = img
    whLB[num].config(image=whLB[num].img)
    whLB[num].config(justify=LEFT)
    whLB[num].place(x=w, y=h)
#    if(color == 0):
#            whLB[num].configure(background="DarkOliveGreen4")
#    else:
#        whLB[num].configure(background="azure3")

textLB = {}
def SmalldrawText(num,w,h,size,color,T):
    global textLB
    global window
    TempFont = font.Font(window, size = 6, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text=T)
    MainText.pack()
    MainText.place(x = w,y=h)
    if(color == 0):
        MainText.configure(background="DarkOliveGreen4")
    else:
        MainText.configure(background="azure3")

def drawText(num,w,h,size,color,T):
    global textLB
    global window
    TempFont = font.Font(window, size = 10, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text=T)
    MainText.pack()
    MainText.place(x = w,y=h)
    if(color == 0):
        MainText.configure(background="DarkOliveGreen4")
    else:
       MainText.configure(background="azure3")


#for key, value in dic2.items():
#    if(key==clist3[num]):
#        print("NAME(key): " + clist[num] + " - ")
#        print("Locate: " + value[0] + ", Date " + value[1] + ", 이산화황: " + value[2] + ", 일산화탄소: " + value[3] + ", 오존: " +value[4] + ", 이산화질소: " + value[5] + ", 미세먼지: " + value[6] + ", 초미세먼지: " + value[7])
#        if(num<10):
#            num+=1

num = 0
for key,value in dic.items():
    if (key == clist[num]):
        temp = 0
        if(value[4] == "'맑음'"):
            temp = 0
        if(value[4] == "'구름 조금'"):
            temp = 0
        if(value[4] == "'구름 많음'"):
            temp = 1
        if(value[4] == "'흐림'"):
            temp = 1
        if (value[4] == "'비'"):
            temp = 2
        if(num == 0):
            drawWh(1, temp, 140, 80, 2, 0)  # 서울
            SmalldrawText(13, 135, 70-5, 2, 0, value[1])
        if(num==1):
            drawWh(2, temp, 90, 140, 2, 1)  # 인천
            SmalldrawText(13, 85, 130-5, 2, 1, value[1])
        if(num==2):
            drawWh(3, temp, 140, 190, 2, 0)  # 대전
            SmalldrawText(13, 135, 180-5, 2, 0, value[1])
        if(num==3):
            drawWh(4, temp, 240, 130, 2, 0)  # 가평
            SmalldrawText(13, 235, 120-5, 2, 0, value[1])
        if(num==4):
            drawWh(5, temp, 250, 50, 2, 0)  # 강릉
            SmalldrawText(13, 245, 40-5, 2, 0, value[1])
        if(num==5):
            drawWh(6, temp, 360, 120, 2, 1)  # 독도
            SmalldrawText(13, 355, 110-5, 2, 1, value[1])
        if(num==6):
            drawWh(7, temp, 210, 180, 2, 0)  # 대구
            SmalldrawText(13, 205, 170-5, 2, 0, value[1])
        if(num==7):
            drawWh(8, temp, 290, 260, 2, 0)  # 부산
            SmalldrawText(13, 295, 250-5, 2, 0, value[1])
        if(num==8):
            drawWh(9, temp, 130, 330, 2, 0)  # 제주
            SmalldrawText(13, 125, 320-5, 2, 0, value[1])
        if(num==9):
            drawWh(10,temp, 170, 270, 2, 0)  # 광주
            SmalldrawText(13, 165, 260-5, 2, 0, value[1])
        if(num==10):
            drawWh(11,temp, 110, 220, 2, 0)  # 전주
            SmalldrawText(13, 95, 210-5, 2, 0, value[1])
        if (num < 10):
            num += 1

num = 0
for key,value in dic2.items():
    if(key==clist3[num]):
        temp = 0
        temp2 = 0
        RANGE = value[6]
        if('0' < RANGE < '30'):
            temp = 0
        elif('30' < RANGE< '80'):
            temp = 1
        elif('80' < RANGE):
            temp = 2

        RANGE = value[7]
        if ('0'< RANGE < '15'):
            temp2 = 0
        elif ('15'< RANGE < '50'):
            temp2 = 1
        elif ('50' < RANGE):
            temp2 = 2
        mynum = 0
        if(temp > temp2):
            mynum = temp
        else:
            mynum = temp2

        if(num == 0):
            drawMask(1, mynum, 140 - 20, 80 + 3, 3, 0)  # 서울
        if(num == 1):
            drawMask(2, mynum, 90 - 20, 140 + 3, 3, 1)  # 인천
        if(num == 2):
            drawMask(3, mynum, 140 - 20, 190 + 3, 3, 0)  # 대전
        if(num == 3):
            drawMask(4, mynum, 240 - 20, 130 + 3, 3, 0)  # 가평
        if(num == 4):
            drawMask(5, mynum, 250 - 20, 50 + 3, 3, 0)  # 강릉
        if(num == 5):
            drawMask(6, mynum, 360 - 20, 120 + 3, 3, 1)  # 독도
        if(num == 6):
            drawMask(7, mynum, 210 - 20, 180 + 3, 3, 0)  # 대구
        if(num == 7):
            drawMask(8, mynum, 290 - 20, 260 + 3, 3, 0)  # 부산
        if(num == 8):
            drawMask(9, mynum, 130 - 20, 330 + 3, 3, 0)  # 제주
        if(num == 9):
            drawMask(10, mynum, 170 - 20, 270 + 3, 3, 0)  # 광주
        if(num == 10):
            drawMask(11, mynum, 110 - 20, 220 + 3, 3, 0)  # 전주
        if (num < 10):
            num+=1





drawText(1,140+4,80+35,2,0,'서울')
drawText(2,90+4,140+35,2,1,'인천')
drawText(3,140+4,190+35,2,0,'대전')
drawText(4,240+4,130+35,2,0,'가평')
drawText(5,250+4,50+35,2,0,'강릉')
drawText(6,360+4,120+35,2,1,'독도')
drawText(7,210+4,180+35,2,0,'대구')
drawText(8,290+4,260+35,2,0,'부산')
drawText(9,130+4,330+35,2,0,'제주')
drawText(10,170+4,270+35,2,0,'광주')
drawText(11,110+4,220+35,2,0,'전주')


def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=1135, y=550)
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "서울")
    SearchListBox.insert(2, "인천")
    SearchListBox.insert(3, "대전")
    SearchListBox.insert(4, "가평")
    SearchListBox.insert(5, "강릉")
    SearchListBox.insert(6, "독도")
    SearchListBox.insert(7, "대구")
    SearchListBox.insert(8, "부산")
    SearchListBox.insert(9, "제주")
    SearchListBox.insert(10, "광주")
    SearchListBox.insert(11, "전주")
    SearchListBox.pack()
    SearchListBox.place(x = 1000, y=550)

    ListBoxScrollbar.config(command=SearchListBox.yview)


for key, value in dic2.items():
    if (key == clist3[iSearchIndex]):
        if(value[6] < '30'):
            drawText(12, 975, 350, 2, 1, '미세먼지: 좋음')
        elif(value[6] < '80'):
            drawText(12, 975, 350, 2, 1, '미세먼지: 나쁨' )
        else:
            drawText(12, 975, 350, 2, 1, '미세먼지: 매우나쁨')

        if (value[7] < '15'):
            drawText(12, 975, 375, 2, 1, '초미세먼지: 좋음')
        elif (value[7] < '50'):
            drawText(12, 975, 375, 2, 1, '초미세먼지: 나쁨')
        else:
            drawText(12, 975, 375, 2, 1, '초미세먼지: 매우나쁨')

for key, value in dic.items():
    if (key == clist[iSearchIndex]):
        drawText(12, 975, 400, 2, 1, '시   간:' + value[7])
        drawText(13, 975, 425, 2, 1, '현제온도:' + value[0])
        if (value[2] <= '-100'):
            drawText(14, 975, 450, 2, 1, '최저온도: error(API data가 존재하지않습니다.)')
        else:
            drawText(14, 975, 450, 2, 1, '최고온도:' + value[2])
        if (value[3] <= '-100'):
            drawText(15, 975, 475, 2, 1, '최저온도: error(API data가 존재하지않습니다.)')
        else:
            drawText(15, 975, 475, 2, 1, '최저온도:' + value[3])
        drawText(16, 975, 500, 2, 1, '날   씨:' + value[4])

base_frm = Frame(window)
base_frm.pack()
InitSearchListBox()
InitTopText()
mainloop()
