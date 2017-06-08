from online.online import Online
from config.configuration import OnlineConfiguration

import asyncio


def main():
    online_config = OnlineConfiguration('./resource/config.ini')
    online_user = Online(token=online_config.token)
    loop = asyncio.get_event_loop()
    user = online_user.user
    user_info, ssh_key = None, None
    try:
        ssh_key, user_info = loop.run_until_complete(asyncio.gather(*[user.user_ssh_key, user.user]))
    except Exception as exception_message:
        print(exception_message)
    print(user_info)
    print(ssh_key)

if __name__ == '__main__':
    main()
