from abc import ABC, abstractmethod

# Notification interface

class NotificationService(ABC):

    @abstractmethod
    def send_notification(self, message):
        pass


# Email notification

class EmailNotification(NotificationService):

    def send_notification(self, message):

        print(f"[EMAIL] {message}")


# SMS notification

class SMSNotification(NotificationService):

    def send_notification(self, message):

        print(f"[SMS] {message}")


# Push notification

class PushNotification(NotificationService):

    def send_notification(self, message):

        print(f"[PUSH] {message}")