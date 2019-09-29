from tkinter import *

class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title('위젯 데모')

        frame1 = Frame(window)
        frame1.pack()

        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = '굵게', variable=self.v1, command=self.processCheckbutton)
        
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text='빨간색', bg='red', variable=self.v2, value=1, command=self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text='노란색', bg='yellow', variable=self.v2, value=2, command=self.processRadiobutton)
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

    def processCheckbutton(self):
        print('체크버튼이' + ( '선택되었습니다' if self.v1.get() == 1 else '해제되었습니다'))

    def processRadiobutton(self):
        print(('빨간색' if self.v2.get() == 1 else '노란색') + '이 선택되었습니다.')

WidgetsDemo()

