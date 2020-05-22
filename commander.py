import vk_api
import datetime

from datetime import datetime

arr_of_user = []

class Commander:

    @staticmethod
    def get_queue():
        i = 1
        users = []
        for user in arr_of_user:
            full_name = user['full_name']
            users.append(str(i) + '. ' + full_name)
            i = i + 1
        return users

    def now_week(self):
        timenow = datetime.now().isocalendar()
        if timenow[1]%2 == 0:return ", сейчас числитель."
        else: return ", сейчас знаменатель."



    def input(self, msg, server, user):

        """
        Функция принимающая сообщения пользователя
        :param user: Пользоватлеь который написал сообщение
        :param server: сервер
        :param msg: Сообщение
        :return: Ответ пользователю, отправившему сообщение
        """
        text = msg['text']
        sex = user['sex']

        if text == 'Поздароваться':
            return 'Привет, ' + user['full_name']



        elif text == 'Записаться к боту':
            if user in arr_of_user:
                return "Ты уже записан!"
            arr_of_user.append(user)
            return 'Записываем...'


        elif text == 'Узнать какая сейчас неделя':
         return user['full_name'] + str(self.now_week())

        elif text == 'бакалавр или магистр':
            return "Бакалавриат или магистратура?"

        elif text == 'Введите свой курс':
            return "Итак, твой курс? =)"

        elif text == 'Вернуться':
            return "Хмм, ты все же решил вернуться..."

        elif text == 'Бакалавриат':
            return "Какой курс бакалавриата?"

        elif text == 'Магистратура':
            return "Ого! Ты уже магистр! А какой курс?"

        elif text == '1':
            return "Ты первый курс..."

        elif text == '2':
            return "Ты уже второй курс!"

        elif text == '3':
            return "Ты уже третий курс!!!"

        elif text == '4':
            return "Выпускной четвертый курс!"
        elif text == 'Вернуться в начало':
            return 'Возвращаемся в самое начало!'






        return "Команда не распознана!"