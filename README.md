# falcon-mail
open-falcon邮件SSL接口  
官方插件不支持SSL  
FLASK 简单实现以下  
url: http://127.0.0.1:4000/mail  

pip install flask

----
以下是falcon 文档说明  

邮件发送http接口：

method: post
params:
  - content: 邮件内容
  - subject: 邮件标题
  - tos: 使用逗号分隔的多个邮件地址
falcon将这样调用该接口：

url=您公司提供的http邮件接口
curl -X POST $url -d "content=xxx&tos=ulric.qin@gmail.com,user@example.com&subject=xxx"
