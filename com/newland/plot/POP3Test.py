#!

from poplib import POP3
from smtplib import SMTP as smtp
from email.mime.text import MIMEText
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
#
# msg = MIMEText('hello, I am Python...', 'plain', 'utf-8')
# s = smtp('smtp.126.com')
# s.set_debuglevel(1)
# s.login("ware1111@126.com",'20120218')
# s.sendmail('ware1111@126.com','ware1111@126.com',msg.as_string())

p = POP3('pop.126.com')
p.user('ware1111@126.com')
p.pass_('20120218')
msgs = p.stat()
msg = p.retr(msgs[0])
msg_content=b'\r\n'.join(msg).decode('utf-8')
# print(rev)
p.quit()



