from bot.kinobot import start_bot

if __name__ == '__main__':
    try:
        start_bot()
    except KeyboardInterrupt:
        print('Stop')
        exit(0)
