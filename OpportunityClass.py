class Opportunity:
    def __init__(self, opportunity_link, opportunity_title, opportunity_description, opportunity_deadline):
        self.opportunity_link = opportunity_link
        self.opportunity_title = opportunity_title
        self.opportunity_description = opportunity_description
        self.opportunity_deadline = opportunity_deadline


class Subscriber:
    def __init__(self, email, name, opportunity_index):
        self.email = email
        self.name = name
        self.opportunity_index = opportunity_index
