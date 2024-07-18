from apis.user_operations.model import GetUserResponse, User, RegisterUserResponse
from requests import Response
from utils.constants import USER_API_BASE_URL
from utils.serialize_response import structure_response


class UserOperations:
    
    CREATE_USER_ENDPOINT = '/users'
    USER_ENDPOINT = f'{CREATE_USER_ENDPOINT}/me'
    
    def __init__(self, app) -> None:
        self.app = app
    
    
    def create_new_user_response(self, data: User) -> Response:
        http_client = self.app.client
        try:
            response = http_client.request(
                method="POST",
                url=f'{USER_API_BASE_URL}{self.CREATE_USER_ENDPOINT}',
                json = data.to_dict()
            )
            return response
        except Exception as e:
            raise e
    
    
    def create_new_user_successfully(self, data: User) -> RegisterUserResponse:
        response = self.create_new_user_response(data)
        assert response.status_code == 201
        return structure_response(response, RegisterUserResponse)


    def delete_user_response(self, token: str) -> Response:
        response = self.app.client.request(
            method="DELETE",
            url=f'{USER_API_BASE_URL}{self.USER_ENDPOINT}',
            headers={"Authorization": f"Bearer {token}"},
        )
        return response
        
        
    def delete_user_successfully(self, token: str) -> None:
        response = self.delete_user_response(token)
        assert response.status_code == 200, "Check status code"
        
        
    def get_user_response(self, token: str) -> Response:
        response = self.app.client.request(
            method="GET",
            url=f'{USER_API_BASE_URL}{self.USER_ENDPOINT}',
            headers={"Authorization": f"Bearer {token}"},
        )
        return response


    def get_user_successfully(self, token: str) -> GetUserResponse:
        response = self.get_user_response(token)
        print(response.content)
        assert response.status_code == 200, "Check status code"
        return structure_response(response, GetUserResponse)