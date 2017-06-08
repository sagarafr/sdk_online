from online_request.online_request import OnlineRequest
from online_request.user_request import UserRequest


class Online:
    def __init__(self, token: str, online_request: OnlineRequest=None):
        self._online = OnlineRequest(token=token) if online_request is None else online_request
        self._user = UserRequest(online_request=self._online)

    @property
    def user(self):
        return self._user
