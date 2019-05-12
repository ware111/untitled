import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

send_user = "835292859@qq.com"       # 发件人的邮箱账号
send_pwd = "wyeizawuonetbfaf"        # 发件人邮箱的密码
rec_user = "835292859@qq.com"    #收件人邮箱

def mail():
    ret = True
    try:
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        msg = MIMEText("这是测试邮箱发送内容！", "plain", "utf-8")
        msg["From"] = formataddr(["FromSMTPQQ", send_user])  # 括号中对应发件人邮箱昵称、发件人邮箱账号
        msg["To"] = formataddr(["RecSMTP"], rec_user)  # 括号中对应收件人邮箱昵称、收件人邮箱账号
        msg["Subject"] = "这是邮件的主题"  # 邮件的主题或标题

        server = smtplib.SMTP("smtp.126.com")   # 括号中对应的是发件人邮箱中的SMTP服务器，端口
        server.login(send_user, send_pwd)  # 括号中对应的是发件人邮箱账号和密码
        server.sendmail(send_user, [rec_user, msg.as_string()]) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret

ret = mail()
if ret:
    print("邮件发送成功！")
else:
    print("邮件发送失败！")
