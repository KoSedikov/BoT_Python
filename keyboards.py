from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor


# Клавиатуры
def keyboard():
    playLoad = (0)
    playLoad11 = (100)
    playLoadTable = (666)
    keyboard = VkKeyboard()
    keyboard.add_button("Поздароваться", VkKeyboardColor.POSITIVE, playLoad)
    keyboard.add_button("Записаться к боту", VkKeyboardColor.PRIMARY, playLoad11)
    keyboard.add_line()
    keyboard.add_button("Узнать какая сейчас неделя", VkKeyboardColor.PRIMARY, playLoad)
    keyboard.add_button("Узнать расписание", VkKeyboardColor.PRIMARY, playLoadTable)
    return keyboard.get_keyboard()


def keyboardInKourse():
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


def keyboardChoise():
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


def keyboardBac():
    playLoad10 = (10)
    playLoad20 = (20)
    playLoad30 = (30)
    playLoad40 = (40)
    playLoad11 = (300)
    playLoad111 = (0)  # Возвращаемся назад
    keyboardBac = VkKeyboard()
    keyboardBac.add_button("1", VkKeyboardColor.POSITIVE, playLoad10)
    keyboardBac.add_button("2", VkKeyboardColor.POSITIVE, playLoad20)
    keyboardBac.add_button("3", VkKeyboardColor.PRIMARY, playLoad30)
    keyboardBac.add_button("4", VkKeyboardColor.PRIMARY, playLoad40)
    keyboardBac.add_line()
    keyboardBac.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)  # Возвращаемся назад
    keyboardBac.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
    return keyboardBac.get_keyboard()


def keyboardMag():
    playLoad50 = (50)
    playLoad60 = (60)
    playLoad111 = (0)  # Возвращение в начало
    playLoad11 = (300)  # Возвращение назад
    keyboardMag = VkKeyboard()
    keyboardMag.add_button("1", VkKeyboardColor.PRIMARY, playLoad50)
    keyboardMag.add_button("2", VkKeyboardColor.PRIMARY, playLoad60)
    keyboardMag.add_line()
    keyboardMag.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)  # Возвращаемся назад
    keyboardMag.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
    return keyboardMag.get_keyboard()


def keyboardGroup():
    playLoadGroup1 = (1)
    playLoadGroup61 = (61)
    playLoadGroup62 = (62)
    playLoadGroup72 = (72)
    playLoadGroup71 = (71)
    playLoadGroup3 = (3)
    playLoadGroup4 = (4)
    playLoadGroup5 = (5)
    playLoad111 = (0)  # Возвращение в начало
    playLoad11 = (300)  # Возвращение назад
    keyboardGroup = VkKeyboard()
    keyboardGroup.add_button("61", VkKeyboardColor.PRIMARY, playLoadGroup61)
    keyboardGroup.add_button("62", VkKeyboardColor.PRIMARY, playLoadGroup62)
    keyboardGroup.add_button("1", VkKeyboardColor.PRIMARY, playLoadGroup1)
    keyboardGroup.add_line()
    keyboardGroup.add_button("71", VkKeyboardColor.PRIMARY, playLoadGroup71)
    keyboardGroup.add_button("72", VkKeyboardColor.PRIMARY, playLoadGroup72)
    keyboardGroup.add_button("3", VkKeyboardColor.PRIMARY, playLoadGroup3)
    keyboardGroup.add_line()
    keyboardGroup.add_button("4", VkKeyboardColor.PRIMARY, playLoadGroup4)
    keyboardGroup.add_button("5", VkKeyboardColor.PRIMARY, playLoadGroup5)
    keyboardGroup.add_line()
    keyboardGroup.add_button("Вернуться", VkKeyboardColor.NEGATIVE, playLoad11)  # Возвращаемся назад
    keyboardGroup.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
    return keyboardGroup.get_keyboard()


def keyboardTable():
     playLoadMonday = (1001)
     playLoadTuesday = (1002)
     playLoadWednesday = (1003)
     playLoadThursday = (1004)
     playLoadFriday = (1005)
     playLoadSaturday = (1006)
     playLoadSunday = (1007)
     playLoad111 = (0)  # Возвращение в начало

     keyboardTable = VkKeyboard()
     keyboardTable.add_button("Понедельник", VkKeyboardColor.POSITIVE, playLoadMonday)
     keyboardTable.add_button("Вторник", VkKeyboardColor.POSITIVE, playLoadTuesday)
     keyboardTable.add_line()
     keyboardTable.add_button("Среда", VkKeyboardColor.POSITIVE, playLoadWednesday)
     keyboardTable.add_button("Четверг", VkKeyboardColor.POSITIVE, playLoadThursday)
     keyboardTable.add_line()
     keyboardTable.add_button("Пятница", VkKeyboardColor.POSITIVE, playLoadFriday)
     keyboardTable.add_button("Суббота", VkKeyboardColor.POSITIVE, playLoadSaturday)
    # keyboardTable.add_button("Воскресенье", VkKeyboardColor.POSITIVE, playLoadSunday)
     keyboardTable.add_line()
     keyboardTable.add_button("Вернуться в начало", VkKeyboardColor.NEGATIVE, playLoad111)  # Возвращаемся в начало
     return keyboardTable.get_keyboard()



def keyboardYesNo():
    playLoadYes = (101)
    playLoadNo = (202)
    keyboardYesNo = VkKeyboard()
    keyboardYesNo.add_button("Да", VkKeyboardColor.POSITIVE, playLoadYes)
    keyboardYesNo.add_button("Нет", VkKeyboardColor.NEGATIVE, playLoadNo)
    return keyboardYesNo.get_keyboard()
