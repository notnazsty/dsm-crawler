from plyer import notification




def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="src/dsmvector.ico",
        timeout=10,
    )

