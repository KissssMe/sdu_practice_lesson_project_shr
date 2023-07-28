# SDU-2023-CryproProject

2023 创新创业实践课实践项目repository

**个人信息：时浩然 202100460085**

以下所有项目均由个人完成，每一个项目都有`README`文件作为报告

**共完成 `14` 个项目，未完成 `7` 个项目**

## 项目列表

| 编号 | 项目名称 | 对应文件夹 |
|:----:|:--------|:----------|
||✅已完成 ||||
|   1  | implement the naïve birthday attack of reduced `SM3`<br> - 在16s内能找到sm3的一组碰撞 | [Project_01_SM3_BirthAttack](./Project_01_SM3_BirthAttack/)|
|   2  | implement the Rho method of reduced `SM3`<br> - 采用碰撞部分bit的方法，8bit时间为5s |[Project_02_Rho_Attack_SM3](./Project_02_Rho_Attack_SM3/) |
|   3  | implement length extension attack for `SM3`, `SHA256`, etc <br> - 选择md5进行长度扩展攻击 | [Project_03_padding_attack](./Project_03_padding_attack/) |
|   4  | do your best to optimize `SM3` implementation (software) <br> - 最终实现加速比约为1.5  |[Project_04_optimize_SM3](./Project_04_optimize_SM3/) |
|   5  | Impl Merkle Tree following <br> - 用二维数组实现树的构建，速度更快 | [Project_05_Impl_Merkle_Tree](./Project_05_Impl_Merkle_Tree/) |
|   9  | AES / SM4 software implementation <br> - 实现了AES-128，速度超过密码库 | [Project_09_AES_implementation](./Project_09_AES_implementation/) |
|  10  | report on the application of this deduce technique in Ethereum with `ECDSA` | [Project_10_ECDSA_pk_recovery](./Project_10_ECDSA_pk_recovery/) |
|  11  | impl `sm2` with <a herf="https://www.rfc-editor.org/info/rfc6980"> RFC6979 </a> | [Project_11_sm2_impl](./Project_11_sm2_impl/) |
|  14  | Implement a `PGP` scheme with `SM2`<br> - 信息加密使用SM4 <br> - 密钥加密使用SM2 | [Project_14_PGP_sm2](./Project_14_PGP_sm2/) |
|  15  | implement `sm2` 2P sign with real network communication | [Project_15_sm2_2Psign](./Project_15_sm2_2Psign/) |
|  16  | implement `sm2` 2P decrypt with real network communication | [Project_16_sm2_2pdec](./Project_16_sm2_2pdec/) |
|  17  | 比较Firefox和谷歌的记住密码插件的实现区别 <br> - 从哈希、加密方法、分组结构、密钥派生方案等方面进行了比较 | [Project_17_Compare_plug-in](./Project_17_Compare_plug-in/) |
|  18  | send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself |  [Project_18_Bitcoin_test](./Project_18_Bitcoin_test/) |
|  19  | forge a signature to pretend that you are Satoshi | [Project_19_Fake_sig](./Project_19_Fake_sig/) |
||❌未完成||||
| 6| impl this protocol with actual network communication||
|7|Try to Implement this scheme||
|8|AES impl with ARM instruction||
|12|verify the above pitfalls with proof-of-concept code||
|13|Implement the above ECMH scheme||
|  21  | Schnorr Bacth |  |
|22|research report on MPT||
