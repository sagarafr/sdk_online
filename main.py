from online.online import Online
from config.configuration import OnlineConfiguration


def main():
    online_config = OnlineConfiguration('./resource/config.ini')
    online_user = Online(token=online_config.token)
    user = online_user.user
    print(user.user)
    print(user.user_ssh_key)


if __name__ == '__main__':
    main()
