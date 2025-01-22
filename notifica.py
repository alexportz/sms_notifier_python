#Importação do cliente Twilio
from twilio.rest import Client

accID = ''
tokenID = ''

cliente = Client(accID, tokenID)

mensagem = cliente.messages.create()

print(mensagem.body)