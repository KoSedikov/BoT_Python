# Импортируем созданный нами класс Server
from server import Server
from config import vk_api_token
from config import bot_id
# Получаем из config.py наш api-token

server1 = Server(vk_api_token, bot_id, "server1")
# vk_api_token - API токен, от группа вконтакте
# bot_id - id сообщества-бота
# "server1" - имя сервера

server1.start()