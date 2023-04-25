import self as self
import vk_api
from config import acces_token
from vk_api.exceptions import ApiError

token = acces_token


class VkTools:
    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=token)

    def get_profile_info(self, user_id):

        try:
            info = self.ext_api.method('users.get',
                                       {'user_id': user_id,
                                        'fields': 'bdate,city,sex,relation'
                                        }
                                       )
        except ApiError:
            return

        return info

    def user_search(self, city_id, age_from, age_to, sex, relation, offset=None):

        try:
            profiles = self.ext_api.method('users.search',
                                           {'city_id': city_id,
                                            'age_from': age_from,
                                            'age_to': age_to,
                                            'sex': sex,
                                            'relation': relation,
                                            'count': 30,
                                            'offset': offset
                                            }
                                           )
        except ApiError:
            return

        profiles = profiles['items']

        result = []
        for profile in profiles:
            if not profile['is_closed']:
                result.append({'name': profile['first_name'] + ' ' + profile['last_name'],
                               'id': profile['id']
                               })

        return result

    def photos_get(self, user_id):
        photos = self.ext_api.method('photos.get',
                                     {'album_id': 'profile',
                                      'owner_id': user_id
                                      }
                                     )

        try:
            photos = photos['items']
        except KeyError:
            return

        result = []
        for num, photo in enumerate(photos):
            result.append({'owner_id': photo['owner_id'],
                           'id': photo['id']
                           })

            num = photo['likes']['count'] + photo['comments']['count']
            result.append((num, photo))
            if len(result) > 2:
                result.sort(reverse=True)
                return [result[0][1], result[1][1], result[2][1]]
            else:
                return False

        return result


# if __name__ == 'main':
#     tools = VkTools(acces_token)
#     # print(tools.get_profile_info(#))
#     # profiles = tools.user_search(1, 20, 40, 1)
#     # print(profiles)
#     photos = tools.photos_get()
#     print(photos)
