#Importação do cliente Twilio
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

nome="São João Batista"
myMessage = f'Olá {nome}, Lembramos que o senhor está inadinplente em nosso sitema. https://google.com'

accID = os.getenv("ACC_SID")
tokenID = os.getenv("TOKEN_ID")
senderPhone = os.getenv("PHONE_SENDER")
receiverPhone = os.getenv("PHONE_RECEIVER")

print(accID)
print(tokenID)
print(senderPhone)
print(receiverPhone)

client = Client(accID, tokenID)
message = client.messages.create(
  from_= senderPhone,
  body= myMessage,
  to= receiverPhone
)

# print(message.sid)
print(message.body)