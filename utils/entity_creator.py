from apis.contact_operations.model import ContactDetails
from apis.user_operations.model import User
from utils.random_utils import generate_random_alphanumeric, get_random_first_name, get_random_last_name, get_random_email, get_password

def create_new_user_data() -> User:
    return User(firstName = get_random_first_name(),
                    lastName = get_random_last_name(),
                    email = get_random_email(), 
                    password = get_password())
    
def create_new_contact_data() -> ContactDetails:
    return ContactDetails(firstName = get_random_first_name(),
                    lastName = get_random_last_name(),
                    email = get_random_email(), 
                    birthDate= '31-07-1992',
                    phone = '+919866030000',
                    street1 = generate_random_alphanumeric(),
                    street2 = generate_random_alphanumeric(),
                    city = generate_random_alphanumeric(), 
                    stateProvince = generate_random_alphanumeric(), 
                    postalCode = '867908',
                    country = generate_random_alphanumeric())