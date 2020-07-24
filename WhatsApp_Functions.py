from Constants import *
from OpportunityClass import Opportunity
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def initiate_selenium():
    chrome_options = Options()
    chrome_options.add_argument(CHROME_OPTIONS)  # change to profile path
    chrome_options.add_argument(CHROME_PROFILE)
    d = webdriver.Chrome(ChromeDriverManager().install(),
                         chrome_options=chrome_options)  # change the executable_path too
    d.get(WEBSITE)  # URL to open whatsapp web
    wait = WebDriverWait(driver=d, timeout=900)  # inscrease or decrease the timeout according to your net connection
    return d,wait

#
# def form_message(department, opportunities,joke):
#     message = "*-----------------------------------------------------*\r"+"*-----------------------------------------------------*\r"+"*here is the new updated opportunity list for : " + department + " departments* \r"
#     if opportunities:
#         for i in range(len(opportunities)):
#             message += (str(i+1) + ".")
#             message += ("*Opportunity Title*: " + opportunities[i].opportunity_title + "\r")
#             message += ("*Opportunity Link*: " + opportunities[i].opportunity_link + "\r")
#             message += ("*Opportunity Description*: " + opportunities[i].opportunity_description + "\r")
#             message += ("*Opportunity Deadline*: " + opportunities[i].opportunity_deadline + "\r")
#     else:
#         message += "_There is no opportunities yet_ \r"
#     message += "*these are automated messages* \r *-----------------------------------------------------*\r *-----------------------------------------------------*\r"
#     return message


def send_msg_department_group(wait, department, opportunities,joke):
    # message = form_message(department, opportunities,joke)
    add_new_chat = NEWCHAT
    title = wait.until(EC.presence_of_element_located((By.XPATH, add_new_chat)))
    title = wait.until(EC.element_to_be_clickable((By.XPATH, add_new_chat)))
    title.click()  # to open the receiver messages page in the browser

    search_section = SEARCHSECTION
    title = wait.until(EC.presence_of_element_located((By.XPATH, search_section)))
    title.click()
    title.send_keys("CUFE CHS IT - "+department)  # send your message followed by an Enter
    # after searching this the entry command
    time.sleep(1)
    name_argument = NAMEARGUMENT # HTML parse code to identify your reciever

    title = wait.until(EC.presence_of_element_located((By.XPATH, name_argument)))

    title = wait.until(EC.element_to_be_clickable((By.XPATH, name_argument)))

    title.click()  # to open the receiver messages page in the browser
    # the sending part is commented for now
    input_path = INPUTPATH
    box = wait.until(EC.presence_of_element_located((By.XPATH, input_path)))

    box.send_keys("*Update opportunity list*")
    box.send_keys(Keys.SHIFT, Keys.ENTER)
    if opportunities:
        for i in range(len(opportunities)):
            box.send_keys(Keys.SHIFT , Keys.ENTER)
            box.send_keys(str(i + 1) + "."+"*Opportunity Title*: " + opportunities[i].opportunity_title)
            box.send_keys(Keys.SHIFT , Keys.ENTER)
            box.send_keys("*Opportunity Link*: " + opportunities[i].opportunity_link)
            box.send_keys(Keys.SHIFT, Keys.ENTER)
            box.send_keys("*Opportunity Description*: " + opportunities[i].opportunity_description.replace('\n','.'))
            box.send_keys(Keys.SHIFT, Keys.ENTER)
            box.send_keys("*Opportunity Deadline*: " + opportunities[i].opportunity_deadline)
            box.send_keys(Keys.SHIFT, Keys.ENTER)
            box.send_keys(Keys.SHIFT, Keys.ENTER)
    else:
        box.send_keys("_There is no opportunities yet_")
        box.send_keys(Keys.SHIFT, Keys.ENTER)
        box.send_keys("bala4 bakasa yaret ay 7ad y-post opportunities")
        box.send_keys(Keys.SHIFT, Keys.ENTER)
    box.send_keys("*these are automated messages*")
    box.send_keys(Keys.ENTER)  # send your message followed by an Enter


def send_custom_whatsapp(wait, department,message):
    # message = form_message(department, opportunities,joke)
    add_new_chat = NEWCHAT
    title = wait.until(EC.presence_of_element_located((By.XPATH, add_new_chat)))
    title = wait.until(EC.element_to_be_clickable((By.XPATH, add_new_chat)))
    title.click()  # to open the receiver messages page in the browser

    search_section = SEARCHSECTION
    title = wait.until(EC.presence_of_element_located((By.XPATH, search_section)))
    title.click()
    title.send_keys("CUFE CHS IT - "+department)  # send your message followed by an Enter
    # after searching this the entry command
    time.sleep(1)
    name_argument = NAMEARGUMENT # HTML parse code to identify your reciever

    title = wait.until(EC.presence_of_element_located((By.XPATH, name_argument)))

    title = wait.until(EC.element_to_be_clickable((By.XPATH, name_argument)))

    title.click()  # to open the receiver messages page in the browser
    # the sending part is commented for now
    input_path = INPUTPATH
    box = wait.until(EC.presence_of_element_located((By.XPATH, input_path)))

    box.send_keys("*This is a custom notification*")
    box.send_keys(Keys.SHIFT, Keys.ENTER)
    box.send_keys(Keys.SHIFT, Keys.ENTER)
    box.send_keys(message)
    box.send_keys(Keys.ENTER)  # send your message followed by an Enter

# if __name__ == '__main__':
#     (driver,wait)=initiate_selenium()
#     opportunity1 = Opportunity("google.com", "google", "No description", "20/10/2020")
#     opportunity2 = Opportunity("google.com", "google", "No description", "20/10/2020")
#     opportunites = [opportunity1, opportunity2]
#     send_msg_department_group(wait,"Kamel Mohsen",opportunites)
#     driver.close()
