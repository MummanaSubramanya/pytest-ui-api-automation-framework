import attr

@attr.s
class UserInfo:
    _id: str = attr.ib(default=None)
    firstName: str = attr.ib(default=None)
    lastName: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    __v: int = attr.ib(default=None)

@attr.s
class User:
    firstName: str = attr.ib(default=None)
    lastName: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    password: str = attr.ib(default=None)
    
    def to_dict(self):
        return attr.asdict(self)
        
@attr.s
class RegisterUserResponse:
    user: UserInfo = attr.ib(default=None, validator=attr.validators.instance_of(UserInfo))
    token: str = attr.ib(default=None, validator=attr.validators.instance_of(str))


@attr.s  
class ErrorResponse:
    message: str = attr.ib(default=None, validator=attr.validators.instance_of(str))

@attr.s
class GetUserResponse:
    _id: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    firstName: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    lastName: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    email: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    __v: str = attr.ib(default=None)