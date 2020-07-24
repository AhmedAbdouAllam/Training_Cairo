import firebase_admin
from firebase_admin import credentials
from html2text import html2text
from firebase_admin import firestore
from OpportunityClass import *
from Credintials import *

opp_list_electrical = []
opp_list_mechanical = []
opp_list_architecture = []
opp_list_civil = []
opp_list_cce = []
cred = credentials.Certificate(JSON_FILE)
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(r'opportunities').stream()
for doc in doc_ref:
    dic = doc.to_dict()
    desc = html2text(dic["desc"])
    opp = Opportunity(dic["link"], dic["title"],desc, dic["deadline"])
    dept = dic["department"]
    if dept == "cce":
        opp_list_cce.append(opp)
    elif dept == "eee":
        opp_list_electrical.append(opp)
    elif dept == "mech":
        opp_list_mechanical.append(opp)
    elif dept == "civil":
        opp_list_civil.append(opp)
    elif dept == "archi":
        opp_list_architecture.append(opp)
    else:
        raise Exception("Unidentified Department for Opportunites")

subscriber_list_electrical = []
subscriber_list_mechanical = []
subscriber_list_architecture = []
subscriber_list_civil = []
subscriber_list_cce = []

doc_ref = db.collection(r'subscribers').stream()
for doc in doc_ref:
    dic = doc.to_dict()

    opp = Subscriber(dic["email"], dic["name"], 0)

    dept = dic["department"]
    if dept == "cce":
        subscriber_list_cce.append(opp)
    elif dept == "eee":
        subscriber_list_electrical.append(opp)
    elif dept == "mech":
        subscriber_list_mechanical.append(opp)
    elif dept == "civil":
        subscriber_list_civil.append(opp)
    elif dept == "archi":
        subscriber_list_architecture.append(opp)
    else:
        raise Exception("Unidentified Department for Subscribers")
