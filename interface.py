import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import comunity_token

token = comunity_token


class BotInterface:

    def __init__(self, token):
        self.bot = vk_api.VkApi(token=token)

    def message_send(self, user_id, message, attachment=None):
        self.bot.method('messages.send',
                        {'user_id': user_id,
                         'message': message,
                         'attachment': attachment,
                         'random_id': get_random_id()
                         }
                        )

    def handler(self):
        longpoll = VkLongPoll(self.bot)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'привет':
                    self.message_send(event.user_id, 'хай')
                elif event.text.lower() == 'поиск':
                    self.message_send(event.user_id, 'введите имя')
                elif event.text.lower() == 'далее':
                    self.message_send(event.user_id, 'дальнейший поиск')
                else:
                    self.message_send(event.user_id, 'неизвестная команда')


# if __name__ == 'main':
#     bot = BotInterface(comunity_token)
#     bot.message_send()
