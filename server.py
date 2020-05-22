import random

import vk_api.vk_api
import keyboards
import json

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor
from commander import Commander, arr_of_user
from file_manager import File
from keyboards import keyboard, keyboardMag, keyboardInKourse, keyboardBac, keyboardChoise, keyboardGroup, keyboardYesNo, keyboardTable


class Server():

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        # Даем серверу имя
        self.server_name = server_name

        self.group_id = group_id

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использоания Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id, wait=30)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

        # Словарь дял каждого отдельного пользователя
        self.users = {}
        self.creator = 121787026
        self.admins = []

    def add_admin(self, id):
        if id in self.admins:
            return False
        self.admins.append(id)
        return True

    def remove_admin(self, id):
        if id in self.admins:
            index = self.admins.index(id)
            del self.admins[index]
            return True
        return False

    def send_msg(self, send_id, message, keyboard):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        return self.vk_api.messages.send(peer_id=send_id,
                                         message=message,
                                         random_id=random.randint(0, 2048),
                                         keyboard=keyboard)

    def get_user_by_id(self, user_id):
        user = self.vk_api.users.get(user_id=user_id, fields="sex")[0]
        first_name = user['first_name']
        last_name = user['last_name']
        full_name = first_name + ' ' + last_name
        sex = user['sex']

        return {
            'id': int(user_id),
            'full_name': full_name,
            'sex': sex
        }

    def start(self):

        for event in self.long_poll.listen():  # Слушаем сервер

            if event.type == VkBotEventType.MESSAGE_NEW:

                playloader = event.raw['object']['message'].get('payload')
                if event.object.message['from_id'] not in self.users:
                    self.users[event.object.message['from_id']] = Commander()
                # Пришло новое сообщение
                if event.type == VkBotEventType.MESSAGE_NEW:
                    msg = event.object.message
                    peer_id = msg['peer_id']

                    file = File()
                    file.save(arr_of_user)

                    user = None
                    user_index = None
                    for index, u in enumerate(arr_of_user):
                        if u['id'] == peer_id:
                            user = u
                            user_index = index
                            break
                    if user is None:
                        user = self.get_user_by_id(peer_id)

                    message = self.users[event.object.message['from_id']].input(event.object.message, self,
                                                                                user)
                    fromId = event.object.message['from_id']
                    user_in = True
                    if not user_index:
                        user_index = len(arr_of_user) - 1
                        user_in = False
                    if playloader and playloader == '666':
                        message = 'А ты уже записан к боту?'
                        self.send_msg(event.object.message['peer_id'], message, keyboardYesNo())
                    elif playloader == '202':
                        message = 'Обязательно запишись к боту! \n Без этого он не сможет тебе плмочь)'
                        self.send_msg(event.object.message['peer_id'], message,keyboardInKourse())
                    elif playloader and playloader == '101':
                        message = 'По какому дню недели нужно расписание?'
                        self.send_msg(event.object.message['peer_id'], message, keyboardTable())
                    elif playloader and playloader == '100':
                        if not user_in:
                            message = 'Ты уверен? Ты уже был записан ранее.'
                        self.send_msg(event.object.message['peer_id'], message, keyboardInKourse())
                    elif playloader and playloader == '300':
                        self.send_msg(event.object.message['peer_id'], message, keyboardChoise())
                    elif playloader == '22':
                        self.send_msg(event.object.message['peer_id'], message, keyboardBac())
                    elif playloader == '33':
                        self.send_msg(event.object.message['peer_id'], message, keyboardMag())
                    elif playloader in ['10', '20','30','40','50','60']:
                        user['course'] = playloader
                        arr_of_user[user_index] = user
                        file.save(arr_of_user)
                        message = 'В какой группе ты учишься??'
                        self.send_msg(event.object.message['peer_id'], message, keyboardGroup())
                    elif playloader in ['1','2','3','4','5','61','62','71','72']:
                        user['group'] = playloader
                        print(playloader)
                        arr_of_user[user_index] = user
                        file.save(arr_of_user)
                        message = 'Твои данные были успешно записаны!'
                        self.send_msg(event.object.message['peer_id'], message, keyboard())
                    else:
                        self.send_msg(event.object.message['peer_id'], message, keyboard())
