import vk_api
from pprint import pprint
from psycopg2 import Error
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import comunity_token, acces_token
from core import VkTools
from data_store import Viewed


class BotInterface:
    def __init__(self, comunity_token, acces_token):
        self.interface = vk_api.VkApi(token=comunity_token)
        self.api = VkTools(acces_token)
        self.data_store = Viewed()
        self.params = None

    def message_send(self, user_id, message, attachment=None):
        self.interface.method('messages.send',
                              {'user_id': user_id,
                               'message': message,
                               'attachment': attachment,
                               'random_id': get_random_id()
                               }
                              )

    def worksheets(self):
        global attachment
        longpoll = VkLongPoll(self.interface)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                command = event.text.lower()

                if command == 'привет':
                    self.params = self.api.get_profile_info(event.user_id)
                    self.message_send(event.user_id, f'здравствуй {self.params["name"]}')
                elif command == 'поиск':
                    users = self.api.search_users(self.params)
                    user = users.pop()

                    if users == users:
                        self.interface = self.api.search_users(event.user_id)
                        return users
                    else:
                        self.message_send(event.user_id, f'введите недостающие данные {self.interface["params"]}')

                    photos_user = self.api.get_photos(user['id'])

                    if self.worksheets:
                        worksheets = self.worksheets.pop()
                        photos_user = self.api.get_photos(worksheets['id'])

                        self.message_send(event.user_id, f'имя: {worksheets["name"]} '
                                                         f'ссылка: vk.com/{worksheets["id"]}'),
                        attachment = ''
                    for num, photo in enumerate(photos_user):
                        attachment += f'photo{photo["owner_id"]}_{photo["id"]}'
                        if num == 2:
                            break
                    self.message_send(event.user_id,
                                      f'Встречайте {user["name"]}',
                                      attachment=attachment
                                      )

                    try:
                        Viewed.check_user == Viewed.check_user
                    except (Exception, Error) as error:
                        print('Ошибка базы данных', error)

                elif command == 'пока':
                    self.message_send(event.user_id, 'пока')
                else:
                    self.message_send(event.user_id, 'команда не опознана')


if __name__ == '__main__':
    bot = BotInterface(comunity_token, acces_token)
    params = bot.api.get_profile_info(789657038)
    users = bot.api.search_users(params)
    pprint(bot.api.get_photos(users[2]['id']))
