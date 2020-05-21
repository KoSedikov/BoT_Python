from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor


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
    keyboardInKourse.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)
    return keyboardInKourse.get_keyboard()


def keyboardChoise(self):
    playLoadch = (22)
    playLoadch1 = (33)
    playLoad11 = (100)  # Вернуться назад
    playLoad111 = (0)  # Возвращаемся в начало
    keyboardChoise = VkKeyboard()
    keyboardChoise.add_button("Бакалавриат", VkKeyboardColor.POSITIVE, playLoadch)
    keyboardChoise.add_button("Магистратура", VkKeyboardColor.PRIMARY, playLoadch1)
    keyboardChoise.add_line()
    keyboardChoise.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)  # Возвращаемся назад
    keyboardChoise.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
    return keyboardChoise.get_keyboard()


def keyboardBac(self):
    playLoad1 = (10)
    playLoad2 = (20)
    playLoad3 = (30)
    playLoad4 = (40)
    playLoad11 = (300)
    playLoad111 = (0)  # Возвращаемся назад
    keyboardBac = VkKeyboard()
    keyboardBac.add_button("1", VkKeyboardColor.POSITIVE, playLoad1)
    keyboardBac.add_button("2", VkKeyboardColor.POSITIVE, playLoad2)
    keyboardBac.add_button("3", VkKeyboardColor.PRIMARY, playLoad3)
    keyboardBac.add_button("4", VkKeyboardColor.PRIMARY, playLoad4)
    keyboardBac.add_line()
    keyboardBac.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)  # Возвращаемся назад
    keyboardBac.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
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
    playLoad111 = (0)  # Возвращение назад
    playLoad11 = (300)  # Возвращение в начало
    keyboardGroup = VkKeyboard()
    keyboardGroup.add_button("ФИИТ", VkKeyboardColor.PRIMARY, playLoadFIIT)
    keyboardGroup.add_button("МОАИС", VkKeyboardColor.PRIMARY, playLoadMOAIS)
    keyboardGroup.add_button("МММ", VkKeyboardColor.PRIMARY, playLoadMMM)
    keyboardGroup.add_line()
    keyboardGroup.add_button("БИ", VkKeyboardColor.PRIMARY, playLoadBI)
    keyboardGroup.add_button("ПИ", VkKeyboardColor.PRIMARY, playLoadPI)
    keyboardGroup.add_button("ПМИ", VkKeyboardColor.PRIMARY, playLoadPMI)
    keyboardGroup.add_line()
    keyboardGroup.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)  # Возвращаемся назад
    keyboardGroup.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
    return keyboardGroup.get_keyboard()