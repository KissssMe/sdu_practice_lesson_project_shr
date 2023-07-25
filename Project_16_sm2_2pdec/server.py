import socket
from gmssl.sm2 import CryptSM2

# SM2公私钥对（使用默认曲线初始化加密工具时会自动生成）
public_key = '04cd6bd2cadbff81f8e3d6f8a11977cf1722e4febd9660aa9c1cbd8a78a2f8d5193408ca5d132512a412fc838d84f543cf9d4d06892a5278844c20a293b390f1e5'
private_key = '6f27241950903d0136c84f605d1565470525255bf8c321ecba7c748e57c8b7d6'

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
server_socket.bind(("localhost", 8888))

# 开始监听连接
server_socket.listen(1)

while True:
   print('等待连接...')
   client_socket, addr = server_socket.accept()

   print(f'接收到来自 {addr} 的连接')

   # 对接收到的消息进行解密
   crypt_sm2 = CryptSM2(private_key=private_key,public_key=public_key)
   encrypted_data = client_socket.recv(2048)
   decrypted_data = crypt_sm2.decrypt(encrypted_data)
   print('解密后的数据:', decrypted_data)

   client_socket.close()
