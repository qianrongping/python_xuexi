import socket

if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用，程序退出立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(('', 9000))
    # 设置监听
    tcp_server_socket.listen(128)

    # 玄幻等待接收客户端请求
    while True:
        # 等待客户端的连接请求
        new_socket, ip_pot = tcp_server_socket.accept()
        # 接收客户端的请求信息
        recv_data = new_socket.recv(4096)
        print(recv_data)

        # 打开文件读取文件中的数据
        with open('static/index.html') as file:
            rile_data = file.read()

        # 响应行
        response_line = 'HTTP/1.1 200 OK\r\n'
        # 响应头
        response_header = 'Server: PWS/1.0\r\n'
        # 响应体
        response_body = rile_data

        # 把数据封装成http响应报文格式的数据
        response = response_line + response_header + '\r\n' + response_body
        # 把字符串编码成二进制
        response_data = response.encode('utf-8')
        # 发送给浏览器的响应报文数据
        new_socket.send(response_data)
        new_socket.close()
