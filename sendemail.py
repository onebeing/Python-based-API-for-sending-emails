#!/usr/bin/python3
from sendgrid.helpers.mail import *
from sendgrid import *
import urllib

def create_content():
  #you can creatively come up with dynamic content
  person = "Chad"
  line = "<table><tr><th>Col 1</th><th>Col 2</th></tr><tr><td>{0}</td><td>Row 1 Col 2</td></td></table>".format(person)
  return line
  
def personalize(html):
  emails = ["",""]
  personalization = Personalization()
  #make sure your template has a Substitution tag somewhere in it like "-Table-"
  personalization.add_substitution(Substitution("-Table-",html))
  for email in emails:
    personalization.add_to(Email(email))
  return personalization

def main():
  #generate HTML
  html = create_content()
  if html is not False:
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
    mail = Mail()
    mail.from_email = Email("you@example.com","Not Chad")
    mail.template_id = "d-b8ae5c2444674060a70fbe486381357c"
    mail.add_personalization(personalize(html))

    try:
      response = sg.client.mail.send.post(request_body=mail.get())
      print(response.status)
    except urllib.error.HTTPError as e:
      print(e.read())
