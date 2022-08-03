import socket
import logging

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # 建立 socket 物件

    addr = ('127.0.0.1', 9999)
    s.bind(addr)    # 將 socket 實際綁定到本機的某個 port 上

    logging.info('UDP Server on %s:%s...', addr[0], addr[1])

    user = {}  # 存放字典{addr:name}
    while True:
        try:
            data, addr = s.recvfrom(1024)  # 等待接收 client 端訊息存放在 2 個變數 data 和 addr 裡
            if not addr in user:
                for address in user:
                    s.sendto(data + ' enter the chat room...'.encode('utf-8'), address)  # 傳送 user 字典的 data 和 address 到 client 端
                user[addr] = data.decode('utf-8')  # 接收的訊息解碼成 utf-8 並存在字典 user 裡，鍵名定義為 addr
                continue  # 若 addr 在 user 字典裡，則跳過本次迴圈

            if 'EXIT'.lower() in data.decode('utf-8'):
                name = user[addr]
                user.pop(addr)      # 刪除 user 裡的 addr
                for address in user:
                    s.sendto((name + ' leave the chat room...').encode(), address)     # 傳送 name 和 address 到 client 端
            else:   
                print('"%s" from %s:%s' %(data.decode('utf-8'), addr[0], addr[1]))  
                for address in user:
                    if address != addr:
                        s.sendto(data, address)

        except ConnectionResetError:
            logging.warning('Someone left unexcept.')

if __name__ == '__main__':
    main()