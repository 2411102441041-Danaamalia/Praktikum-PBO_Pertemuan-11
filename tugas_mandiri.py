from abc import ABC, abstractmethod

class INotificationChannel(ABC):
    @abstractmethod
    def send(self, user, message):
        pass

# Implementasi konkrit
class EmailChannel(INotificationChannel):
    def send(self, user, message):
        print(f"Email ke {user}: {message}")

class SmsChannel(INotificationChannel):
    def send(self, user, message):
        print(f"SMS ke {user}: {message}")

class PushChannel(INotificationChannel):
    def send(self, user, message):
        print(f"Push ke {user}: {message}")

class WhatsappChannel(INotificationChannel):
    def send(self, user, message):
        print(f"Whatsapp ke {user}: {message}")

# Koordinator SRP
class NotificationService:
    def __init__(self, channels):
        self.channels = channels

    def notify(self, user, message):
        for channel in self.channels:
            channel.send(user, message)

# Contoh penggunaan
channels = [EmailChannel(), SmsChannel(), WhatsappChannel()]
service = NotificationService(channels)
service.notify("Amel", "Selamat! Anda mendapat notifikasi baru.")
