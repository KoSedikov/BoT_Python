import vk_api.vk_api
import random
import pprint

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType


class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        self.server_name = server_name
        self.vk = vk_api.VkApi(token=api_token)
        self.long_poll = VkBotLongPoll(self.vk, group_id)
        self.vk_api = self.vk.get_api()

    def send_msg(self, send_id, message):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        self.vk_api.messages.send(peer_id=send_id,message=message,random_id = random.randint(0,2000))

    def start(self):
        for event in self.long_poll.listen():  # Слушаем сервер

            # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:
                username = self.get_user_name(event.object.message['from_id'])
                print("Ай-ДИ пользователя:")
                pprint.pprint(event.object.message['from_id'])
                print("Текст сообщения:")
                pprint.pprint(event.object.message['text'])
                #Простейшая логика бота.
                if event.object.message['text'].lower() == ("привет" or "здравствуйте" or "приветули" or "здрасте"):
                    self.send_msg(121787026, "Привет-привет, \n Как настроение!?)")
                else:
                    self.send_msg(121787026, '{0},Извини,не понял тебя!'.format(username['first_name']))



    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]

    def get_user_city(self, user_id):
        """ Получаем город пользователя"""
        return self.vk_api.users.get(user_id=user_id, fields="city")[0]["city"]['title']

    def send_message(self, peer_id, message):
        self.vk_api.messages.send(peer_id=peer_id, message=message)