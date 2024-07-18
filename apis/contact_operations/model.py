import attr

@attr.s
class ContactDetails:
    firstName: str = attr.ib(default=None)
    lastName: str = attr.ib(default=None)
    birthDate: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    phone: str = attr.ib(default=None)
    street1: str = attr.ib(default=None)
    street2: str = attr.ib(default=None)
    city: str = attr.ib(default=None)
    stateProvince: str = attr.ib(default=None)
    postalCode: str = attr.ib(default=None)
    country: str = attr.ib(default=None)
    
    def to_dict(self):
        return attr.asdict(self)
    
    
@attr.s
class AddContactResponse:
    _id: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    firstName: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    lastName: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    email: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    phone: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    street1: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    street2: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    city: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    stateProvince: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    postalCode: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    country: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    owner: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    __v: str = attr.ib(default=None)
    