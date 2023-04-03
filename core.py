import vk_api
from config import acces_token


class VkTools():
    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=token)

        def get_profile_info(self, user_id):
            info = self.vk_api.method('users.get',
                                      {'user_id': user_id
                                       'fields': 'bdate,city,sex,relation'

                                      }
                                      )


            return info
