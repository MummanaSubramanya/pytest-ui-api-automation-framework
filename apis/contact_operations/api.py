from requests import Response
from apis.contact_operations.model import AddContactResponse, ContactDetails
from utils.serialize_response import structure_response


class ContactOperations:
    
    CONTACTS_ENDPOINT = '/contacts'
    
    def __init__(self, app, url) -> None:
        self.app = app
        self.url = url
        
    def create_new_contact_response(self, token: str, data: ContactDetails) -> Response:
        response = self.app.client.request(
            method="POST",
            url=f'{self.url}{self.CONTACTS_ENDPOINT}',
            json=data.to_dict(),
            headers={"Authorization": f"Bearer {token}"},
        )
        return response

    def create_new_contact_successfully(self, token: str, data: ContactDetails) -> AddContactResponse:
        response = self.create_new_contact_response(token, data)
        print(response.content)
        print(response.status_code)
        assert response.status_code == 201
        return structure_response(response, AddContactResponse)
    
    