from tkinter import *
from tkinter.ttk import *

class settingTomcat(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('톰캣 자동세팅')
        self.pack(fill=BOTH, expand=True)

        #CATALINA_HOME 버튼 + 조회하여 가져오는 text area
        frame01 = Frame(self)
        frame01.pack(fill=X)

        btn_cat = Button(frame01, text='CATALINA_HOME%')
        btn_cat.pack()

def main():
    base = Tk()
    base.geometry('300x300')
    app = settingTomcat(base)
    base.mainloop()

if __name__ == '__main__':
    main()