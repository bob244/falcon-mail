from flask import Flask, request, abort
import smtplib
from email.mime.text import MIMEText
from email.header import Header


smtp_username = 'XXXXX'
smtp_password = 'XXXXX'


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/mail', methods=['POST'])
def send_mail():
    if not request.values or not 'content' in request.values:
         abort(400)
    content = request.values.get('content')
    subject = request.values.get('subject')
    tos = request.values.get('tos')
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(smtp_username, 'utf-8')
    message['To'] = Header("服务器管理员", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        smtpObj.login(smtp_username, smtp_password)
        smtpObj.sendmail(smtp_username, tos.split(','), message.as_string())
        return "ok", 200
    except smtplib.SMTPException as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(port=4000)
