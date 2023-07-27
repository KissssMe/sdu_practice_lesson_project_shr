#send a tx on Bitcoin testnet...
import requests
import re
#url: Bitcoin testnet链接
url='https://whatsonchain.com/block-height/801680'
#向它发送的tx信息
tx={
    'tx':'111222333'
    }
post_html=requests.post(url,data=tx)
#输出返回的响应信息
print(post_html.text)

