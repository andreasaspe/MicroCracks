import courier
from courier.client import Courier
from bs4 import BeautifulSoup
import requests
import time

# TJEK DENNE GITHUB SIDE FOR HVORDAN MAN SENDER MAILS: https://github.com/trycourier/courier-python.
# Log in på courier.com. Har logget på med google med denne mail: andreas.marathon.bot@gmail.com

#GLEEEM DET HER SCRIPT!!

client = Courier(
  authorization_token="pk_prod_6Y7XA3NCMY4C7MJG6YMVWA01MYY4" # Defaults to COURIER_AUTH_TOKEN
)

def send_email(title,body,to_email):
  response = client.send(
    message=courier.ContentMessage(
      to=courier.UserRecipient(
        email=to_email,
        data={
          "name": "Andreas",
        }
      ),
      content=courier.ElementalContentSugar(
        title=title,
        body=body,
      ),
      routing=courier.Routing(method="all", channels=["inbox", "email"]),
    )
  )

def check_tickets(old_text):
    url = "https://secure.onreg.com/onreg2/bibexchange/?eventid=6591"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if "Der er ikke nogen startnumre til salg i øjeblikket. Prøv igen lidt senere." in soup.text:
        return False, soup.text
    
    if old_text != soup.text:
        return True, soup.text
    else:
        return False, soup.text
    
    # # Tjek om strengen "Der er ikke nogen startnumre til salg i øjeblikket. Prøv igen lidt senere." er på siden
    # if "Der er ikke nogen startnumre til salg i øjeblikket. Prøv igen lidt senere." in soup.text:
    #     return False
    # elif site_changed == 0:
    #     site_changed = 1
    # else:
    #     return False
    
old_text = ""
counter = 0
if __name__ == "__main__":
    while True:
        try:
            buy, old_text = check_tickets(old_text)
            print(counter)
            counter += 1
            if buy == True:
                title = "KØØØØØØB fra Marathon3"
                body = "Der er marathonbilletter til salg!! Køb dem her: https://secure.onreg.com/onreg2/bibexchange/?eventid=6591"
                send_email(title, body, "andreasaspe@gmail.com")
            # if counter%10 == 0:
            #     title = "Regelmæssigt tjek for marathonbot."
            #     body = "Marathonbot virker stadig"
            #     send_email(title, body, "andreasaspe@gmail.com")
                counter = 0
            time.sleep(5)
        except:
            print("No internet connection")
            time.sleep(10)
        


# print(response)



# resp = client.send_message(
#   message={
#     "to": {
#       "email": "andreas.marathon.bot@gmail.com",
#     },
#     "template": "R01YHRKHMFMTJ8GM0V1G4N4A4ZZD",
#     "data": {
#     },
#   }
# )

# print(resp['requestId'])


# resp = client.send(
#   event="courier-quickstart",
#   recipient="andreas.marathon.bot@gmail.com",
#   data={
#     "favoriteAdjective": "awesomeness"
#   },
#   profile={
#     "email": "andreas.marathon.bot@gmail.com"
#   }
# )
# # token = 'o.yOl7lqZKIrAUIJ7gpC8VD55kzMp1dQhm'