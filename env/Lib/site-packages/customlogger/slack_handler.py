import json
import logging
import os

import requests


class SlackHandler(logging.Handler):
    # emojis {{{1
    emojis = {
        logging.NOTSET: ':loudspeaker:',
        logging.DEBUG: ':simple_smile:',
        logging.INFO: ':smile:',
        logging.WARNING: ':sweat:',
        logging.ERROR: ':sob:',
        logging.CRITICAL: ':scream:'
    }

    # usernames {{{1
    usernames = {
        logging.NOTSET: 'Notset',
        logging.DEBUG: 'Debug',
        logging.INFO: 'Info',
        logging.WARNING: 'Warning',
        logging.ERROR: 'Erorr',
        logging.CRITICAL: 'Critical',
    }

    # }}}

    def __init__(  # {{{1
            self,
            webhook_url=None,
            token=None,
            channel=None,
            usernames=None,
            emojis=None,
            fmt='[%(levelname)s] [%(asctime)s] [%(name)s] - %(message)s',
            as_user=False,
    ):
        super().__init__()
        self.__webhook_url = webhook_url or os.getenv('WEBHOOK_URL')
        if not self.__webhook_url:
            print('WARN: Not found WEBHOOK_URL. SlackHandler not work.')
            self.__isDisabled = True
            return None

        self.__token = token
        self.__isDisabled = False
        self.__channel = channel
        self.__usernames = usernames if token else SlackHandler.usernames
        self.__emojis = emojis if token else SlackHandler.emojis
        self.__fmt = logging.Formatter(fmt)
        self.__as_user = as_user

    def setEmoji(self, levelno, emoji):  # {{{1
        if not self.__emojis:
            self.__emojis = self.emojis
        self.__emojis[levelno] = emoji

    def setUsernames(self, levelno, username):  # {{{1
        if not self.__usernames:
            self.__usernames = self.usernames
        self.__usernames[levelno] = username

    def makeContent(self, record):  # {{{1
        content = {
            'text': self.format(record),
        }

        if self.__emojis:
            content['icon_emoji'] = self.__emojis[record.levelno]
        if self.__usernames:
            content['username'] = self.__usernames[record.levelno]
        if self.__channel:
            content['channel'] = self.__channel
        if self.__as_user:
            content['as_user'] = self.__as_user

        if self.__token:
            content['token'] = self.__token
        else:
            content = json.dumps(content)

        return content

    def emit(self, record):  # {{{1
        try:
            if self.__isDisabled:
                return

            requests.post(self.__webhook_url, data=self.makeContent(record))
        except Exception:
            self.handleError(record)

    # }}} 1
