import os

#URL = "https://api.mailgun.net/v3/sandbox8156d331603d4b118aa3343cb7b0e063.mailgun.org/messages"
#API_KEY = "b522602d1a17f227d0d12cd21adc6510-b6183ad4-56c26762"
#FROM = "Mailgun Sandbox <postmaster@sandbox8156d331603d4b118aa3343cb7b0e063.mailgun.org>"
ALERT_TIMEOUT = 10
COLLECTION = "alerts"

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"

