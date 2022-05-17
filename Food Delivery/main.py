
import requests



sender = "Prajwal"

bot_message = ""
while bot_message != "bye":
    user_message = input ("Enter your message: ")
    print("Sending message now....")
    r = requests.post("http://localhost:5005/webhooks/rest/webhook", json={"sender": sender, "message": user_message})
    print(r)
    print("Bot: ", end = ' ')
    for i in r.json():
        bot_message = i["text"]
        print(bot_message)  
   