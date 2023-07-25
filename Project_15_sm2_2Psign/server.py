# Import the required modules
import socket
from gmssl import sm2, func

# 实例化SM2对象
private_key = '394020013c311000594feb02127d27a0e9c3ad213efb2923f4b5e5966c5a0534'
public_key = 'b3b72b1705a16bca014be2f90323accfe9275d3bd75101937b5deed8e35c6255b8abb5f7b2f9e56ae9c361b2f992fd9a8f7b28a4f8b3d6923f4ca870371c9067'
sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)

#服务端部分，用于生成签名
def server_side(socket):
    # 绑定socket到一个地址和端口
    server_address = ('localhost', 12345)
    sock.bind(server_address)

    # 监听连接
    print("服务器建立到",server_address,"的连接")
    sock.listen(1)

    # 当接收到连接请求时
    while True:
        # 接受一个连接
        connection, client_address = sock.accept()

        try:
            # 接收数据
            data = connection.recv(1024)
            if data:
                # 使用SM2签名算法生成签名
                random_hex_str = func.random_hex(sm2_crypt.para_len)
                sign = sm2_crypt.sign(data, random_hex_str)
                print("服务器生成签名：",sign)

                # 将签名编码为字节格式并发送给客户端
                connection.sendall(sign.encode('utf-8'))
            else:
                break
        finally:
            # 清理连接
            connection.close()

#客户端部分，用于验证签名
def client_side(socket):
    # 连接到服务器
    server_address = ('localhost', 12345)
    sock.connect(server_address)

    try:
        # 发送数据
        message = 'this is the message to be signed'
        sock.sendall(message)

        # 查看从服务器收到的签名
        data = sock.recv(1024)
        if data:
            # 验证签名
            if sm2_crypt.verify(data, message):
                print("the signature is valid")
            else:
                print("the signature is invalid")
    finally:
        # 关闭连接
        sock.close()

# 创建一个TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 根据需要调用server_side()或者client_side()
server_side(sock)
# client_side(sock)
