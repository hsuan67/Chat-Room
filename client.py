import socket
import threading

def recv(sock, addr):   # UDP 連線在接收訊息前先 send 一次，讓系統知道所佔 port
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))

def send(sock, addr):
    while True:
        string = input('')
        message = name + ' : ' + string
        data = message.encode('utf-8')
        sock.sendto(data, addr)
        if string.lower() == 'EXIT'.lower():
            break

def main():   # 通過 multithreading 實現多個 client 端之間的通訊
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('127.0.0.1', 9999)
    tr = threading.Thread(target=recv, args=(s, server), daemon=True)
    ts = threading.Thread(target=send, args=(s, server))
    tr.start()
    ts.start()
    ts.join()
    s.close()

if __name__ == '__main__':
    print("----- Welcome to the chat room! Type 'exit' to leave.-----")
    name = input('Please enter your name:')
    print('-----------------%s------------------' % name)
    main()