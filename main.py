import logging
import time

import config
from utils.hypixel_api import HypixelAPI
from utils.player_session_manager import PlayerSessionManager
from utils.telegram_bot_api import TelegramBotAPI


def main():
    logging.basicConfig(filename='logs.log', level=logging.ERROR,
                        format=config.BASIC_LOGGING_FORMAT)

    hypixel_api = HypixelAPI(config.HYPIXEL_API_KEY)
    player_session_manager = PlayerSessionManager()
    telegram_bot_api = TelegramBotAPI(config.TELEGRAM_BOT_TOKEN)

    while True:
        my_friends = hypixel_api.get_player_friends(config.MY_MINECRAFT_UUID)

        for friend in my_friends:
            friend_uuid = friend['uuidSender'] if friend['uuidSender'] != config.MY_MINECRAFT_UUID else friend['uuidReceiver']
            name = hypixel_api.get_player(friend_uuid)['displayname']
            session = hypixel_api.get_player_session(friend_uuid)

            if player_session_manager.is_session_changed(
                    name, session):
                if session['online']:
                    message = f'Your friend {name} joined Hypixel server. Game type: {session["gameType"]}.'
                else:
                    message = f'Your friend {name} left Hypixel server.'

                telegram_bot_api.send_message(
                    config.TELEGRAM_BOT_MY_CHAT_ID, message)

        time.sleep(config.CHECK_INTERVAL)


if __name__ == '__main__':
    main()
