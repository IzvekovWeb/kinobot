from telebot import types


def generate_markup():
    """
    Создаем кастомную клавиатуру
    :return: Объект кастомной клавиатуры
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    all_answers = '{},{}'.format('1', '2')

    list_items = []
    for item in all_answers.split(','):
        list_items.append(item)

    for item in list_items:
        markup.add(item)
    return markup
