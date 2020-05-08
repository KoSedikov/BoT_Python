# Перечисления команд, режимов
from command_enum import Command
from mode_enum import Mode

class Commander:

    def input(self, msg):
        """
        Функция принимающая сообщения пользователя
        :param msg: Сообщение
        :return: Ответ пользователю, отправившему сообщение
        """


        return "Команда не распознана!"