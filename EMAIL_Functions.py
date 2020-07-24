import smtplib
from pathlib import Path
from email.message import EmailMessage
from string import Template
from Constants import *
from OpportunityClass import *
from Credintials import *

def send_email_department(department_subscribers, department_name, department_opportunities,joke,link):
    for subscriber in department_subscribers:
        email = EmailMessage()
        email['from'] = SENDER_NAME
        email['to'] = subscriber.email
        email['subject'] = SUBJECT
        html_string = Template(Path(HTML_PATH).read_text())
        var_name = subscriber.name
        var_department = department_name

        var_internships = ""

        if department_opportunities:
            var_internships += "<ol>"
            for opportunity in department_opportunities: # here it will not be the whole opportunites but only by
                # index Ahmed
                # A.Allam
                var_opportunity_link = opportunity.opportunity_link
                var_opportunity_title = opportunity.opportunity_title
                var_opportunity_description = opportunity.opportunity_description
                var_opportunity_deadline = opportunity.opportunity_deadline
                var_internships += "<li>" \
                                   "<a href=\"" + var_opportunity_link + "\">" + var_opportunity_title + "</a><br>" \
                                                                                                         "<ul class=\"description\">" \
                                                                                                         "<li>" + var_opportunity_description + "</li>" \
                                                                                                                                                "<li>" + var_opportunity_deadline + "</li>" \
                                                                                                                                                                                    "</ul>" \
                                                                                                                                                                                    "</li><br>"

                var_internships += "</ol>"
        else:
            var_internships="<p>Unfortunately there is no Opportunities</p>"

        email.set_content(html_string.substitute(
            {"html_name": var_name, "html_department": var_department, "html_internships": var_internships,"Link":link}), 'html')
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(email)

def send_custom_email(department_subscribers, message):
    for subscriber in department_subscribers:
        email = EmailMessage()
        email['from'] = SENDER_NAME
        email['to'] = subscriber.email
        email['subject'] = SUBJECT


        email.set_content(message)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(email)

# testing Area
if __name__ == "__main__":
    subscriber1 = Subscriber("AhmedAbdouAllam@gmail.com", "Ahmed Allam", 12)
    subscriber2 = Subscriber("AhmedAbdouAllam@gmail.com", "Ahmed Ibrahim", 12)
    opportunity1 = Opportunity("google.com", "google", "No description", "20/10/2020")
    opportunity2 = Opportunity("google.com", "google", "No description", "20/10/2020")
    opportunites = [opportunity1, opportunity2]
    send_email_department([subscriber1,subscriber2], "CCEE", opportunites)
