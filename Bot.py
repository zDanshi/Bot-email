import smtplib
from email.message import EmailMessage


print("""
 _____           ___  ___      _ _   ______       _   
|  ___|          |  \/  |     (_) |  | ___ \     | |  
| |__    ______  | .  . | __ _ _| |  | |_/ / ___ | |_ 
|  __|  |______| | |\/| |/ _` | | |  | ___ \/ _ \| __|
| |___           | |  | | (_| | | |  | |_/ / (_) | |_ 
\____/           \_|  |_/\__,_|_|_|  \____/ \___/ \__|
""")
email = EmailMessage()
email['from'] = "Seu nome"            
email['to'] = "destinatario@gmail.com"     
email['subject'] = "Assunto do email" 


emailcount = 0
	
def send_email():
    print("Espere um momento :)\n")
    with   smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("seuemail@gmail.com", "suasenha") 
        smtp.send_message(email)

while (emailcount <= 1): #definir quantos emails quer enviar
    if __name__ == '__main__':
      try:
        print("Enviando E-Mail...\n")
        send_email()
        print('\n\t Email Enviado :) \n')

        emailcount += 1

      except KeyboardInterrupt:
        print('\n\t Operação cancelada pelo usuário :( \n')
    
      except Exception as e:
        print(f'\n\t Aconteceu algo de errado :( \n\n\t {e} \n')


	