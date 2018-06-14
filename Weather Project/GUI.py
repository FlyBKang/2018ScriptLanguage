from tkinter import *
from tkinter import font
import tkinter.messagebox


window = Tk()
window.title("날씨 프로그램")
window.geometry("600x500+750+200")
DataList = []

photo = PhotoImage(file = "KR 지도.png" )
imageLabel = Label(window, image=photo)
imageLabel.pack()

def InitTopText():
    TempFont = font.Font(window, size = 15, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="전국 날씨 찾기")
    MainText.pack()
    MainText.place(x = 10, y = 10)
    MainText.configure(background = 'white')


def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=550, y=50)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "서울(대방)")
    SearchListBox.insert(2, "인천(부평)")
    SearchListBox.insert(3, "대전(동구")
    SearchListBox.insert(4, "가평")
    SearchListBox.insert(5, "강릉")
    SearchListBox.insert(6, "독도")
    SearchListBox.insert(7, "대구")
    SearchListBox.insert(8, "부산")
    SearchListBox.insert(9, "제주")
    SearchListBox.insert(10, "광주")
    SearchListBox.insert(11, "전주")
    SearchListBox.pack()
    SearchListBox.place(x = 410, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(window, font = TempFont, text = "검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=500, y=110)


def SearchButtonAction():
    global SearchListBox

    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
        pass
    elif iSearchIndex == 2:
        pass
    elif iSearchIndex == 3:
        pass
    elif iSearchIndex == 4:
        pass
    elif iSearchIndex == 5:
        pass
    elif iSearchIndex == 6:
        pass
    elif iSearchIndex == 7:
        pass
    elif iSearchIndex == 8:
        pass
    elif iSearchIndex == 9:
        pass
    elif iSearchIndex == 10:
        pass


def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes

            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes

                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass
                        if tel[0] is not '0':
                            tel = "02-" + tel
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))

InitTopText()
InitSearchListBox()
InitSearchButton()


window.mainloop()