# 比较Firefox和谷歌的记住密码插件的实现区别

## 谷歌插件——Keepass
对于谷歌的有名的记住密码插件，大多数收费不开源，退而求其次，我选取了一个跨平台插件`keepass`。

## Keepass简介
KeePass 的数据库是创建在本地的，也就是说你的一切密码都存在你的电脑上。创建数据库最主要的一步就是创建「主密码」或者叫做「管理密码」。

值得一提的是，KeePass 还提供了密钥文件（Key file）作为密码，密钥文件可以是一个文本、一个音频、一个视频甚至一个 exe 文件。而且你可以使用叠加的方式来使用，这样你打开你的数据库就需要主密码+密钥文。

创建完数据库你就可以根据个人的需求添加密码或者直接导入密码（导出支持CSV文件，也支持将 1Password、LastPass 等主流密码管理器）

## Keepass实现细节

Keepass开源代码在GitHub中可以找到，仓库地址为 https://github.com/keepassxreboot/keepassxc/tree/develop

阅读源代码可知以下信息：

* **采用的哈希方法**：`SHA256或SHA512`
```
class CryptoHash
{
public:
    enum Algorithm
    {
        Sha256,
        Sha512
    };
```

* **采用的加密方法**：`AES256-CBC`
```
    bool testAes256Cbc()
    {
        QByteArray key = QByteArray::fromHex("603deb1015ca71be2b73aef0857d7781"
        "1f352c073b6108d72d9810a30914dff4");

        ………………

        if (data != plainText) {
            g_cryptoError = "AES-256 CBC decryption mismatch.";
            return false;
        }

        return true;
    }
```

* **密钥派生函数**：`AES-KDF`
```
    bool testAesKdf()
    {
        QByteArray key = QByteArray::fromHex("000102030405060708090A0B0C0D0E0F"
                                             "101112131415161718191A1B1C1D1E1F");
        …………

        if (plainText != cipherText) {
            g_cryptoError = "AES KDF encryption mismatch.";
            return false;
        }

        return true;
    }

```

* **随机数生成**：
KeePass首先使用各种熵源创建一个熵池 （包括系统加密提供程序生成的随机数， 当前日期/时间和正常运行时间、光标位置、操作系统版本、 处理器计数、环境变量、进程和内存统计信息， 当前区域性、新的随机 GUID 等）。
生成高级生成方法的随机位 使用加密安全的伪随机数生成器 （基于 SHA-256/SHA-512 和 ChaCha20）使用熵池初始化。

随机数生成中源码包含randomize、randomArray、randomUInt等函数，在此不再展示。

* **进程内存保护**：
KeePass使用Windows DPAPI加密内存中的敏感数据（通过CryptProtectMemory / ProtectedMemory）。 使用 DPAPI 时，内存加密的密钥存储在 由 Windows 管理的安全、不可交换的内存区域。KeePass 2.x 总是在 DPAPI 可用时使用; 在KeePass 1.x中，可以禁用此功能（在高级选项中;默认情况下 启用 DPAPI;如果禁用，KeePass 1.x 将使用 ARC4 加密 带有随机密钥的算法


## Firefox插件——bitwarden

firefox中最火爆的密码管理插件其实是lastpass，但因为其不开源，我们在这里选择了bitwarden进行比较分析，其源代码地址为 https://github.com/bitwarden/clients/tree/master

## Bitwarden实现细节

* **主密钥（Master Key）**：
最核心的密钥，所有后续的密钥和加密密钥均通过主密钥派生，主密钥也是解密所有登录信息以及私人数据的唯一密钥，丢失会导致无法获取已经保存的数据，泄漏将导致所有的数据公之于众。所以主密钥复杂点毕竟你所有的密钥都不需要记了，主密钥在特别简单岂不是很危险？
```
masterKeyHash = pbkdf2(masterKey, email)
```

* **加密方式**：
Bitwarden 使用 AES-CBC 256 位加密，并使用 PBKDF2 SHA-256 或 Argon2 派生加密密钥。

* **KDF**：
PBKDF2 或者 Argon2

由Bitwarden实现的PBKDF2的工作原理是使用您的用户名加盐您的主密码，并通过单向哈希算法（HMAC-SHA-256）运行结果值以创建固定长度的哈希。此值再次使用您的用户名进行加盐处理，并按可配置的次数（KDF 迭代）进行哈希处理。

## 总结
**从两个插件的实现细节来看基本相似**：
* 加密方法都为AES-CBC 256
* 哈希方法都采用SHA-256
* 实现逻辑都为用户保存主密钥，通过主密钥及KDF派生出多个轮密钥
* KDF方法有所不同，Keepass采用AES-KDF；Bitwarden采用PBKDF2 或者 Argon2

**初步推测这种高度的相似性有以下原因**：

两者都是开源的插件，对于最主流的非开源插件，我们并没有办法拿到源码进行分析；这种开源的插件商业化不是那么强，对于某些付费可靠密码库的使用也比较有限，AES-256和SHA-256是最效率、最经济的安全选择。