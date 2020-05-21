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
from keyboards import keyboard, keyboardMag, keyboardInKourse, keyboardBac, keyboardChoise, keyboardGroup


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
                    if not user_index:
                        user_index = 0
                    if playloader and playloader == '100':
                        arr_of_user[user_index] = user
                        file.save(arr_of_user)
                        self.send_msg(event.object.message['peer_id'], message, self.keyboardInKourse())
                    if playloader and playloader == '300':
                        self.send_msg(event.object.message['peer_id'], message, self.keyboardChoise())
                    if playloader == '22':
                        self.send_msg(event.object.message['peer_id'], message, self.keyboardBac())
                    elif playloader == '33':
                        print(playloader)
                        self.send_msg(event.object.message['peer_id'], message, self.keyboardMag())
                        user['course'] = user_index
                        arr_of_user[user_index] = user
                        file.save(arr_of_user)
                        print(playloader)
                    elif playloader :#== ('10') or ('20') or ('30') or ('40') or ('50') or ('60'):
                        self.send_msg(event.object.message['peer_id'], message, self.keyboardGroup())
                    # user['departament'] = playloader


    # Клавиатуры
    def keyboard(self):
        playLoad = (0)
        playLoad11 = (100)
        keyboard = VkKeyboard()
        keyboard.add_button("Поздароваться", VkKeyboardColor.POSITIVE, playLoad)
        keyboard.add_button("Записаться к боту", VkKeyboardColor.PRIMARY, playLoad11)
        keyboard.add_button("Узнать какая сейчас неделя", VkKeyboardColor.PRIMARY, playLoad)
        return keyboard.get_keyboard()


    def keyboardInKourse(self):
        playLoad22 = (0)
        playLoad33 = (300)
        playLoad33 = (300)
        playLoad111 = (0)
        keyboardInKourse = VkKeyboard()
        keyboardInKourse.add_button("бакалавр или магистр", VkKeyboardColor.POSITIVE, playLoad33)
        keyboardInKourse.add_line()
        keyboardInKourse.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad22)
        keyboardInKourse.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE,playLoad111)
        return keyboardInKourse.get_keyboard()


    def keyboardChoise(self):
        playLoadch = (22)
        playLoadch1 = (33)
        playLoad11 = (100) # Вернуться назад
        playLoad111 = (0)  # Возвращаемся в начало
        keyboardChoise = VkKeyboard()
        keyboardChoise.add_button("Бакалавриат", VkKeyboardColor.POSITIVE, playLoadch)
        keyboardChoise.add_button("Магистратура", VkKeyboardColor.PRIMARY, playLoadch1)
        keyboardChoise.add_line()
        keyboardChoise.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)# Возвращаемся назад
        keyboardChoise.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE,playLoad111) # Возвращаемся в начало
        return keyboardChoise.get_keyboard()


    def keyboardBac(self):
        playLoad1 = (10)
        playLoad2 = (20)
        playLoad3 = (30)
        playLoad4 = (40)
        playLoad11 = (300)
        playLoad111 = (0)# Возвращаемся назад
        keyboardBac = VkKeyboard()
        keyboardBac.add_button("1", VkKeyboardColor.POSITIVE, playLoad1)
        keyboardBac.add_button("2", VkKeyboardColor.POSITIVE, playLoad2)
        keyboardBac.add_button("3", VkKeyboardColor.PRIMARY, playLoad3)
        keyboardBac.add_button("4", VkKeyboardColor.PRIMARY, playLoad4)
        keyboardBac.add_line()
        keyboardBac.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)# Возвращаемся назад
        keyboardBac.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)# Возвращаемся в начало
        return keyboardBac.get_keyboard()


    def keyboardMag(self):
        playLoad5 = (50)
        playLoad6 = (60)
        keyboardMag = VkKeyboard()
        keyboardMag.add_button("1", VkKeyboardColor.PRIMARY, playLoad5)
        keyboardMag.add_button("2", VkKeyboardColor.PRIMARY, playLoad6)
        return keyboardMag.get_keyboard()

    def keyboardGroup(self):
        playLoadFIIT = (100)
        playLoadMOAIS = (6100)
        playLoadMMM = (300)
        playLoadBI = (400)
        playLoadPI = (7200)
        playLoadPMI = (2600)
        playLoad111 = (0) #Возвращение в начало
        playLoad11 = (300)#Возвращение назад
        keyboardGroup = VkKeyboard()
        keyboardGroup.add_button("ФИИТ", VkKeyboardColor.PRIMARY,playLoadFIIT)
        keyboardGroup.add_button("МОАИС", VkKeyboardColor.PRIMARY,playLoadMOAIS)
        keyboardGroup.add_button("МММ", VkKeyboardColor.PRIMARY,playLoadMMM)
        keyboardGroup.add_line()
        keyboardGroup.add_button("БИ", VkKeyboardColor.PRIMARY,playLoadBI)
        keyboardGroup.add_button("ПИ", VkKeyboardColor.PRIMARY,playLoadPI)
        keyboardGroup.add_button("ПМИ", VkKeyboardColor.PRIMARY,playLoadPMI)
        keyboardGroup.add_line()
        keyboardGroup.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)  # Возвращаемся назад
        keyboardGroup.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
        return keyboardGroup.get_keyboard()
