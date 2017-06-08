from online_request.online_request import OnlineRequest

from os.path import isfile


class UserRequest(OnlineRequest):
    def __init__(self, token: str = None, online_request: OnlineRequest=None):
        if online_request is not None:
            self.__dict__ = online_request.__dict__
        elif token is not None:
            super().__init__(token=token)

    @property
    async def user(self):
        return await self.get('/user')

    @property
    async def user_ssh_key(self):
        return await self.get('/user/key/ssh')

    async def user_ssh_key_id(self, ssh_id: str=None):
        return await self.get('/user/ssh/key/{}'.format(ssh_id))

    async def add_ssh_key_id(self, description: str, content: str = None, filename: str = None):
        if filename is not None and isfile(filename):
            with open(filename, 'r') as fd_file:
                return await self.post('/user/ssh/key', description=description, content=''.join(fd_file.readlines()))
        elif content is not None:
            return await self.post('/user/ssh/key', description=description, content=content)
        raise ValueError("filename or content is None")
