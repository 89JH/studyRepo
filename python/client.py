#네트워크
'''
통신조건
-네트워크 연결유지
-주소필요(IP)
-통신장치필요(socket) ex)전화기
sender / receiver

소켓 간 패킷을 통해 데이터 전송

client        --------------        server
socket  패킷 - 패킷 - 패킷 -listner socket

TCP/IP : 송/수신 확인함 (통신속도가 느림(send / receive 확인을 해야하니..))
UDP : 송수신 확인하지 않음(통신속도가 빠름(send/ receive 확인을 안하니..))
'''
import socket

#서버 IP & PORT
ip = '172.30.108.77'
port = 9999

#클라이언트 소켓 준비
client = socket.socket()

#서버 접속
client.connect(ip, port)
print('------ Servier is connected ------')










