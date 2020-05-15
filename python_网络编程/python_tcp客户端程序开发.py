import socket

if __name__ == '__main__':
    # 1 创建tcp客户端套接字
    # AF_INET:ipv4地址类型
    # SOCK_STREAM: tcp传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2 和服务器端套接字建立连接
    tcp_client_socket.connect(('192.168.231.1',8080))

    send_content = '你好，我是客户端小白！！'
    # 对字符串编码转换为二进制数据
    send_data = send_content.encode('gbk')

    # 3 发送数据到服务端
    tcp_client_socket.send(send_data)

    # 4 接收服务端的数据
    # 1024：表示每次接收的最大值
    recv_data = tcp_client_socket.recv(1024)
    # 对二进制数据解码
    recv_content = recv_data.decode('gbk')
    print('接收服务端的数据为：', recv_content)

    # 5 关闭套接字
    tcp_client_socket.close()
