import socket
import threading


# 处理客户端请求的任务
def handle_client_request(ip_port, service_client_socket):
    # 代码执行到此，说明建立成功
    print('客户端的ip地址和端口号：', ip_port)

    while True:
        # 接受客户端发送的数据，这次接受数据的最大字节是1024
        recv_data = service_client_socket.recv(1024)
        if recv_data:
            # 获取数据的长度
            recv_data_length = len(recv_data)
            print('接受数据的长度为：', recv_data_length)

            # 对二进制数据进行解码
            recv_content = recv_data.decode('gbk')
            print('接受客户端的数据为：', recv_content, ip_port)

            # 准备发送数据
            send_data = 'OK,问题正在处理中'.encode('gbk')
            service_client_socket.send(send_data)
        else:
            print('客户端下线了：', ip_port)
            break
    # 关闭服务器与客户端的套接字，终止和客户端的通信
    service_client_socket.close()


if __name__ == '__main__':
    # 1 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2 设置端口号复用，让程序退出端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 给程序绑定端口号
    tcp_server_socket.bind(('', 8080))

    # 设置监听
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端建立连接的请求, 只有客户端和服务端建立连接成功代码才会解阻塞，代码才能继续往下执行
        # 1. 专门和客户端通信的套接字： service_client_socket
        # 2. 客户端的ip地址和端口号： ip_port
        service_client_socket, ip_port = tcp_server_socket.accept()

        # 当客户端和服务端连接成功，创建一个子线程，让子线程专门负责接收客户的小心
        sub_thread = threading.Thread(target=handle_client_request, args=(ip_port, service_client_socket))
        # 设置主进程退出，子线程销毁（守护主进程）
        sub_thread.setDaemon(True)
        sub_thread.start()

    # 关闭服务端的套接字，终止客户端提供建立请求的服务
    # tcp_server_socket.close()
