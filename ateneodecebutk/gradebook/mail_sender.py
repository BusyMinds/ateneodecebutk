import requests

def send_message(filepath):
    return requests.post(
        "https://api.mailgun.net/v2/sandbox53636.mailgun.org/messages",
        auth=("api", "key-4egq8drvnv3reclfr66o27p8ehpgdqi7"),
        data={"from": "Gradebook Web App <noel@sandbox53636.mailgun.org>",
              "to": ["noelmartin@gmail.com"],
              "subject": "Test from MailGun",
              "text": "Testing some Mailgun awesomeness!" + str(filepath)})
