def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    fl_rec = bool
    fl_sen = bool
    if '@' in sender:
        if '.com' in sender:
            fl_sen = True
        elif '.ru' in sender:
            fl_sen = True
        elif '.net' in sender:
            fl_sen = True
        else:
            fl_sen = False
    else:
        fl_sen = False
    if '@' in recipient:
        if '.' in recipient:
            fl_rec = True
    else:
        fl_rec = False
    if fl_sen != fl_rec or False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender != 'university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
