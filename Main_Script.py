# Packages
from WhatsApp_Functions import *
from EMAIL_Functions import *
from DataBase_Handler import *
from Credintials import *
import pyjokes
from datetime import datetime

# 1)connect with the data base
# 2)get the following lists of subscriber and opportunity objects

# verification = '0'
# # adding a joke at the end of the message.
# while verification == '0':
joke = pyjokes.get_joke()
print(joke)
    # verification = input("are you ok with this joke?")

def print_subscribers_number():
    count = len(subscriber_list_architecture) + len(subscriber_list_cce) + \
            len(subscriber_list_civil) + len(subscriber_list_mechanical) + len(subscriber_list_electrical)
    print("Your total subscribers are : "  + str(count))


def print_expired_opportunities():
    for opp in opp_list_architecture:
        date_time_obj = datetime.strptime(opp.opportunity_deadline, '%Y-%m-%d')
        if date_time_obj < datetime.today():
            print(opp.opportunity_title)
    for opp in opp_list_cce:
        date_time_obj = datetime.strptime(opp.opportunity_deadline, '%Y-%m-%d')
        if date_time_obj < datetime.today():
            print(opp.opportunity_title)
    for opp in opp_list_civil:
        date_time_obj = datetime.strptime(opp.opportunity_deadline, '%Y-%m-%d')
        if date_time_obj < datetime.today():
            print(opp.opportunity_title)
    for opp in opp_list_mechanical:
        date_time_obj = datetime.strptime(opp.opportunity_deadline, '%Y-%m-%d')
        if date_time_obj < datetime.today():
            print(opp.opportunity_title)
    for opp in opp_list_electrical:
        date_time_obj = datetime.strptime(opp.opportunity_deadline, '%Y-%m-%d')
        if date_time_obj < datetime.today():
            print(opp.opportunity_title)

def send_emails():
    send_email_department(subscriber_list_architecture, "AET", opp_list_architecture, joke,AET_LINK)
    send_email_department(subscriber_list_cce, "CCE & HEM", opp_list_cce, joke,CCE_LINK)
    send_email_department(subscriber_list_civil, "Civil", opp_list_civil, joke,CEM_LINK)
    send_email_department(subscriber_list_mechanical, "Mechanical", opp_list_mechanical, joke,MED_LINK)
    send_email_department(subscriber_list_electrical, "Electrical", opp_list_electrical, joke,EEE_LINK)


def send_whatsapp_msgs():
    (driver, wait) = initiate_selenium()
    send_msg_department_group(wait, "AET", opp_list_architecture, joke)
    send_msg_department_group(wait, "CCE & HEM", opp_list_cce, joke)
    send_msg_department_group(wait, "Civil", opp_list_civil, joke)
    send_msg_department_group(wait, "Mechanical", opp_list_mechanical, joke)
    send_msg_department_group(wait, "Electrical", opp_list_electrical, joke)
    driver.close()

def send_custom_whatsapp_main(message):
    (driver, wait) = initiate_selenium()
    send_custom_whatsapp(wait,"AET", message)
    send_custom_whatsapp(wait,"CCE & HEM", message)
    send_custom_whatsapp(wait,"Civil", message)
    send_custom_whatsapp(wait,"Mechanical", message)
    send_custom_whatsapp(wait,"Electrical", message)

def send_custom_email_main(message):
    send_custom_email(subscriber_list_architecture,message)
    send_custom_email(subscriber_list_cce, message)
    send_custom_email(subscriber_list_civil, message)
    send_custom_email(subscriber_list_mechanical, message)
    send_custom_email(subscriber_list_electrical, message)

def send_daily():
    send_emails()
    send_whatsapp_msgs()

def send_custom(message):
    send_custom_whatsapp_main(message)
    send_custom_email_main(message)

if __name__ == "__main__":

    val = input("Do you want to send custom or daily messages ? \n1-Custom \n2-Daily\n3-else\n")
    if(val == "1"):
        message = input("Enter you custom message : \n")
        send_custom(message)
    elif val == "2":
        send_daily()
    else:
        val = input("1-print all subscribers number\n2-print all expired opportunities\n")
        if val == "1":
            print_subscribers_number()
        else:
            print_expired_opportunities()
