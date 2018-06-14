from tkinter import *
from tkinter import ttk

import requests
from bs4 import BeautifulSoup

#############################################################
#현재　날씨　출력
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000&mode=stdxm'
response = requests.get(url)
soup = BeautifulSoup(response.text,' html.parser ')

mylist=soup.select('dd.now_weather1_right')
mylist=str(mylist)
mylist=mylist.split(' , ')
templist=[]

for i in range(len(mylist)):
        templist.append(mylist[i][mylist[i].index('right'),7:])
for i in range(len(templist)):
        templist[i]=templist[i].replace('</dd>',' ')
templist[0]=templist[0][templist[0].index('>'),1:]
templist[1]=templist[1][:-1]

Current_temperature=templist[0]
Current_precipitation=templist[1]

Current_weather='●현재　날씨●'
Current_temperature = '   온도 :    ',Current_temperature
Current_precipitation = '강수량 :　　　', Current_precipitation


url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000&mode=stdxm'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

mylist=soup.select('dd.now_weather1_left.icon')
mylist=str(mylist)
mylist=mylist.split(',')
mylist=mylist[0]
Weather_Description=mylist[mylist.index('alt="'), 5:mylist.index('src')-16]

a = Tk()

#제목
label=ttk.Label(a,text="현재　서울　날씨를　알려드리겠습니다")
label.pack()
label.config(foreground = 'black', background = 'white')
label.config(font=('현대하모니　L',11,'bold'))


#이미지를　x,　y좌표에　보여주기
lbl2=ttk.Label(a,text='image　place')
lbl2.pack()
lbl2.config(justify=LEFT)
img=PhotoImage(file = 'C:\\Users\\윤상\\PycharmProjects\\Weather Project\\맑음.gif')
img=img.subsample(2,2)
lbl2.img=img
lbl2.config(image=lbl2.img)
lbl2.config(justify=LEFT)
lbl2.place(x=10, y=75)
lbl2.configure(background='black')

#날씨　정보
Weather=ttk.Label(a,text=Current_weather)
Temperature=ttk.Label(a,text=Current_temperature)
Precipitation=ttk.Label(a,text=Current_precipitation)
Description=ttk.Label(a,text=Weather_Description)

#날씨　정보　위치
Weather.place(x=150,y=70)
Temperature.place(x=150,y=90)
Precipitation.place(x=150,y=150)
Description.place(x=10,y=50)

#날씨　정보　백그라운드　색갈
Weather.configure(background='white')
Temperature.configure(background='white')
Precipitation.configure(background='white')
Description.configure(background='white')
Description.config(font=('현대하모니　L' ,11,'bold'))


#확인　버튼

def close_window():
        a.destroy()

btn=Button(a,text="확인",command=close_window,width=12)
btn.place(x=160,y=180)


a.title('서울　날씨')
a.geometry('280x220 600 350')
a.configure(background = 'white')
a.mainloop()