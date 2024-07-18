from configparser import ConfigParser
from apis.contact_operations.api import ContactOperations
from apis.requests import Client
from apis.user_operations.api import UserOperations


class Application:
    
    def __init__(self, config: ConfigParser):
        self.client = Client()
        self.user_operations = UserOperations(self, config['base_url'])
        self.contact_operations = ContactOperations(self, config['base_url'])