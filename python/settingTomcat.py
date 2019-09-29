from tkinter import * 
import tkinter.messagebox as mb
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from ftplib import FTP
import os
import sys
import ctypes
import urllib.parse
import xml.etree.ElementTree as elemTree
import socket
import subprocess

import collections
import re

import time

portData = {}
class settingTomcat(Frame):
    returnVal = ''
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('톰캣 자동세팅')
        self.pack(fill=BOTH, expand=True)

        #CATALINA_HOME 버튼 + 조회하여 가져오는 text area
        frame01 = Frame(self)
        frame01.pack(fill=X)

        btn_cat = Button(frame01, text='CATALINA_HOME%', command=lambda:catPush())
        btn_cat.grid(row=0, column=0, sticky=W)
        #btn_cat.pack()

        #한줄 띄우기용
        #Label(frame01).pack()

        text_cat = ScrolledText(frame01, width=40, height=10)
        text_cat.grid(row=1, columnspan=4)
        #text_cat.pack()

        #한줄 띄우기용
        #Label(frame01).pack()
        Label(frame01).grid(row=3)
        
        pathRec_label = Label(frame01, text='추천환경변수명')
        pathRec_label.grid(row=4, column=0, sticky=W)
        pathRec_entry = Entry(frame01, width=25)
        pathRec_entry.grid(row=4, column=1, columnspan=2)

        pathNm_label = Label(frame01, text='환경변수명')
        pathNm_label.grid(row=5, column=0, sticky=W)
        #pathNm_label.pack(side=LEFT, anchor=N, padx=10, pady=10)
        pathNm_entry = Entry(frame01, width=25)
        pathNm_entry.grid(row=5, column=1, columnspan=2)

        pathEnv_label = Label(frame01, text='환경변수경로')
        pathEnv_label.grid(row=6, column=0, sticky=W)
        pathEnv_entry = Entry(frame01, width=25)
        pathEnv_entry.grid(row=6, column=1, columnspan=2)

        btn_addPath = Button(frame01, text='환경변수추가', command=lambda:btnPath01())
        btn_addPath.grid(row=7, column=0, sticky=W)
        btn_addTomcat = Button(frame01, width=25, text='톰캣폴더복사', command=lambda:btnTomcat())
        btn_addTomcat.grid(row=7, column=1, columnspan=2)

        btn_portCheck = Button(frame01, text='톰캣포트확인', command=lambda:btnPcheck())
        btn_portCheck.grid(row=8, column=0, sticky=W)
        portCheck_label = Label(frame01, text='※8080포트들만 확인합니다.')
        portCheck_label.grid(row=8, column=1, columnspan=2, sticky=W)
        portCheck_entry = Entry(frame01, width=42)
        portCheck_entry.grid(row=9, columnspan=3)
        
        #한줄 띄우기용
        #Label(frame01).pack()
        portComment_label01 = Label(frame01, text='※포트자동 변경은 Connector포트의 뒷자리가\n8080일때만 유효합니다. 그 외 포트들은\n직접 server.xml파일을 열어 수정하는 것을 추천합니다.')
        portComment_label01.grid(row=10, column=0, columnspan=3, sticky=W)

        portRecommend_label = Label(frame01, text='추천port(Connector)')
        portRecommend_label.grid(row=11, column=0, sticky=W)
        portRecommend_entry = Entry(frame01, width=25)
        portRecommend_entry.grid(row=11, column=1, columnspan=2)

        portShutdown_label = Label(frame01, text='Shutdown Port')
        portShutdown_label.grid(row=12, column=0, sticky=W)
        portShutdown_entry = Entry(frame01, width=10)
        portShutdown_entry.grid(row=12, column=1, sticky=W)
        portShutdown_label2= Label(frame01, text='default : 8005')
        portShutdown_label2.grid(row=12, column=2, sticky=W)

        portRedirect_label = Label(frame01, text='Redirect Port')
        portRedirect_label.grid(row=13, column=0, sticky=W)
        portRedirect_entry = Entry(frame01, width=10)
        portRedirect_entry.grid(row=13, column=1, sticky=W)
        portRedirect_label2 = Label(frame01, text='default : 8443')
        portRedirect_label2.grid(row=13, column=2, sticky=W)

        portAJP_label = Label(frame01, text='AJP/1.3 Port')
        portAJP_label.grid(row=14, column=0, sticky=W)
        portAJP_entry = Entry(frame01, width=10)
        portAJP_entry.grid(row=14, column=1, sticky=W)
        portAJP_label2 = Label(frame01, text='default : 8009')
        portAJP_label2.grid(row=14, column=2, sticky=W)

        btn_addConfig = Button(frame01, width=42, text='위 설정대로 server.xml 파일 세팅', command=lambda:btnConfig())
        btn_addConfig.grid(row=15, column=0, columnspan=3)

        #외부 프로그램 실행 - os.system('notepad')
        #btn_notepad = Button(frame01, text='노트패트열기', command=lambda:btnNotePad()).pack()   
        #btn_cmd = Button(frame01, text='CMD열기', command=lambda:btnCMD()).pack()

        def catPush():
            #컴퓨터의 환경변수 목록 가져오기
            #sValue = os.environ['JAVA_HOME'] <- 환경변수명 JAVA_HOME인 것 가져오기
            sKeys = os.environ.keys()
            
            #운영시에는 'CATALINA_HOME' 으로 변경
            sorted(sKeys)
            maxValue = 'JAVA_HOME'
            maxNum = 0

            for item in sKeys:

                if 'JAVA_HOME' in item:
                    if maxValue < item:
                        maxValue = item

                    sValue = os.environ[item]
                    text_cat.insert('end', '-' + item + '\n' +sValue + '\n')

            maxNum = str(int(maxValue[9:]) + 1)
            returnVal = maxValue.replace(maxValue[9:], maxNum)
            pathRec_entry.insert('end', returnVal)
            print('cat버튼클릭')

        def btnPath01():
            #os.environ모듈도 환경변수를 세팅할 수 있을것 같긴한데...
            #env = os.environ['JAVA_HOME2']
            #newPath = r"C:\pythonTest;"# + env['JAVA_HOME2']
            #newPath = r''
            #env = newPath

            #pathNm = 'JAVA_HOME2'
            #entry창에 입력된 값을 가져온다
            pathNm = Entry.get(pathNm_entry)
            #setPath = 'C:\\Program Files\\apacheTest'
            setPath = Entry.get(pathEnv_entry)
            resultPath = 'SETX {0} "{1}" /M'.format(pathNm, setPath)
            #포트확인
            #'netstat -ano | findstr 8080'

            print('resultPath = ' + resultPath)
            os.system(resultPath)

            print('환경변수추가버튼 클릭')

        def btnTomcat():
            #print(svIp)
            #print(svDir)
            ftp = FTP()
            data = []

            try:
                ftp.connect(IP, 포트)
                ftp.login(아이디, 비밀번호)
                ftp.cwd('/tomcatTest')
                #ftp.cwd('/')

                #print(filenames)
                print('ftp연결 성공')

            except Exception as E:
                print('ftp연결 실패-' + E)

            print(ftp.pwd())
            
            #filenames = ftp.nlst()

            try:
                data = ftp.nlst()
            except Exception as E:
                print(E)

            print('4')


        def btnConfig():
            print('----------------------------------시작----------------------------------')
            tomcatPath = 'D:\\Apache Software Foundation\\Tomcat 8.5\\conf'
            for (path, dir, files) in os.walk(tomcatPath):
                for fileNames in files:
                    #아래 코드는 확장자만 찾아서 가져온다.
                    #배치파일 수정할때 필요할듯 싶어서 남겨둠
                    ext = os.path.splitext(fileNames)[-1]
                    if fileNames == 'server.xml':
                        #with open(fileNames, 'r') as f:
                        f = open(tomcatPath + "\\" + fileNames, 'r')
                        #lines = f.readlines()

                        tree = elemTree.parse(tomcatPath + '\\' + fileNames)
                        root = tree.getroot()

                        print(root.tag)
                        print(root.attrib)

                        test = tree.find('./Service')
                        test3 = tree.getiterator('service')
                        print('테스트333')
                        print(test3)
                        print('테스트3333')

                        test1 = test.find('Connector[2]')
                        test2 = test.find('Connector[1]')

                        print('테스트 태그 조회 시작')
                        print(test.tag)
                        print(test.attrib)
                        print('테스트 태그 조회 종료')

                        print('테스트 태그 조회 시작11111')
                        print(test1.tag)
                        print(test1.attrib)
                        print('테스트 태그 조회 종료11111')

                        print('테스트 태그 조회 시작22222')
                        print(test2.tag)
                        print(test2.attrib)
                        print('테스트 태그 조회 종료22222')

                        print('maxPort = ' + portData['maxPort'])
                        print('redirectPort = ' + portData['redirecPort'])
                        print('ajpPort = ' + portData['ajpPort'])


                        for port in root.iter('Server'):
                            print(port.get('port'))
                            #newPort = '5' + port.text
                            #port.text = newPort
                            #print('111111111111111111111 - ' + prePortNum)
                            #port.set('port' , prePortNum + port.get('port'))

                        print(test2.iter('port'))

                        for port2 in test.iter('port'):
                            print('테스트 태그 조회 시작33333')
                            print(port2.get('port'))
                            print('테스트 태그 조회 종료33333')
                        
                        tree.write('D:\\server222.xml')     

                        #tree.write('C:\\Users\\Choi.JH\\Documents\\server111.xml')

                        #for test in root.findall('port'):
                        #    print('11111111111111111111111')
                        #    port = test.find('port').text
                        #    print(port)



                        #tree.write('C:\\Program Files\\Apache Software Foundation\\Tomcat 8.5\\conf\\server.xml')

                        #for child in root:
                        #    print(child.tag)

                        for test in root.iter('GlobalNamingResources'):
                            print(test)

                        #print(lines)
                        #for line in lines:
                        #    if 'Server' in line:
                        #        print(lines)
            
            print('-----------------------------------끝----------------------------------')


        def btnPcheck():
            hosts = ['127.0.0.1','0.0.0.0']
            ports = [8080]
            '''
            for host in hosts:
                for port in ports:
                    try:
                        print('[+] Connection to ' + host + ':' + str(port))
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect_ex((host, port))
                        banner = s.recv(1024)
                        if banner:
                            print('[+] Port ' + str(port) + ' open:' + banner)
                        s.close()
                    except:
                        pass
            '''

            #포트 8080 대상목록 .txt 파일로 저장
            os.system('netstat -anp tcp | findstr 8080 >> d:\\test.txt')

            filePath = 'D:\\test.txt'
            ipnPort = re.findall(r'\d+[.]\d+[.]\d+[.]\d+[:]\d+', open(filePath).read().lower())

            data = []
            for x,y in collections.Counter(ipnPort).most_common():
                data.append(int(str(x).rpartition(':')[2]))

            os.remove('D:\\test.txt')
            if len(data) == 0:
                mb.messagebox.showerror("오류", "현재 오픈되어있는 8080포트가 존재하지 않습니다.")
                return

            data.remove(0)
            maxPort = str(max(data))

            for item in data:
                portCheck_entry.insert('end', str(item) + ',')
            
            #마지막 ',' 제거
            newPortVal = portCheck_entry.get()[:-1]
            #entry에 입력되어있는 모든값 제거
            portCheck_entry.delete(0, END)
            #entry에 마지막 ',' 제거한 값 입력
            portCheck_entry.insert('end', newPortVal)

            #global 문을 사용하여 전역변수로 사용할 수도 있지만,
            #global 문은 사용하지 않는 것을 추천한다..
            #global 문을 사용하는 것은 함수가 매개 변수와 반환값을 이용해 외부와 소통하는 자연스러운 흐름을 깨트리는 것이다..
            #global returnPort
            #returnPort = prePortNum + '8080'
            #shutdownPort = prePortNum + '8005'
            #global redirectPort 
            #redirectPort = prePortNum + '8443'
            #global ajpPort 
            #ajpPort = prePortNum + '8009'

            prePortNum = str(int(maxPort[:1])+1)
            portData['maxPort'] = prePortNum + '8080'
            #portData['shtdownPort'] = prePortNum + '8005'
            portData['redirecPort'] = prePortNum + '8443'
            portData['ajpPort'] = prePortNum + '8009'
            
            if int(portData['maxPort'])>65535:
                mb.messagebox.showerror("오류", "포트 범위 초과")
                portData['maxPort'] = ''

            if int(portData['redirecPort']) > 65535:
                mb.messagebox.showerror("오류", "포트 범위 초과")
                portData['redirecPort'] = ''
            
            if int(portData['ajpPort']) > 65535:
                mb.messagebox.showerror("오류", "포트 범위 초과")
                portData['ajpPort'] = ''
            
            portRecommend_entry.insert('end', portData['maxPort'])
            portShutdown_entry.insert('end', '-1')
            portRedirect_entry.insert('end', portData['redirecPort'])
            portAJP_entry.insert('end', portData['ajpPort'])

        def btnNotePad():
            os.system('notepad')
            print('노트패드버튼 클릭')

        def btnCMD():
#            os.system('run')
            print('CMD열기')

''' 첫번째 - 관리자 권한으로 실행하기, 이 방법을 사용하면
    2개의 프로그램이 실행된다.. 관리자모드, 일반모드
    왜 2개가 실행되는지는 더 공부 필요...
    추가로, 관리자모드의 파이썬 커맨드(?)창이 뒤에 뜬다..
def runAdmin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32

    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    
    if hasattr(sys, '_MEIPASS'):
        #Support pyinstaller Wrapped program.
        arguments = argv[1:]
    else:
        arguments = argv

    argument_line = u' '.join(arguments)
    executable = sys.executable

    if debug:
        print('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u'runas', executable, argument_line, None, 1)

    if int(ret) <= 32:
        return False
    return None
'''

''' 두번째
    - 관리자 모드로 실행하는 부분이다. 어떤 원리로 실행되는지는 더 공부 필요..
    참고 싸이트 url
    https://code-examples.net/ko/q/12c2d20
'''

#여러 프레임을 사용할때 사용하려고 만들어놈.. 다음에 공부하고 코딩
class nextFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('톰캣 자동세팅')
        self.pack(fill=BOTH, expand=True)

        #CATALINA_HOME 버튼 + 조회하여 가져오는 text area
        frame02 = Frame(self)
        frame02.pack(fill=X)
        

def elevate():
    import ctypes, win32com.shell.shell, win32event, win32process
    
    outPath = r'%s\%s.out' % (os.environ["TEMP"], os.path.basename(__file__))

    if ctypes.windll.shell32.IsUserAnAdmin():
        if os.path.isfile(outPath):
            sys.stderr = sys.stdout = open(outPath, 'w', 1)
        return
    with open(outPath, 'w+', 1) as outfile:
        hProc = win32com.shell.shell.ShellExecuteEx(lpFile=sys.executable, \
            lpVerb='runas', lpParameters=' '.join(sys.argv), fMask=64, nShow=0)['hProcess']

        while True:
            hr = win32event.WaitForSingleObject(hProc, 40)
            while True:
                line = outfile.readline()
                if not line: break
                sys.stdout.write(line)
            if hr != 0x102: break
    os.remove(outPath)
    sys.stderr = ''
    sys.exit(win32process.GetExitCodeProcess(hProc))

def main():
    base = Tk()
    # width x height + x축 + y축
    base.geometry('300x700+100+100')    
    app = settingTomcat(base)
    base.mainloop()

if __name__ == '__main__':
    #첫번째 방법을 사용할때...
    #ret = runAdmin()
    #if ret is True or ret is None:
    #    main()
    #else:
    #    print('Error(ret=%d): cannot elevate privilege' % (ret,))
    #    print('Error')

    #두번째 방법 사용
    #실제 사용시에는 주석 제거
    #elevate()
    main()
