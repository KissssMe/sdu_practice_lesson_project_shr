# sdu_practice_lesson_project_shr

2023 创新创业实践课实践项目repository

**个人信息：时浩然 202100460085**

以下所有项目均由个人完成

## 项目列表

<table>
<thead>
  <tr>
    <th align="center" width=10%> 编号</th>
    <th width=55%>项目名称</th>
    <th width=25%>对应文件夹</th>
  </tr>
</thead>
<tbody>
   <tr>
    <td align="center" colspan="4"> 
        ✅已完成
    </td> 
   </tr>
  <tr>
    <td rowspan="2" align="center"> 1</td>
    <td rowspan="2" >implement the naïve birthday attack of reduced <code>SM3</code>
    <li>  在16s内能找到sm3的一组碰撞
    </td>
    <td><a href="./Project_01_SM3_BirthAttack/">Project_01_SM3_BirthAttack</a>
    </td>

  </tr>
<tr>
  </tr>
  <tr>
    <td rowspan="2" align="center"> 2</td>
    <td rowspan="2" >implement the Rho method of reduced <code>SM3</code>
    <li>  采用碰撞部分bit的方法，8bit时间为5s
    </td>
    <td><a href="./Project_02_Rho_Attack_SM3/">Project_02_Rho_Attack_SM3</a></td>

  </tr>
  <tr>

  </tr>
  <tr>
    <td align="center">3</td>
    <td>implement length extension attack for <code>SM3</code>, <code>SHA256</code>, etc
    <li>  选择md5进行长度扩展攻击
    </td>
    <td><a href="./Project_03_padding_attack/">Project_03_padding_attack</a></td>
    
  </tr>
  <tr>
    <td rowspan="2" align="center">4</td>
    <td rowspan="2" >do your best to optimize <code>SM3</code> implementation (software)
    <li> 最终实现加速比约为1.5
    </td>
    <td><a href="./Project_04_optimize_SM3/">Project_04_optimize_SM3</a></td>
    
  </tr>

  <tr>
  </tr>
  <tr>
    <td rowspan="3" align="center">5</td>
    <td rowspan="3" >Impl Merkle Tree following 
    <a herf="https://www.rfc-editor.org/info/rfc6962"> RFC6962 </a>
         <li> 用二维数组实现树的构建，速度更快
    </td>
    <td><a href="./Project_05_Impl_Merkle_Tree/">Project_05_Impl_Merkle_Tree</a></td>
  </tr>
  <tr>

  </tr>
  <tr>

  </tr>
  <tr>
    <td align="center">9</td>
    <td>AES / SM4 software implementation
    <li> 实现了AES-128，速度超过密码库
    </td>
    <td > <a href="./Project_09_AES_implementation/">Project_09_AES_implementation</a></td>
  </tr>
  <tr>
    <td align="center">10</td>
    <td>report on the application of this deduce technique in Ethereum with <code>ECDSA</code></td>
    <td><a href="./Project_10_ECDSA_pk_recovery/" >Project_10_ECDSA_pk_recovery</a></td>
  </tr>

  <tr>
    <td rowspan="2" align="center">11</td>
    <td rowspan="2">impl <code>sm2</code> with <a herf="https://www.rfc-editor.org/info/rfc6980"> RFC6979 </a>
    </td>
    <td><a href="./Project_11_sm2_impl/" target="_blank" rel="noopener noreferrer">Project_11_sm2_implementation</a></td>
  </tr>
  
  <tr>
  </tr>

  <tr>
    <td rowspan="2" align="center">14</td>
    <td rowspan="2" >Implement a <code>PGP</code> scheme with <code>SM2</code>
         <li> 信息加密使用SM4
         <li> 密钥加密使用SM2
    </td>
    <td><a href="./Project_14_PGP_sm2/">Project_14_PGP_sm2</a></td>
    
  </tr>
  <tr>
  </tr>
  <tr>
    <td align="center">15</td>
    <td>implement <code>sm2</code> 2P sign with real network communication</td>
    <td><a href="./Project_15_sm2_2Psign/">Project_15_sm2_2Psign</a></td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td>implement <code>sm2</code> 2P decrypt with real network communication</td>
    <td><a href="./Project_16_sm2_2pdec/" >Project_16_sm2_2pdec</a></td>
  </tr>
  <tr>
    <td align="center">17</td>
    <td>比较Firefox和谷歌的记住密码插件的实现区别
    <li> 从哈希、加密方法、分组结构、密钥派生方案等方面进行了比较
    </td>
    <td > <a href="./Project_17_Compare_plug-in/">Project_17_Compare_plug-in</a></td>
  </tr>
  <tr>
    <td align="center">18</td>
    <td>send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself</td>
    <td><a href="./Project_18_Bitcoin_test/">Project_18_Bitcoin_test</a></td>
  </tr>
  <tr>
    <td align="center">19</td>
    <td>forge a signature to pretend that you are Satoshi</td>
    <td> <a href="./Project_19_Fake_sig/">Project_19_Fake_sig</a></td>
  </tr>
  <tr>
    <td align="center">17</td>
    <td>research report on MPT</td>
    <td> <a href="./merkle-tree/MPT%20report.md"> MPT report</a></td>
    <td align="center">🦀️</td>
  </tr>
  <tr>
    <td align="center">18</td>
    <td>Find a key with hash value “sdu_cst_20220610” under a message composed of your name followed by your student ID. For example, “San Zhan 202000460001”.</td>
    <td> <a href="./cryptanalysis"> cryptanalysis </a> </td>
    <td align="center">🐙</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td>Try to build zkp app to proof CET6 Score &gt; 425</td>
    <td><a href="./poc-of-zkp">poc-of-zkp</a></td>
    <td align="center">🎣</td>
  </tr>
  <tr>
    <td align="center">额外</td>
    <td>  Do your best to optimize <code>SM4</code> implementation (software)</td>
    <td><a href="./sm4">sm4</a></td>
    <td align="center">🐙</td>
  </tr>
  <tr>
    <td align="center" colspan="4"> 
        ❌未完成
    </td> 
   </tr>
  <tr>
    <td align="center">19</td>
    <td>Find a 64-byte message under some k fulfilling that their hash value is symmetrical.</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>
