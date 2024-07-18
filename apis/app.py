from apis.contact_operations.api import ContactOperations
from apis.requests import Client
from apis.user_operations.api import UserOperations


class Application:
    
    def __init__(self):
        self.client = Client()
        self.user_operations = UserOperations(self)
        self.contact_operations = ContactOperations(self)