from online.online_request import OnlineRequest


class UserRequest(OnlineRequest):
    def __init__(self, token: str = None, online_request: OnlineRequest=None):
        if online_request is not None:
            self.__dict__ = online_request.__dict__
        elif token is not None:
            super().__init__(token=token)

    @property
    def user(self):
        return self.get('/user')

    @property
    def user_ssh_key(self):
        return self.get('/user/key/ssh')

    @property
    def user_ssh_key_id(self, ssh_id: str=None):
        return self.get('/user/ssh/key/{}'.format(ssh_id))

    def add_ssh_key_id(self, description: str, content: str):
        return self.post('/user/ssh/key', description=description, content=content)
