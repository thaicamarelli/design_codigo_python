from abc import ABC, abstractmethod

# classe de interface 
# define a regra de construção das demais classes que ela e implementada
# Quando crio uma classe herdando de ABC e coloco dentro de abstractmetho 
# Eu nao posso criar objetos que instanciam a classe
class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self,message: str) -> None:
        pass

# quando coloco a classe de cima como herança eu obrigo ela a ter os mesmos metodos da de cima
class EmailNotificationSender(NotificationSender):
    def send_notification(self,message: str) -> None:
        print(message)

class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender
    
    def send(self,message: str) -> None:
        self.__notification_sender.send_notification(message)

obj = Notificator(EmailNotificationSender())
obj.send('Olá mundo')