import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import *
from ftplib import FTP
import os
import sys
import ctypes
import urllib.parse
import xml.etree.ElementTree as elemTree
import collections
#lxml 라이브러리는 xml파일을 그대로 출력해준다.
#파이썬 xml 라이브러리를 그냥 사용하게되면 xml을 수정해서 write할때 알파벳 순서대로 다시 정렬하여 수정된다.
import lxml.etree as etree

# 파일 및 디렉토리 복사할때사용하는 library
import shutil, errno

portData = {}
pathData = {}

class settingTomcat(Frame):
    returnVal = ''

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('톰캣 자동세팅')
        self.pack(fill=BOTH, expand=True)

        # CATALINA_HOME 버튼 + 조회하여 가져오는 text area
        frame01 = tk.Frame(self)
        frame01.pack(fill=X)

        btn_cat = Button(frame01, text='CATALINA_HOME%', command=lambda: catPush())
        btn_cat.grid(row=0, column=0, sticky=W)
        # btn_cat.pack()

        # 한줄 띄우기용
        # Label(frame01).pack()

        text_cat = ScrolledText(frame01, width=40, height=10)
        text_cat.grid(row=1, columnspan=4)
        # text_cat.pack()

        projectNm_label = Label(frame01, text='프로젝트명')
        projectNm_label.grid(row=3, column=0, sticky=W)
        projectNm_entry = Entry(frame01, width=25)
        projectNm_entry.grid(row=3, column=1, columnspan=2)

        pathRec_label = Label(frame01, text='추천환경변수명')
        pathRec_label.grid(row=4, column=0, sticky=W)
        pathRec_entry = Entry(frame01, width=25)
        pathRec_entry.grid(row=4, column=1, columnspan=2)

        pathNm_label = Label(frame01, text='환경변수명')
        pathNm_label.grid(row=5, column=0, sticky=W)
        # pathNm_label.pack(side=LEFT, anchor=N, padx=10, pady=10)
        pathNm_entry = Entry(frame01, width=25)
        pathNm_entry.grid(row=5, column=1, columnspan=2)

        pathEnv_label = Label(frame01, text='환경변수경로')
        pathEnv_label.grid(row=6, column=0, sticky=W)
        pathEnv_entry = Entry(frame01, width=25)
        pathEnv_entry.grid(row=6, column=1, columnspan=2)

        btn_addPath = Button(frame01, text='환경변수추가', command=lambda: btnPath01())
        btn_addPath.grid(row=7, column=0, sticky=W)
        btn_addTomcat = Button(frame01, width=25, text='톰캣폴더복사', command=lambda: btnTomcat())
        btn_addTomcat.grid(row=7, column=1, columnspan=2)

        btn_portCheck = Button(frame01, text='톰캣포트확인', command=lambda: btnPcheck())
        btn_portCheck.grid(row=8, column=0, sticky=W)
        portCheck_label = Label(frame01, text='※8080포트들만 확인합니다.')
        portCheck_label.grid(row=8, column=1, columnspan=2, sticky=W)
        portCheck_entry = Entry(frame01, width=42)
        portCheck_entry.grid(row=9, columnspan=3)

        # 한줄 띄우기용
        # Label(frame01).pack()
        portComment_label01 = Label(frame01,
                                    text='※포트자동 변경은 Connector포트의 뒷자리가\n8080일때만 유효합니다. 그 외 포트들은\n직접 server.xml파일을 열어 수정하는 것을 추천합니다.\n(포트의범위는 65535까지입니다.)')
        portComment_label01.grid(row=10, column=0, columnspan=3, sticky=W)

        portRecommend_label = Label(frame01, text='추천port(Connector)')
        portRecommend_label.grid(row=11, column=0, sticky=W)
        portRecommend_entry = Entry(frame01, width=25)
        portRecommend_entry.grid(row=11, column=1, columnspan=2)

        portShutdown_label = Label(frame01, text='Shutdown Port')
        portShutdown_label.grid(row=12, column=0, sticky=W)
        portShutdown_entry = Entry(frame01, width=10)
        portShutdown_entry.grid(row=12, column=1, sticky=W)
        portShutdown_label2 = Label(frame01, text='default : 8005')
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

        path_entry = Entry(frame01, width=42)
        path_entry.grid(row=15, columnspan=3)

        btn_addConfig = Button(frame01, width=42, text='위 설정대로 server.xml 파일 세팅', command=lambda: btnConfig())
        btn_addConfig.grid(row=16, column=0, columnspan=3)

        btn_setContext = Button(frame01, width=42, text='context(DB정보), isapi(IIS연동) 세팅', command=lambda: btnContext())
        btn_setContext.grid(row=17, column=0, columnspan=3)

        btn_setBat = Button(frame01, width=42, text='.bat 파일 세팅', command=lambda: btnSetBat())
        btn_setBat.grid(row=18, column=0, columnspan=3)

        btn_release95 = Button(frame01, width=42, text='개발(95)서버 배포(구현X)', command=lambda: btnRelease95)
        btn_release95.grid(row=19, column=0, columnspan=3)
        btn_release = Button(frame01, width=42, text='운영(81,82,83)서버 배포(진행중)')
        btn_release.grid(row=20, column=0, columnspan=3)

        # 외부 프로그램 실행 - os.system('notepad')
        # btn_notepad = Button(frame01, text='노트패트열기', command=lambda:btnNotePad()).pack()
        # btn_cmd = Button(frame01, text='CMD열기', command=lambda:btnCMD()).pack()

        def catPush():
            # 컴퓨터의 환경변수 목록 가져오기
            # sValue = os.environ['JAVA_HOME'] <- 환경변수명 JAVA_HOME인 것 가져오기
            sKeys = os.environ.keys()

            # 운영시에는 'CATALINA_HOME' 으로 변경
            sorted(sKeys)
            maxValue = 'CATALINA_HOME'
            maxNum = 0

            for item in sKeys:

                if 'CATALINA_HOME' in item:
                    if maxValue < item:
                        maxValue = item

                    sValue = os.environ[item]
                    text_cat.insert('end', '-' + item + '\n' + sValue + '\n')

            maxNum = str(int(maxValue[13:]) + 1)
            returnVal = maxValue.replace(maxValue[13:], maxNum)
            pathRec_entry.insert('end', returnVal)
            print('cat버튼클릭')

        def btnPath01():
            # pathNm = 'JAVA_HOME2'
            # entry창에 입력된 값을 가져온다
            pathNm = Entry.get(pathNm_entry)
            # setPath = 'C:\\Program Files\\apacheTest'
            setPath = Entry.get(pathEnv_entry)
            resultPath = 'SETX {0} "{1}" /M'.format(pathNm, setPath)

            print('resultPath = ' + resultPath)
            os.system(resultPath)

            print('환경변수추가버튼 클릭')

        def btnTomcat():
            print('----------------------------------톰캣폴더복사 시작----------------------------------')
            if projectNm_entry.get().replace(' ', '') == '':
                messagebox.showerror('오류', '프로젝트명이 입력되지 않았습니다.')
                return

            # 개발서버에서 실행시 특정 폴더에서 복사해오는걸로 설정.. 테스트도 필요
            # 테스트용
            pathData['bDir'] = 'D:\\Apache Software Foundation'
            # 실제 운영용
            #pathData['bDir'] = 개발서버 특정 경로 지정해서 사용해보기.
            pathData['tDir'] = 'D:\\Apache Software Foundation' + '_' + projectNm_entry.get().replace(' ', '')

            try:
                shutil.copytree(pathData['bDir'], pathData['tDir'])
                path_entry.insert('end', pathData['tDir'])
            except OSError as E:
                if E.errno == errno.ENOTDIR:
                    shutil.copy(pathData['bDir'], pathData['tDir'])
                    path_entry.insert('end', pathData['tDir'])
                else:
                    # raise
                    messagebox.showerror('오류', E)
            print('----------------------------------톰캣폴더복사 종료----------------------------------')

        def btnConfig():
            print('----------------------------------server.xml 설정 시작----------------------------------')
            # 테스트용
            # 실제 개발/운영서버에는 톰캣 8.0 버전을 쓰고있으므로, 버전을 바꿔줘야한다.
            tomcatPath = pathData['tDir'] + '\\Tomcat 8.5\\conf'

            if tomcatPath == '':
                messagebox.showerror('오류', '경로가 지정되지 않았습니다.')
                return

            '''
            for문에 3개가 꼭있어야한다.
            왜냐하면 os.walk(tomcatPath)의 결과값이 경로/디렉토리/파일목록
            세가지로 분류되어 결과가 나온다.
            우리는 파일목록만 있으면 되는데, 파일목록만 뽑아내는 방법을 현재는 모름
            '''
            for (path, dir, files) in os.walk(tomcatPath):
                for fileNames in files:
                    # 아래 코드는 확장자만 찾아서 가져온다.
                    # 배치파일 수정할때 필요할듯 싶어서 남겨둠
                    # ext = os.path.splitext(fileNames)[-1]
                    if fileNames == 'server.xml':
                        file = tomcatPath + '\\' + fileNames
                        tree = elemTree.parse(file)

                        '''
                        #root tag정보 가져오는 방법
                        root = tree.getroot()
                        #root tag명을 가져오는 방법
                        root.tag
                        #root 속성 값들을 가져오는 방법
                        root.attrib
                        '''

                        root = tree.getroot()

                        # shutdown port - default : 8005
                        # shutdown port = '-1' 로 하면 shutdown 포트를 따로 사용하지 않는다는 의미.
                        # 톰캣을 여러개 띄우고(서비스가 여러개라서)있으므로 -1로 지정해서 사용하는게 편할듯하다.
                        print('-----------------------------------shutdown포트 설정 시작-----------------------------------')
                        for port in root.iter('Server'):
                            port.set('port', portShutdown_entry.get())
                        print('shutdownPort = ' + portShutdown_entry.get())
                        print('-----------------------------------shutdown포트 설정 완료-----------------------------------')

                        rService = tree.find('./Service')
                        # HTTP포트(8080)
                        conn01 = rService.find('Connector[1]')
                        # AJP포트(8009)
                        conn02 = rService.find('Connector[2]')

                        print('-----------------------------------HTTP포트 설정 시작-----------------------------------')
                        for port in conn01.iter('Connector'):
                            port.set('port', portRecommend_entry.get())
                            port.set('redirectPort', portRedirect_entry.get())
                        print('httpPort = ' + portRecommend_entry.get())
                        print('httpRedirectPort = ' + portRedirect_entry.get())
                        print('-----------------------------------HTTP포트 설정 완료-----------------------------------')

                        print('-----------------------------------AJP/1.3포트 설정 시작-----------------------------------')
                        for port in conn02.iter('Connector'):
                            port.set('port', portAJP_entry.get())
                            port.set('redirectPort', portRedirect_entry.get())
                        print('ajpPort = ' + portAJP_entry.get())
                        print('ajpRedirectPort = ' + portRedirect_entry.get())
                        print('-----------------------------------AJP/1.3포트 설정 종료-----------------------------------')

                        # server.xml파일에 적용..
                        tree.write(file)

            print('----------------------------------server.xml 설정 종료----------------------------------')

        # ---------------------------------폼캣포트확인 버튼 클릭 시작---------------------------------
        def btnPcheck():
            print('----------------------------------톰캣포트확인 시작----------------------------------')
            # 포트 8080 대상목록 .txt 파일로 저장
            #운영용
            #os.system('netstat -anp tcp | findstr 8080 >> c:\\test.txt')

            #테스트용
            os.system('netstat -anp tcp | findstr 8080 >> d:\\test.txt')

            #실 운영용
            #filePath = 'c:\\test.txt'

            #테스트용
            filePath = 'd:\\test.txt'
            ipnPort = re.findall(r'\d+[.]\d+[.]\d+[.]\d+[:]\d+', open(filePath).read().lower())

            data = []
            for x, y in collections.Counter(ipnPort).most_common():
                data.append(int(str(x).rpartition(':')[2]))

            #실운영용
            #os.remove('c:\\test.txt')

            #테스트용
            os.remove('d:\\test.txt')
            if len(data) == 0:
                messagebox.showerror("오류", "현재 오픈되어있는 8080포트가 존재하지 않습니다.")
                return

            data.remove(0)
            maxPort = str(max(data))

            for item in data:
                portCheck_entry.insert('end', str(item) + ',')

            # 마지막 ',' 제거
            newPortVal = portCheck_entry.get()[:-1]
            # entry에 입력되어있는 모든값 제거
            portCheck_entry.delete(0, END)
            # entry에 마지막 ',' 제거한 값 입력
            portCheck_entry.insert('end', newPortVal)

            # global 문을 사용하여 전역변수로 사용할 수도 있지만,
            # global 문은 사용하지 않는 것을 추천한다..
            # global 문을 사용하는 것은 함수가 매개 변수와 반환값을 이용해 외부와 소통하는 자연스러운 흐름을 깨트리는 것이다..
            # global returnPort
            # returnPort = prePortNum + '8080'
            # shutdownPort = prePortNum + '8005'
            # global redirectPort
            # redirectPort = prePortNum + '8443'
            # global ajpPort
            # ajpPort = prePortNum + '8009'

            if len(maxPort) == 4: #포트의 자릿수가 4자리이면 앞에 1붙이기 ex)8080 -> return '1'
                prePortNum = '1'
            elif len(maxPort) == 5: #포트의 자릿수가 5자리이면 +1 하기 ex)18080 -> return '2'
                prePortNum = str(int(maxPort[:1]) + 1)

            portData['returnPort'] = prePortNum + '8080'
            # portData['shutdownPort'] = prePortNum + '8005'
            portData['shutdownPort'] = '-1'
            portData['redirectPort'] = prePortNum + '8443'
            portData['ajpPort'] = prePortNum + '8009'

            print(portData['returnPort'])
            print(portData['redirectPort'])
            print(portData['ajpPort'])

            if int(portData['returnPort']) > 65535:
                messagebox.showerror("오류", "포트 범위 초과")
                portData['returnPort'] = ''

            if int(portData['redirectPort']) > 65535:
                messagebox.showerror("오류", "포트 범위 초과")
                portData['redirectPort'] = ''

            if int(portData['ajpPort']) > 65535:
                messagebox.showerror("오류", "포트 범위 초과")
                portData['ajpPort'] = ''

            portRecommend_entry.insert('end', portData['returnPort'])
            portShutdown_entry.insert('end', portData['shutdownPort'])
            portRedirect_entry.insert('end', portData['redirectPort'])
            portAJP_entry.insert('end', portData['ajpPort'])

            print('----------------------------------톰캣포트확인 종료----------------------------------')

        # ---------------------------------폼캣포트확인 버튼 클릭 종료---------------------------------

        # .bat파일세팅 버튼 클릭 시작
        def btnSetBat():
            print('----------------------------------.bat파일 설정 시작----------------------------------')
            # 테스트용
            # 실제 개발/운영서버에는 톰캣 8.0 버전을 쓰고있으므로, 버전을 바꿔줘야한다.
            tomcatPath = pathData['tDir'] + '\\Tomcat 8.5\\bin'

            if tomcatPath == '':
                messagebox.showerror('오류', '경로가 지정되지 않았습니다.')
                return

            for (path, dir, files) in os.walk(tomcatPath):
                for fileNames in files:

                    # 아래 코드는 확장자만 찾아서 가져온다.
                    # 배치파일 수정할때 필요할듯 싶어서 남겨둠
                    ext = os.path.splitext(fileNames)[-1]
                    if ext == '.bat':
                        try:
                            with open(tomcatPath + '\\' + fileNames, 'r') as f:
                                newValue = pathRec_entry.get()
                                newline = []
                                for word in f.readlines():
                                    newline.append(word.replace('CATALINA_HOME', newValue))

                            with open(tomcatPath + '\\' + fileNames, 'w') as f:
                                for line in newline:
                                    f.writelines(line)
                        except Exception as E:
                            print(E)
                        finally:
                            f.close()

            print('----------------------------------.bat파일 설정 종료----------------------------------')

        # 개발서버 배포 버튼 클릭 시작
        def btnRelease95():
            print('개발서버배포')
            '''#FTP는 조금 더 공부해보고 반영하기
            ftp = FTP()
            data = []

            try:
                ftp.connect(IP, 포트)
                ftp.login(아이디, 비밀번호)
                ftp.cwd('/tomcatTest')
                #ftp.cwd('/')

                #print(filenames)
                print('ftp연결 성공')
                #filenames = ftp.nlst()

            except Exception as E:
                print('ftp연결 실패-' + E)
            '''
        # 개발서버 배포 버튼 클릭 종료
        
        #Context, isapi 설정 시작
        def btnContext():
            print('----------------------------------Context,isapi 설정 시작----------------------------------')
            # 테스트용
            # 실제 개발/운영서버에는 톰캣 8.0 버전을 쓰고있으므로, 버전을 바꿔줘야한다.
            tomcatPath = pathData['tDir'] + '\\Tomcat 8.5\\conf\\Catalina\\localhost'
            isapiPath = pathData['tDir'] + '\\Tomcat 8.5\\isapi'
            targetPath = pathData['tDir'] + '\\Tomcat 8.5'

            if tomcatPath == '':
                messagebox.showerror('오류', '경로가 지정되지 않았습니다.')
                return

            for (path, dir, files) in os.walk(tomcatPath):
                for fileNames in files:
                    
                    if fileNames == 'ROOT.xml':
                        file = tomcatPath + '\\' + fileNames
                        #tree = elemTree.parse(file)
                        try:
                            tree = etree.parse(file)
                        except Exception as E:
                            print(E)

                        root = tree.getroot()
                        # DB01
                        res01 = tree.find('Resource[1]')
                        # DB02 - 읽기전용
                        res02 = tree.find('Resource[2]')
                        
                        #웹소스 폴더
                        docPath = 'C:\\test'
                        #서비스 파일에 등록된 DB Connection명
                        dbNm01 = 'test_DB'
                        #서비스 파일에 등록된 DB Connection명(읽기전용)
                        dbNm02 = 'test_DB_R'
                        #DB접속정보(MSSQL)
                        dbUrl = 'jdbc:sqlserver://111.111.111.111:1433;databaseName=TEST'
                        #접속ID
                        dbId = 'test'
                        #접속PW
                        dbPw = 'test'

                        print('-----------------------------------Context 설정 시작-----------------------------------')
                        for con in root.iter('Context'):
                            con.set('docBase', docPath)
                        print('-----------------------------------Context 설정 종료-----------------------------------')

                        print('-----------------------------------Resource01 설정 시작(운영DB)-----------------------------------')
                        for res in res01.iter('Resource'):
                            #print(res.get('name'))
                            res.set('name', dbNm01)
                            res.set('url', dbUrl)
                            res.set('username', dbId)
                            res.set('password', dbPw)
                        print('-----------------------------------Resource01 설정 종료(운영DB)-----------------------------------')

                        print('-----------------------------------Resource02 설정 시작(읽기전용DB)-----------------------------------')
                        for res in res02.iter('Resource'):
                            #print(res.get('name'))
                            res.set('name', dbNm02)
                            res.set('url', dbUrl)
                            res.set('username', dbId)
                            res.set('password', dbPw)
                        print('-----------------------------------Resource02 설정 종료(읽기전용DB)-----------------------------------')

                        tree.write(file)

            for (path, dir, files) in os.walk(isapiPath):
                for fileNames in files:
                    if fileNames == 'isapi_redirect-1.2.31.properties':
                        try:
                            with open(isapiPath + '\\' + fileNames, 'r') as f:
                                newValue = targetPath
                                newline = []

                                for word in f.readlines():
                                    newline.append(word.replace('tomcatPath', newValue))

                            with open(isapiPath + '\\' + fileNames, 'w') as f:
                                for line in newline:
                                    f.writelines(line)
                        except Exception as E:
                            print(E)
                        finally:
                            f.close()            
            print('----------------------------------Context,isapi 설정 종료----------------------------------')


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


# 여러 프레임을 사용할때 사용하려고 만들어놈.. 다음에 공부하고 코딩
class nextFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('톰캣 자동세팅')
        self.pack(fill=BOTH, expand=True)

        # CATALINA_HOME 버튼 + 조회하여 가져오는 text area
        frame02 = Frame(self)
        frame02.pack(fill=X)


def elevate():
    '''
    window 기능을 사용하기 위해서는 win32com library가 있어야한다.
    python에서 pywin32 패키지를 설치하면 된다.
    아래 링크 - pywin32 - 버전선택 - 윈도우환경, 파이썬버전에 맞는 버전 선택하여 다운 후 설치

    https://sourceforge.net/projects/pywin32/files/?source=navbar

    설치 되었는지는, cmd창에서 파이썬 실행후
    import wind32com.clinet / import ctypes 등을 입력하여 정상 처리되는지 테스트해보면 된다.

    '''
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
    # app변수는 어디서 사용을할까..?
    # app = settingTomcat(base)
    settingTomcat(base)
    base.mainloop()


if __name__ == '__main__':
    # 첫번째 방법을 사용할때...
    # ret = runAdmin()
    # if ret is True or ret is None:
    #    main()
    # else:
    #    print('Error(ret=%d): cannot elevate privilege' % (ret,))
    #    print('Error')

    # 두번째 방법 사용
    # 실제 사용시에는 주석 제거
    #elevate()
    main()
