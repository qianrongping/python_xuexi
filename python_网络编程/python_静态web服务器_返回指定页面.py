import socket


def main():
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

        # 判断接收数据的长度是否为0
        if len(recv_data) == 0:
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_content = recv_data.decode('utf-8')
        print(recv_content)

        # 对数据 按照 空格 进行 分割
        request_list = recv_content.split(' ', maxsplit=2)
        # 获取请求的资源路径
        request_path = request_list[1]
        print(request_path)

        # 判断请求的路径是否是根目录，如果是根目录设置返回的信息
        if request_path == '/':
            request_path = '/index.html'
        try:
            # 打开文件读取文件中的数据
            with open('static' + request_path, 'rb') as file:
                rile_data = file.read()
        except Exception as e:
            # 响应行
            response_line = 'HTTP/1.1 400 NOT Found\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'

            with open('static/error.html', 'rb') as file:
                rile_data = file.read()

            # 响应体
            response_body = rile_data

            # 把数据封装成http响应报文格式的数据
            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            # 发送给浏览器的响应报文数据
            new_socket.send(response)

        else:
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'
            # 响应体
            response_body = rile_data

            # 把数据封装成http响应报文格式的数据
            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body
            # 发送给浏览器的响应报文数据
            new_socket.send(response)

        finally:
            new_socket.close()


if __name__ == '__main__':
    main()
