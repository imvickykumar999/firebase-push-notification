import firebase_admin
from firebase_admin import credentials, messaging

def initialize_firebase():
    # Path to your service account key file
    cred = credentials.Certificate('fir-push-notification-85613-61ecdbc86a05.json')
    firebase_admin.initialize_app(cred)

def send_push_notification(token, title, body):
    # Define the message payload
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )

    # Send the message
    response = messaging.send(message)
    return response

if __name__ == "__main__":
    initialize_firebase()
    fcm_token = 'dF8A2vqxUKQPjV27rLXtiO:APA91bG58DRwh6leVAXV7HBITVU9Y4TD1SzMO3H2o9qI4QOp9BdiQvbNhQN9DMpMgDU9XUjZYUjBuwd866BEyYp-_DCLqS91_NLZQr1Kh9n-eOi91q4ZLdoHlDZG5onwV5_kNpdvA9k1'
    title = 'Hello'
    body = 'World'
    response = send_push_notification(fcm_token, title, body)
    print('Successfully sent message:', response)

