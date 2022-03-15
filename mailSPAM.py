import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

lgreen = '\033[92m'
clear = '\033[0m'

print(clear+lgreen+"""       ▗▜ ▞▀▖▛▀▖   ▙▗▌
▛▚▀▖▝▀▖▄▐ ▚▄ ▙▄▘▝▀▖▌▘▌
▌▐ ▌▞▀▌▐▐ ▖ ▌▌  ▞▀▌▌ ▌
▘▝ ▘▝▀▘▀▘▘▝▀ ▘  ▝▀▘▘ ▘                   Version 1.0"""+lgreen+clear)

print("1) Запустить spammail.")
print("2) Обновить spamMail.")
print("3) Выход.")
input1 = input(Fore.BLUE+"Введите номер пункта: "+Style.RESET_ALL)
    elif input1 == "1":
        send_mail()
    elif input1 == "2":
	update()
					
    elif input1 == "3":
	print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
		exit()
def update():
	a=input("Вы уверены, что хотите обновить? (y/n) ")

	if a=="y":
	os.system("cd && rm -rf spamMail && git clone https://github.com/Roundstg04/spamMail && cd spamMail && sh install.sh")
	exit()
	else:
	print("Отменено")

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
