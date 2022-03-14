import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print('clear')
print(green+"""▗▜ ▞▀▖▛▀▖   ▙▗▌
▛▚▀▖▝▀▖▄▐ ▚▄ ▙▄▘▝▀▖▌▘▌
▌▐ ▌▞▀▌▐▐ ▖ ▌▌  ▞▀▌▌ ▌
▘▝ ▘▝▀▘▀▘▘▝▀ ▘  ▝▀▘▘ ▘                   Version 1.0"""+green)

def send_mail():
	login = input('Введите вашу почту:')
	password = input('Введите пароль от почты:')
	url = input('URL:')
	toaddr = input('Кому:')
	topic = input('Тема:')
	message = input('Введите сообщение:')
	num = int(input('Введите кол-во сообщений:'))

	for value in range (num):
		msg = MIMEMultipart()

		msg['Subject'] = topic
		msg['From'] = login
		body = message
		msg.attach(MIMEText(body, 'plain'))

		server = root.SMTP_SSL( url, 465 )
		server.login(login, password)
		server.sendmail(login, toaddr, msg.as_string())

		value += 1

		print('Отправлено:' + str(value))

def main():
	send_mail()

if __name__ == '__main__':
	main()
