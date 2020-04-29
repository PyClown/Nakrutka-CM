from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api, sys, colorama, time
colorama.init()
print(colorama.Fore.CYAN + 'Reverse by vk.com/pivo.json and vk.com/lakebug')
TOKEN = input('[*]Ввведите токен от страницы: ')
PEER_ID = input('[*]Введите чат куда будут идти сообщения(без +2000000000) : ')

def main():
    print(colorama.Fore.GREEN + '***************\n\n[*]Соеденение с сервером VK API..')
    try:
        vk_session = vk_api.VkApi(token=TOKEN)
        print(colorama.Fore.GREEN + '[*]Отправка данных для подключения..')
        vk = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        print(colorama.Fore.GREEN + '[*]Сессия создана')
        print(colorama.Fore.GREEN + '[*]Успешной подключение!\n\n***************')
    except Exception as e:
        try:
            print(colorama.Fore.RED + f"\n[*]Ошибка соединения с API VK. Возможно неверные данные или двухфакторка\n{e}")
            sys.exit()
        finally:
            e = None
            del e

    count_message = 0
    print(colorama.Fore.YELLOW + '[*]Начинаю накрутку')
    try:
        while True:
            message_id1 = vk.messages.send(peer_id=(2000000000 + int(PEER_ID)), random_id=0, message='&#2;')
            vk.messages.delete(message_ids=message_id1, delete_for_all=1)
            message_id2 = vk.messages.send(peer_id=(2000000000 + int(PEER_ID)), random_id=0, message='&#2;')
            vk.messages.delete(message_ids=message_id2, delete_for_all=1)
            message_id3 = vk.messages.send(peer_id=(2000000000 + int(PEER_ID)), random_id=0, message='&#2;')
            vk.messages.delete(message_ids=message_id3, delete_for_all=1)
            message_id4 = vk.messages.send(peer_id=(2000000000 + int(PEER_ID)), random_id=0, message='&#2;')
            vk.messages.delete(message_ids=message_id4, delete_for_all=1)
            count_message += 3
            time.sleep(12)

    except KeyboardInterrupt:
        print(f"\n\n[*]Всего {count_message} сообщений отправлено")
        print('[*]Unpacked by vk.com/pivo.json ')
        sys.exit()
    else:
        print('Ошибка. Возможно ид чата введен неверно')


if name == 'main':
    main()
