import socket
from gmssl.sm2 import CryptSM2

# 服务端的公钥（一般由服务端事先提供）
public_key = '04cd6bd2cadbff81f8e3d6f8a11977cf1722e4febd9660aa9c1cbd8a78a2f8d5193408ca5d132512a412fc838d84f543cf9d4d06892a5278844c20a293b390f1e5'
private_key = '6f27241950903d0136c84f605d1565470525255bf8c321ecba7c748e57c8b7d6'

# 创建 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect(("localhost", 8888))

# 对要发送的消息进行加密
plaintext = 'Hello, this is a message from client!'
crypt_sm2 = CryptSM2(public_key=public_key,private_key=private_key)
encrypted_data = crypt_sm2.encrypt(plaintext.encode())

client_socket.send(encrypted_data)

# 关闭连接
client_socket.close()
