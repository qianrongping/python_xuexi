import socket
import threading
import sys
import python_framework


class HttpWebServer(object):
    def __init__(self, oprt):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用，程序退出立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(('', oprt))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod  # 设置为静态方法
    def handle_client_request(new_socket):
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

        # 判断是否是动态资源请求,以后把后缀是.html的请求任务是动态资源请求
        if request_path.endswith(".html"):
            """动态资源请求"""
            # 动态资源请求找web框架进行处理,需要把请求参数给web框架
            # 准备给web框架的参数信息,都要放到字典里面
            env = {
                'request_path': request_path
                # 传入请求头信息
            }
            # 使用框架处理动态资源请求,web框架需要把处理结果返回给web服务器,web服务器负责把返回的结果封装成报文发送给浏览器
            status, headers, response_body = python_framework.handle_request(env)
            print(status, headers, response_body)
            # 相应行
            response_line = "HTTP/1.1 %s\r\n" % status
            # 响应头
            response_header = ""
            for header in headers:
                response_header += "%s: %s\r\n" % header

            # 拼接响应报文
            response_data = (response_line + response_header + "\r\n" + response_body).encode('utf-8')

            # 发送报文
            new_socket.send(response_data)
            # 关闭连接
            new_socket.close()
        else:
            """静态资源请求"""

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

    def sub_stat(self):
        # x循环等待接收客户端请求
        while True:
            # 等待客户端的连接请求
            new_socket, ip_pot = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 守护主线程
            sub_thread.setDaemon(True)
            # 启动线程
            sub_thread.start()


def main():
    # params = sys.argv
    # # 判断命令行参数是否是2 个
    # if len(params) != 2:
    #     print('命令行参数格式如下：python3 xxx.py 9000')
    #
    # # 判断第二个参数是否是数字
    # if not sys.argv[1].isdigit():
    #     print('命令行参数格式如下：python3 xxx.py 9000')
    #
    # oprt = int(sys.argv[1])
    web_server = HttpWebServer(8000)
    web_server.sub_stat()


if __name__ == '__main__':
    main()
